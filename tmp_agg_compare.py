import json,re,difflib,collections
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
# load raw xlsx values
matrix=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_values.json',encoding='utf8'))['台账']['values']
# rows indexed 1-based Excel
issue_starts=[]
for i in range(5,len(matrix)):
 r=matrix[i]
 if r[4] is not None and str(r[4]).strip()!='': issue_starts.append((i,int(r[4])))
# aggregate ranges from start to next issue start
agg={}
for idx,(start,no) in enumerate(issue_starts):
 end=issue_starts[idx+1][0] if idx+1<len(issue_starts) else len(matrix)
 rows=matrix[start:end]
 def join(col):
  out=[]
  for r in rows:
   v=r[col] if col<len(r) else None
   if v is not None and str(v).strip()!='': out.append(str(v))
  return '\n'.join(out)
 first=rows[0]
 agg[no]={
  'start':start+1,'end':end,
  'groupIssue':first[5], 'groupLeader':first[7], 'groupLeadDept':first[8], 'groupRespDept':first[9], 'groupCoordDept':first[10], 'groupCities':first[11],
  'groupMeasures':join(13),'groupTargets':join(14),'groupDeadline':first[15],
  'groupInspection':join(16), 'selfIssue':first[17], 'selfLeader':first[19], 'selfLeadDept':first[20], 'selfRespDept':first[21], 'selfCoordDept':first[22], 'selfCities':first[23],
  'localMeasures':join(25),'localTargets':join(26),'localDeadline':join(27), 'measureRows':end-start
 }

def norm(s):
 s=str(s or '')
 s=s.replace('（自查不存在此问题）','').replace('(自查不存在此问题)','').replace('（集团巡视反馈）','')
 s=re.sub(r'[\s\u200c\u200b]+','',s)
 # normalize punctuation and numbering comma
 return s.replace('“','').replace('”','').replace('"','').replace(',','，').replace('：',':')
def sim(a,b): return difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()

def fval(f,k):
 return f.get(k)
summary=[]
for w in wr:
 no=w['num']; x=agg[no]; wf=w['fields']; wm=wf.get('整改措施') or wf.get('防范措施'); wt=wf.get('整改目标') or wf.get('达成目标');
 gs=sim(w['issue'],x['groupIssue']); ls=sim(w['issue'],x['selfIssue']) if x['selfIssue'] else 0
 source='group' if gs>=ls else 'local'
 if source=='group': vals={'issue':x['groupIssue'],'leader':x['groupLeader'],'resp':x['groupRespDept'],'coord':x['groupCoordDept'],'measure':x['groupMeasures'],'target':x['groupTargets'],'deadline':x['groupDeadline']}
 else: vals={'issue':x['selfIssue'],'leader':x['selfLeader'],'resp':x['selfRespDept'],'coord':x['selfCoordDept'],'measure':x['localMeasures'],'target':x['localTargets'],'deadline':x['localDeadline']}
 wvals={'issue':w['issue'],'leader':wf.get('责任领导'),'resp':wf.get('责任部门'),'coord':wf.get('配合部门'),'measure':wm,'target':wt,'deadline':wf.get('完成时限')}
 sims={k:sim(wvals[k],vals[k]) if vals[k] else 0 for k in wvals}
 exact={k:norm(wvals[k])==norm(vals[k]) for k in wvals}
 summary.append({'no':no,'source':source,'issueSim':max(gs,ls),'groupSim':gs,'localSim':ls,'sims':sims,'exact':exact,'word':wvals,'excel':vals,'rows':x['measureRows'],'start':x['start'],'end':x['end']})
json.dump({'agg':agg,'summary':summary},open(r'E:\\sl_obsidian\\tmp_agg_compare.json','w',encoding='utf8'),ensure_ascii=False,indent=2)
# stats
print('issues',len(summary),'measure rows total',sum(s['rows'] for s in summary),'group measure rows',sum(1 for i in range(5,len(matrix)) if matrix[i][12] is not None),'local measure rows',sum(1 for i in range(5,len(matrix)) if matrix[i][24] is not None))
print('source',collections.Counter(s['source'] for s in summary))
for k in ['issue','leader','resp','coord','measure','target','deadline']:
 print(k,'exact',sum(s['exact'][k] for s in summary),'sim>=.95',sum(s['sims'][k]>=.95 for s in summary),'sim<.8',sum(s['sims'][k]<.8 for s in summary))
print('\nDetailed low measure/target sims:')
for s in summary:
 if s['sims']['measure']<.8 or s['sims']['target']<.8:
  print(s['no'],s['source'],'measure',round(s['sims']['measure'],2),'target',round(s['sims']['target'],2),'lens',len(str(s['word']['measure'] or '')),len(str(s['excel']['measure'] or '')),len(str(s['word']['target'] or '')),len(str(s['excel']['target'] or '')),'deadline',s['word']['deadline'],s['excel']['deadline'])
print('\nDeadline differences:')
for s in summary:
 if norm(s['word']['deadline'])!=norm(s['excel']['deadline']): print(s['no'],s['source'],s['word']['deadline'],'vs',s['excel']['deadline'])





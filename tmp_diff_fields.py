import json,re,difflib,os
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
xr=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_issues.json',encoding='utf8'))['rows']

def norm(s):
 s=str(s or '')
 s=s.replace('（自查不存在此问题）','').replace('(自查不存在此问题)','').replace('（集团巡视反馈）','')
 s=re.sub(r'[\s\u200c\u200b]+','',s)
 s=s.replace('“','').replace('”','').replace('"','').replace('，',',').replace('。','.')
 return s

def sim(a,b): return difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()
rows=[]
for w,x in zip(wr,xr):
 g=sim(w['issue'],x.get('groupIssue')); l=sim(w['issue'],x.get('localIssue')) if x.get('localIssue') else 0
 source='group' if g>=l else 'local'; score=max(g,l)
 xf={
  'leader': x.get('groupLeader') if source=='group' else x.get('localLeader'),
  'leadDept': x.get('groupLeadDept') if source=='group' else x.get('localLeadDept'),
  'respDept': x.get('groupRespDept') if source=='group' else x.get('localRespDept'),
  'coordDept': x.get('groupCoordDept') if source=='group' else x.get('localCoordDept'),
  'measure': x.get('groupMeasure') if source=='group' else x.get('localMeasure'),
  'target': x.get('groupTarget') if source=='group' else x.get('localTarget'),
  'deadline': x.get('groupDeadline') if source=='group' else x.get('localDeadline'),
  'issue': x.get('groupIssue') if source=='group' else x.get('localIssue'),
 }
 wf=w['fields']; wfields={'leader':wf.get('责任领导'),'leadDept':None,'respDept':wf.get('责任部门'),'coordDept':wf.get('配合部门'),'measure':wf.get('整改措施') or wf.get('防范措施'),'target':wf.get('整改目标') or wf.get('达成目标'),'deadline':wf.get('完成时限'),'issue':w['issue']}
 diffs={}
 for k in ['issue','leader','respDept','coordDept','measure','target','deadline']:
  a=wfields[k]; b=xf[k]
  if norm(a)!=norm(b): diffs[k]={'word':a,'excel':b,'sim':sim(a,b)}
 rows.append({'no':w['num'],'source':source,'score':score,'gscore':g,'lscore':l,'diffs':diffs,'word':wfields,'excel':xf})
json.dump(rows,open(r'E:\\sl_obsidian\\tmp_field_diffs.json','w',encoding='utf8'),ensure_ascii=False,indent=2)
for r in rows:
 print(f"{r['no']} source={r['source']} score={r['score']:.2f} diffs={','.join(r['diffs']) or '-'}")

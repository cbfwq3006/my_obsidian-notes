import json,re,difflib
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
xr=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_issues.json',encoding='utf8'))['rows']

def norm(s):
 s=str(s or '')
 s=s.replace('（自查不存在此问题）','').replace('(自查不存在此问题)','').replace('（集团巡视反馈）','')
 return re.sub(r'[\s\u200c\u200b]+','',s)
def sim(a,b): return difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()
rows=[]
for w,x in zip(wr,xr):
 g=sim(w['issue'],x.get('groupIssue')); l=sim(w['issue'],x.get('localIssue')) if x.get('localIssue') else 0
 source='group' if g>=l else 'local'; score=max(g,l)
 xf={'leader':x.get('groupLeader') if source=='group' else x.get('localLeader'),'respDept':x.get('groupRespDept') if source=='group' else x.get('localRespDept'),'coordDept':x.get('groupCoordDept') if source=='group' else x.get('localCoordDept'),'measure':x.get('groupMeasure') if source=='group' else x.get('localMeasure'),'target':x.get('groupTarget') if source=='group' else x.get('localTarget'),'deadline':x.get('groupDeadline') if source=='group' else x.get('localDeadline'),'issue':x.get('groupIssue') if source=='group' else x.get('localIssue')}
 wf=w['fields']; wfields={'leader':wf.get('责任领导'),'respDept':wf.get('责任部门'),'coordDept':wf.get('配合部门'),'measure':wf.get('整改措施') or wf.get('防范措施'),'target':wf.get('整改目标') or wf.get('达成目标'),'deadline':wf.get('完成时限'),'issue':w['issue']}
 diffs=[]
 for k in ['issue','leader','respDept','coordDept','measure','target','deadline']:
  a=wfields[k]; b=xf[k]
  if norm(a)!=norm(b): diffs.append(k)
 rows.append((w['num'],source,score,g,l,diffs))
print('num\tsource\tbest\tgroup\tlocal\tdiffs')
for z in rows: print('\t'.join([str(z[0]),z[1],f'{z[2]:.3f}',f'{z[3]:.3f}',f'{z[4]:.3f}',','.join(z[5]) or '-']))

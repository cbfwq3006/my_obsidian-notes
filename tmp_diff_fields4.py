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
 g=sim(w['issue'],x.get('issue')); l=sim(w['issue'],x.get('selfIssue')) if x.get('selfIssue') else 0
 source='group' if g>=l else 'local'; score=max(g,l)
 # correct mapped keys
 if source=='group': xf={'leader':x.get('leader'),'respDept':x.get('respDept'),'coordDept':x.get('coordDept'),'measure':x.get('measure'),'target':x.get('target'),'deadline':x.get('deadline'),'issue':x.get('issue')}
 else: xf={'leader':x.get('selfLeader'),'respDept':x.get('selfRespDept'),'coordDept':x.get('selfCoordDept'),'measure':x.get('selfMeasure'),'target':x.get('selfTarget'),'deadline':x.get('selfDeadline'),'issue':x.get('selfIssue')}
 wf=w['fields']; wfields={'leader':wf.get('责任领导'),'respDept':wf.get('责任部门'),'coordDept':wf.get('配合部门'),'measure':wf.get('整改措施') or wf.get('防范措施'),'target':wf.get('整改目标') or wf.get('达成目标'),'deadline':wf.get('完成时限'),'issue':w['issue']}
 diffs=[]
 for k in ['issue','leader','respDept','coordDept','measure','target','deadline']:
  if norm(wfields[k])!=norm(xf[k]): diffs.append(k)
 rows.append((w['num'],source,score,g,l,diffs))
print('num\tsource\tbest\tgroup\tlocal\tdiffs')
for z in rows: print('\t'.join([str(z[0]),z[1],f'{z[2]:.3f}',f'{z[3]:.3f}',f'{z[4]:.3f}',','.join(z[5]) or '-']))

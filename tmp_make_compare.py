import json,re,difflib
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
xr=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_issues.json',encoding='utf8'))['rows']
def norm(s):
 s=str(s or '')
 s=s.replace('（自查不存在此问题）','').replace('(自查不存在此问题)','').replace('（集团巡视反馈）','')
 return re.sub(r'[\s\u200c\u200b]+','',s)
def sim(a,b): return difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()
def short(s,n=180):
 s=str(s or '').replace('\n',' / ')
 return s if len(s)<=n else s[:n]+'…'
def nums(s):
 return re.findall(r'\d+(?:\.\d+)?%?|\d+年|\d+月|\d+日|\d+个|\d+项|\d+万元|\d+亿元|\d+万|\d+元',str(s or ''))
rows=[]
for w,x in zip(wr,xr):
 wf=w['fields']; wm=wf.get('整改措施') or wf.get('防范措施'); wt=wf.get('整改目标') or wf.get('达成目标');
 sources=[('集团巡视',x.get('issue'),x.get('leader'),x.get('respDept'),x.get('coordDept'),x.get('measure'),x.get('target'),x.get('deadline')),('自查/市公司',x.get('selfIssue'),x.get('selfLeader'),x.get('selfRespDept'),x.get('selfCoordDept'),x.get('selfMeasure'),x.get('selfTarget'),x.get('selfDeadline'))]
 scores=[sim(w['issue'],s[1]) if s[1] else 0 for s in sources]
 # compare all fields to both, report best source per field
 out={'no':w['num'],'word_issue':w['issue'],'word':{'leader':wf.get('责任领导'),'respDept':wf.get('责任部门'),'coordDept':wf.get('配合部门'),'measure':wm,'target':wt,'deadline':wf.get('完成时限')},'excel':{},'match':{'issue_source':sources[scores.index(max(scores))][0] if max(scores)>0 else None,'issue_score':max(scores)}}
 for label,issue,lead,resp,coord,measure,target,deadline in sources:
  out['excel'][label]={'issue':issue,'leader':lead,'respDept':resp,'coordDept':coord,'measure':measure,'target':target,'deadline':deadline}
 # field best similarity and exact status
 for field,ww in [('leader',wf.get('责任领导')),('respDept',wf.get('责任部门')),('coordDept',wf.get('配合部门')),('measure',wm),('target',wt),('deadline',wf.get('完成时限'))]:
  vals=[s[{'leader':2,'respDept':3,'coordDept':4,'measure':5,'target':6,'deadline':7}[field]] for s in sources]
  ss=[sim(ww,v) if v else 0 for v in vals]
  out['match'][field]={'source':sources[ss.index(max(ss))][0] if max(ss)>0 else None,'score':max(ss),'exact':any(norm(ww)==norm(v) for v in vals if v is not None)}
 # numeric contradiction issue texts
 out['numbers']={'word':nums(w['issue']),'group':nums(x.get('issue')),'local':nums(x.get('selfIssue'))}
 rows.append(out)
json.dump(rows,open(r'E:\\sl_obsidian\\tmp_full_compare.json','w',encoding='utf8'),ensure_ascii=False,indent=2)
# concise text report
with open(r'E:\\sl_obsidian\\tmp_compare_report.txt','w',encoding='utf8') as f:
 for r in rows:
  f.write(f"问题{r['no']}：问题来源匹配={r['match']['issue_source']}({r['match']['issue_score']:.2f})；")
  f.write('字段最佳匹配：'+', '.join(f"{k}={v['source']}({v['score']:.2f})" for k,v in r['match'].items() if k not in ['issue_source','issue_score'])+'\n')
  f.write('  Word问题：'+short(r['word_issue'])+'\n')
  for label in ['集团巡视','自查/市公司']:
   x=r['excel'][label]
   if x['issue']:
    f.write('  Excel'+label+'问题：'+short(x['issue'])+'\n')
  for fld,label in [('leader','责任领导'),('respDept','责任部门'),('coordDept','配合部门'),('deadline','完成时限')]:
   ww=r['word'][fld]; vals=[(lab,r['excel'][lab][fld]) for lab in ['集团巡视','自查/市公司'] if r['excel'][lab][fld] is not None]
   if vals and not any(norm(ww)==norm(v) for _,v in vals): f.write(f"  {label} Word={short(ww,120)}；Excel="+' | '.join(f'{lab}:{short(v,120)}' for lab,v in vals)+'\n')
  # measure target lengths and first lines
  for fld,label in [('measure','整改措施/防范措施'),('target','整改目标/达成目标')]:
   ww=r['word'][fld]; vals=[(lab,r['excel'][lab][fld]) for lab in ['集团巡视','自查/市公司'] if r['excel'][lab][fld] is not None]
   scores=[sim(ww,v) for _,v in vals]
   if vals and max(scores)<0.98: f.write(f"  {label}差异（Word {len(str(ww or ''))}字；Excel="+' | '.join(f'{lab}{len(str(v))}字' for lab,v in vals)+f"；最高相似度{max(scores):.2f}）\n")
  if r['numbers']['word'] != r['numbers']['group'] and r['numbers']['word'] != r['numbers']['local']:
   f.write('  数字口径：Word='+','.join(r['numbers']['word'])+'；Excel集团='+','.join(r['numbers']['group'])+'；Excel自查='+','.join(r['numbers']['local'])+'\n')


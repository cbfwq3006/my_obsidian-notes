import json,re,difflib,collections
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
obj=json.load(open(r'E:\\sl_obsidian\\tmp_agg_compare.json',encoding='utf8'))
# obj summary indexed; use excel local fields as stored? summary picked source; need agg
agg=obj['agg']
def norm(s):
 s=str(s or '').replace('（自查不存在此问题）','').replace('(自查不存在此问题)','').replace('（集团巡视反馈）','')
 return re.sub(r'[\s\u200c\u200b]+','',s)
def sim(a,b): return difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()
for key,label in [('localMeasures','measure'),('localTargets','target'),('localDeadline','deadline')]:
 ex=[]
 for w in wr:
  x=agg[str(w['num'])]; wf=w['fields']; ww=(wf.get('整改措施') or wf.get('防范措施')) if label=='measure' else ((wf.get('整改目标') or wf.get('达成目标')) if label=='target' else wf.get('完成时限'))
  xx=x[key]
  ex.append(sim(ww,xx) if xx else 0)
 print(label,'exact',sum(norm((wr[i]['fields'].get('整改措施') or wr[i]['fields'].get('防范措施')) if label=='measure' else ((wr[i]['fields'].get('整改目标') or wr[i]['fields'].get('达成目标')) if label=='target' else wr[i]['fields'].get('完成时限'))) == norm(agg[str(wr[i]['num'])][key]) for i in range(len(wr))), '>=.95',sum(v>=.95 for v in ex),'avg',round(sum(ex)/len(ex),3),'low',[(i+1,round(v,2)) for i,v in enumerate(ex) if v<.8])
# deadlines local normalized conversion
print('Deadline differences local:')
for w in wr:
 x=agg[str(w['num'])]; wd=w['fields'].get('完成时限'); xd=x['localDeadline']
 # stringify excel serial convert month
 if isinstance(xd,(int,float)):
  from datetime import datetime,timedelta
  xd=(datetime(1899,12,30)+timedelta(days=xd)).strftime('%Y年%-m月')
 if norm(wd)!=norm(xd): print(w['num'],wd,'vs',xd)
# print local low records summary
for w in wr:
 x=agg[str(w['num'])]; wm=w['fields'].get('整改措施') or w['fields'].get('防范措施'); lm=x['localMeasures']; wt=w['fields'].get('整改目标') or w['fields'].get('达成目标'); lt=x['localTargets']
 sm,st=sim(wm,lm),sim(wt,lt)
 if sm<.8 or st<.8:
  print('LOW',w['num'],'measure',round(sm,2),'target',round(st,2),'Wlen',len(str(wm or '')),'Xlen',len(str(lm or '')))



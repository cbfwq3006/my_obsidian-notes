import json,re
obj=json.load(open(r'E:\\sl_obsidian\\tmp_agg_compare.json',encoding='utf8'))
for s in obj['summary']:
 x=s['excel']; w=s['word']
 # number lines in grouped/local measures
 def count(v): return len([z for z in str(v or '').splitlines() if z.strip()])
 print(s['no'], 'source',s['source'],'rows',s['rows'],'Wm',count(w['measure']),'Xm',count(x['measure']),'Wt',count(w['target']),'Xt',count(x['target']))

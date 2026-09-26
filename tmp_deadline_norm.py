import json,re,datetime
obj=json.load(open(r'E:\\sl_obsidian\\tmp_agg_compare.json',encoding='utf8'))
def conv(v):
 if v is None:return ''
 if isinstance(v,(int,float)):
  d=datetime.datetime(1899,12,30)+datetime.timedelta(days=v)
  return d.strftime('%Y年%-m月')
 return str(v)
for s in obj['summary']:
 w=s['word']; e=s['excel'];
 wd=conv(w['deadline']); ed=conv(e['deadline']);
 if wd!=ed:
  print(s['no'],s['source'],wd,'=>',ed)

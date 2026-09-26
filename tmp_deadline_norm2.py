import json,datetime
obj=json.load(open(r'E:\\sl_obsidian\\tmp_agg_compare.json',encoding='utf8'))
def conv(v):
 if v is None:return ''
 if isinstance(v,(int,float)):
  d=datetime.datetime(1899,12,30)+datetime.timedelta(days=v); return f'{d.year}年{d.month}月'
 return str(v)
def clean(v): return ' / '.join(conv(z) for z in str(v).split('\n'))
for s in obj['summary']:
 wd=clean(s['word']['deadline']); ed=clean(s['excel']['deadline'])
 if wd!=ed: print(s['no'],s['source'],wd,'=>',ed)

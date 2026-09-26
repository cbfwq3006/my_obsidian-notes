import json,datetime
# raw issue rows
raw=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_issues.json',encoding='utf8'))['rows']
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
def conv(v):
 if v is None:return ''
 if isinstance(v,(int,float)):
  d=datetime.datetime(1899,12,30)+datetime.timedelta(days=v); return f'{d.year}年{d.month}月'
 return str(v).replace('。','')
for w,x in zip(wr,raw):
 wd=conv(w['fields'].get('完成时限')); gd=conv(x['deadline']); ld=conv(x['selfDeadline'])
 # choose source based issue similarity manually from prior list? print if any
 if wd not in [gd,ld]: print(w['num'],wd,'group',gd,'local',ld)

import json,datetime
m=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_values.json',encoding='utf8'))['台账']['values']
starts=[]
for i in range(5,len(m)):
 if m[i][4] is not None and str(m[i][4]).strip(): starts.append((i,int(m[i][4])))
def conv(v):
 if v is None or str(v).strip()=='': return ''
 if isinstance(v,(int,float)):
  d=datetime.datetime(1899,12,30)+datetime.timedelta(days=v); return f'{d.year}年{d.month}月'
 return str(v)
for j,(st,no) in enumerate(starts):
 en=starts[j+1][0] if j+1<len(starts) else len(m)
 gd=[];ld=[]
 for r in m[st:en]:
  if r[15] is not None: gd.append(conv(r[15]))
  if r[27] is not None: ld.append(conv(r[27]))
 gu=sorted(set(gd)); lu=sorted(set(ld))
 if len(gu)>1 or len(lu)>1 or not lu:
  print(no,'group=',gu,'local=',lu,'rows',en-st)

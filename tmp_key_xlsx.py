import json,re
x=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_values.json',encoding='utf8'))['台账']['values']
# output key columns B-F,H-P,S-V,Y-AB for parent rows where col E has concrete issue, and all task rows grouped
for i,row in enumerate(x):
 def s(j):
  v=row[j] if j<len(row) else None
  return '' if v is None else str(v).replace('\n',' / ')
 if i<5: continue
 if any(row[j] is not None for j in [1,2,3,4,5,7,12,13,14,15]):
  vals={k:s(j) for k,j in [('B',1),('C',2),('D',3),('E',4),('F',5),('H',7),('I',8),('J',9),('K',10),('L',11),('M',12),('N',13),('O',14),('P',15),('S',18),('T',19),('U',20),('V',21),('Y',24),('Z',25),('AA',26),('AB',27)]}
  # only print rows with specific issue or task row M nonempty
  if vals['E'] or vals['M']:
   print('ROW',i+1, json.dumps(vals,ensure_ascii=False))

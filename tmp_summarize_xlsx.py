import json, re
x=json.load(open('E:\\sl_obsidian\\tmp_xlsx_values.json',encoding='utf8'))['台账']['values']
for i,row in enumerate(x):
 vals=[('' if v is None else str(v).replace('\n',' / ')) for v in row]
 # print rows where task or location relevant; all rows concise
 print(f'R{i+1}: '+' || '.join(f'{j+1}:{v[:260]}' for j,v in enumerate(vals) if v))

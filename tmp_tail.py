import json,re
x=json.load(open(r'E:\\sl_obsidian\\tmp_docx.json',encoding='utf8'))['paragraphs']
for p in x[-180:]: print(f"{p['i']}\t{p['text']}")

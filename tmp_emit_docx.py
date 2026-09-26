import json
x=json.load(open('E:\\sl_obsidian\\tmp_docx.json',encoding='utf8'))
with open('E:\\sl_obsidian\\tmp_docx_paras.tsv','w',encoding='utf8') as f:
 for p in x['paragraphs']:
  f.write(f"{p['i']}\t{p['text'].replace(chr(9),' ')}\n")

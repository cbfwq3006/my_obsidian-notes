import json,re
paras=json.load(open(r'E:\\sl_obsidian\\tmp_docx.json',encoding='utf8'))['paragraphs']
for p in paras:
 t=p['text'].strip()
 if re.match(r'^具体问题\d+：',t):
  m=re.match(r'^具体问题(\d+)：(.*)$',t)
  print(m.group(1)+'\t'+m.group(2))

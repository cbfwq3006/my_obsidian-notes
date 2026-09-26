import json,re,collections
x=json.load(open(r'E:\\sl_obsidian\\tmp_docx.json',encoding='utf8'))['paragraphs']
for p in x:
 t=p['text']
 if re.match(r'^(问题|具体问题)',t) or t.startswith('【责任') or t.startswith('【完成') or t.startswith('【整改') or t.startswith('【达成') or t.startswith('【防范'):
  print(p['i'], t[:300])

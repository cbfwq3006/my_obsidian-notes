import json,re
# parse word
paras=json.load(open(r'E:\\sl_obsidian\\tmp_docx.json',encoding='utf8'))['paragraphs']
wr=[]; cur=None
for p in paras:
 t=p['text'].strip()
 if re.match(r'^具体问题\d+：',t):
  if cur: wr.append(cur)
  m=re.match(r'^具体问题(\d+)：(.*)$',t); cur={'num':int(m.group(1)),'issue':m.group(2).strip(),'fields':{}}
 elif cur:
  m=re.match(r'^【([^】]+)】\s*(.*)$',t)
  if m: cur['fields'][m.group(1)]=m.group(2).strip()
  elif cur['fields'] and not re.match(r'^(问题|具体问题|一、|二、|三、|四、|五、)',t):
   k=list(cur['fields'])[-1]; cur['fields'][k]+='\n'+t
if cur: wr.append(cur)
json.dump(wr,open(r'E:\\sl_obsidian\\tmp_word_records.json','w',encoding='utf8'),ensure_ascii=False,indent=2)
# print key summary
for r in wr:
 f=r['fields']; ms=f.get('整改措施') or f.get('防范措施',''); tg=f.get('整改目标') or f.get('达成目标','')
 print(f"{r['num']}\t{r['issue']}\t领导={f.get('责任领导','')}\t责任={f.get('责任部门','')}\t配合={f.get('配合部门','')}\t措施={ms[:100].replace(chr(10),' / ')}\t目标={tg[:100].replace(chr(10),' / ')}\t时限={f.get('完成时限','')}")

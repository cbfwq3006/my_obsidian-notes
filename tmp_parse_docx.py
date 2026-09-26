import json,re
paras=json.load(open(r'E:\\sl_obsidian\\tmp_docx.json',encoding='utf8'))['paragraphs']
# parse records
records=[]; cur=None; section=''
for p in paras:
 t=p['text'].strip()
 if not t: continue
 if re.match(r'^具体问题\d+：',t):
  if cur: records.append(cur)
  m=re.match(r'^具体问题(\d+)：(.*)$',t)
  cur={'num':int(m.group(1)),'issue':m.group(2).strip(),'fields':{}}
 elif cur:
  m=re.match(r'^【([^】]+)】\s*(.*)$',t)
  if m:
   key=m.group(1); val=m.group(2).strip(); cur['fields'][key]=val
  else:
   # append to last field if current paragraph is continuation
   if cur['fields']:
    k=list(cur['fields'])[-1]
    # avoid section headings accidentally
    if not re.match(r'^(问题|具体问题|一、|二、|三、|四、|五、)',t): cur['fields'][k]+='\n'+t
if cur: records.append(cur)
print('records',len(records))
for r in records:
 print('\n#',r['num'],r['issue'])
 for k,v in r['fields'].items(): print(k,':',v[:500].replace('\n',' / '))

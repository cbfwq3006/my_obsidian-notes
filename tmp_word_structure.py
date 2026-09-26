import json,re,collections
p=json.load(open(r'E:\\sl_obsidian\\tmp_docx.json',encoding='utf8'))['paragraphs']
sections=[x['text'] for x in p if re.match(r'^[一二三四五六七八九十]+、',x['text'])]
print('sections',len(sections)); print('\n'.join(sections))
# count fields and paragraphs in Word
for key in ['责任领导','责任部门','配合部门','整改措施','防范措施','整改目标','达成目标','完成时限']:
 print(key,sum(1 for x in p if x['text'].startswith('【'+key+'】')))
print('specific',sum(1 for x in p if re.match(r'^具体问题\d+：',x['text'])))
# other headings maybe cover and no field

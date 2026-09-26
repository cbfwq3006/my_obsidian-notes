import json
obj=json.load(open(r'E:\\sl_obsidian\\tmp_agg_compare.json',encoding='utf8'))
for n in [1,2,3,4,5,7,8,9,13,19,21,22,23,26,28,29,30,32,34,35,36,37,39,40,41,42,44,45,46,47,48,49,50,51]:
 s=obj['summary'][n-1]
 print('\n###',n,'source',s['source'],'deadline',s['word']['deadline'],'=>',s['excel']['deadline'])
 for f in ['measure','target']:
  print(f+' WORD:',s['word'][f])
  print(f+' XLSX:',s['excel'][f])

import json
obj=json.load(open(r'E:\\sl_obsidian\\tmp_agg_compare.json',encoding='utf8'))
for n in [41,50,51]:
 s=obj['summary'][n-1]
 print('问题',n)
 print('Word目标:',repr(s['word']['target']))
 print('Excel目标:',repr(s['excel']['target']))
 print('Word措施:',repr(s['word']['measure']))
 print('Excel措施:',repr(s['excel']['measure']))

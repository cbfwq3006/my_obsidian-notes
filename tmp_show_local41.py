import json,re
obj=json.load(open(r'E:\\sl_obsidian\\tmp_agg_compare.json',encoding='utf8'))
for n in [41,50]:
 s=obj['summary'][n-1]; print('\n',n); print('word',s['word']); print('excel',s['excel'])

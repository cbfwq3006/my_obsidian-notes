import json
obj=json.load(open(r'E:\\sl_obsidian\\tmp_agg_compare.json',encoding='utf8'))
for n in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]:
 s=obj['summary'][n-1]
 w=s['word']; e=s['excel']
 # print only responsibility / deadlines / source; JSON to preserve
 print(json.dumps({'no':n,'source':s['source'],'word_leader':w['leader'],'excel_leader':e['leader'],'word_resp':w['resp'],'excel_resp':e['resp'],'word_coord':w['coord'],'excel_coord':e['coord'],'word_deadline':w['deadline'],'excel_deadline':e['deadline']},ensure_ascii=False))

import json
rows=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_local_issues.json',encoding='utf8'))
for x in rows:
 if x.get('localIssue'):
  print('NO',x['no'],'ROW',x['row'])
  for k in ['localIssue','localLeader','localLeadDept','localRespDept','localCoordDept','localCities','localMeasure','localTarget','localDeadline']:
   print(k,':',x.get(k))

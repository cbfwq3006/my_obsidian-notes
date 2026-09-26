import json,re,collections
x=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_values.json',encoding='utf8'))['台账']['values']
# Use rows 5 onwards; group records based on col E start, aggregate task rows M and self Y
starts=[]
for i in range(5,len(x)):
 if x[i][4] is not None and str(x[i][4]).strip(): starts.append(i)
print('issue starts',len(starts))
# count task entries M and Y across all rows
print('group measures rows',sum(1 for r in x[5:] if r[12] is not None and str(r[12]).strip()))
print('local measures rows',sum(1 for r in x[5:] if r[24] is not None and str(r[24]).strip()))
# records that have empty measures targets etc
for i in starts:
 r=x[i]
 print(r[4], 'group deadline',r[15], 'local deadline',r[27], 'hasGroup',bool(r[13]),'hasLocal',bool(r[25]))

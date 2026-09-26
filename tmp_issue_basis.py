import json,re,difflib,collections
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
# use aggregate from json; keys strings
agg=json.load(open(r'E:\\sl_obsidian\\tmp_agg_compare.json',encoding='utf8'))['agg']
def norm(s):
 s=str(s or '').replace('（自查不存在此问题）','').replace('(自查不存在此问题)','').replace('（集团巡视反馈）','')
 return re.sub(r'[\s\u200c\u200b]+','',s).replace('“','').replace('”','').replace('，',',').replace('。','.')
for mode in ['exact','sim']:
 c=collections.Counter(); arr=[]
 for w in wr:
  x=agg[str(w['num'])]; a=norm(w['issue']); g=norm(x['groupIssue']); l=norm(x['selfIssue']);
  if mode=='exact':
   if a==g and a==l: label='both'
   elif a==g: label='group'
   elif a==l: label='local'
   else: label='modified'
  else:
   gs=difflib.SequenceMatcher(None,a,g).ratio(); ls=difflib.SequenceMatcher(None,a,l).ratio() if l else 0
   label='group' if gs>=ls else 'local'; arr.append((w['num'],gs,ls,label))
  c[label]+=1
 print(mode,c)
if mode=='sim': print(arr)
# print exact mismatches and source texts concise (safe utf8 file)
with open(r'E:\\sl_obsidian\\tmp_issue_basis.txt','w',encoding='utf8') as f:
 for w in wr:
  x=agg[str(w['num'])]; a=norm(w['issue']); g=norm(x['groupIssue']); l=norm(x['selfIssue']);
  if a==g and a==l: b='两者'
  elif a==g: b='集团巡视'
  elif a==l: b='自查/市公司'
  else: b='改写/压缩'
  f.write(f"{w['num']}\t{b}\tWord：{w['issue']}\n集团：{x['groupIssue']}\n自查：{x['selfIssue']}\n\n")

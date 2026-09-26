import json,re
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
# read xlsx json generated
xr=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_issues.json',encoding='utf8'))['rows']
# normalize text
norm=lambda s: re.sub(r'\s+','',str(s or '').replace('（自查不存在此问题）','').replace('(自查不存在此问题)','').replace('（集团巡视反馈）',''))
# direct issue number mapping
for w,x in zip(wr,xr):
 # compare issue text similarity via common chars/sequence
 a=norm(w['issue']); b=norm(x['issue'])
 # SequenceMatcher
 import difflib
 ratio=difflib.SequenceMatcher(None,a,b).ratio()
 print(f"{w['num']}\t{ratio:.3f}\tW:{w['issue'][:70]}\tX:{x['issue'][:70]}")

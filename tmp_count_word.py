import json,re
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
# Count numbered lines in measures and targets
for r in wr:
 f=r['fields']; m=f.get('整改措施') or f.get('防范措施',''); t=f.get('整改目标') or f.get('达成目标','')
 # line starts numbering incl subitems
 ml=[ln for ln in m.splitlines() if re.match(r'^\s*(?:\d+\.|（\d+）|\(\d+\))',ln)]
 tl=[ln for ln in t.splitlines() if re.match(r'^\s*(?:\d+\.|（\d+）|\(\d+\))',ln)]
 print(r['num'],len(ml),len(tl))

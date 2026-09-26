import json,re
wr=json.load(open(r'E:\\sl_obsidian\\tmp_word_records.json',encoding='utf8'))
def count(s):
 return len([ln for ln in str(s or '').splitlines() if ln.strip() and re.match(r'^\s*(?:\d+\.|（\d+）|\(\d+\))',ln)])
print('word measure',sum(count((r['fields'].get('整改措施') or r['fields'].get('防范措施',''))) for r in wr))
print('word targets',sum(count((r['fields'].get('整改目标') or r['fields'].get('达成目标',''))) for r in wr))
print('word records',len(wr))

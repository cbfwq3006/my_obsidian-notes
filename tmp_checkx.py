import json
x=json.load(open(r'E:\\sl_obsidian\\tmp_xlsx_issues.json',encoding='utf8'))['rows'][0]
print(x.keys()); print(x)

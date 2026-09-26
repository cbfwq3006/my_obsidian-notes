import json
x=json.load(open('E:\\sl_obsidian\\tmp_docx.json',encoding='utf8'))
print('PARAGRAPHS',len(x['paragraphs']),'TABLES',len(x['tables']))
for p in x['paragraphs']:
 print(f"P{p['i']} [{p['style']}] {p['text']}")
for t in x['tables']:
 print('\nTABLE',t['i'],t['nrows'],t['ncols'])
 for ri,row in enumerate(t['rows'][:8]):
  print('R',ri,' || '.join(c['text'].replace('\n',' / ')[:300] for c in row))

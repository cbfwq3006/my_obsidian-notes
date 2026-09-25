import zipfile,re,html,sys
p=sys.argv[1]
with zipfile.ZipFile(p) as z:
 s=z.read('xl/sharedStrings.xml').decode('utf-8','ignore'); shared=[]
 for si in re.findall(r'<si.*?</si>',s,re.S): shared.append(html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',si,re.S))))
 s=z.read('xl/worksheets/sheet1.xml').decode('utf-8','ignore')
 out=[]
 for row in re.findall(r'<row[^>]*>.*?</row>',s,re.S):
  vals=[]
  for c in re.findall(r'<c[^>]*?(?:/>|>.*?</c>)',row,re.S):
   ref=re.search(r'r="([A-Z]+\d+)"',c); v=re.search(r'<v>(.*?)</v>',c,re.S); typ=re.search(r' t="([^"]+)"',c)
   if not ref or not v: continue
   try: val=shared[int(v.group(1))] if typ and typ.group(1)=='s' else v.group(1)
   except: val=v.group(1)
   vals.append((ref.group(1),val))
  if vals: out.append('ROW '+vals[0][0][1:]+'\t'+'\t'.join(f'{a}={b}' for a,b in vals))
open(r'E:\sl_obsidian\.tmp_old_utf8.txt','w',encoding='utf-8').write('\n'.join(out))
print('rows',len(out))

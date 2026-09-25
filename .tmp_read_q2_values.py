import zipfile,re,html,sys
p=sys.argv[1]
with zipfile.ZipFile(p) as z:
 shared=[]
 try:
  s=z.read('xl/sharedStrings.xml').decode('utf-8','ignore')
  for si in re.findall(r'<si.*?</si>',s,re.S):
   shared.append(html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',si,re.S))))
 except: pass
 print('shared',len(shared))
 s=z.read('xl/worksheets/sheet1.xml').decode('utf-8','ignore')
 for row in re.findall(r'<row[^>]*>.*?</row>',s,re.S):
  vals=[]
  for c in re.findall(r'<c[^>]*?(?:/>|>.*?</c>)',row,re.S):
   ref=re.search(r'r="([A-Z]+\d+)"',c)
   if not ref: continue
   typ=re.search(r' t="([^"]+)"',c)
   v=re.search(r'<v>(.*?)</v>',c,re.S)
   val=''
   if typ and typ.group(1)=='s' and v:
    try: val=shared[int(v.group(1))]
    except: val=v.group(1)
   elif typ and typ.group(1)=='inlineStr':
    val=html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',c,re.S)))
   elif v: val=html.unescape(v.group(1))
   if val!='': vals.append(f'{ref.group(1)}={val}')
  if vals: print(' | '.join(vals))

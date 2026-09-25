import zipfile,re,html,sys
p=sys.argv[1]
with zipfile.ZipFile(p) as z:
  for n in z.namelist():
    if n.endswith('.xml'):
      try:s=z.read(n).decode('utf-8','ignore')
      except:continue
      if 'sheetData' not in s: continue
      print('===',n,'===')
      # print row xml with values and refs compact
      ss=re.search(r'<sheetData.*?</sheetData>',s,re.S)
      if not ss: continue
      for row in re.findall(r'<row[^>]*>.*?</row>',ss.group(),re.S):
       vals=[]
       for c in re.findall(r'<c[^>]*?(?:/>|>.*?</c>)',row,re.S):
        ref=re.search(r'r="([A-Z]+\d+)"',c)
        v=re.search(r'<v>(.*?)</v>',c,re.S)
        t=re.search(r'<t[^>]*>(.*?)</t>',c,re.S)
        if ref:
         val=html.unescape(t.group(1) if t else (v.group(1) if v else ''))
         vals.append(f'{ref.group(1)}={val}')
       if vals: print(' | '.join(vals))

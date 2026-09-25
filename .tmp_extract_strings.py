import zipfile, os, re
from pathlib import Path
files=[Path(r'E:\sl_obsidian\outputs\20260901_8月工作总结及9月工作计划\8月工作总结及9月工作计划.xlsx'),Path(r'D:\work\2026\9\3 巡察整改报告\集团党组巡视河南整改台账-焦作市分公司0910.xlsx'),Path(r'D:\work\2026\9\3 王统主任安排工作\台账9月20日前完成\中央巡视整改问题台账（汇总）0918.xlsx'),Path(r'D:\work\2026\9\3 王统主任安排工作\台账9月20日前完成\2025年第一批集团党组巡视整改现场检查评估发现共性问题自查自纠整改台账-焦作公司0918.xlsx')]
for p in files:
 print('\n===',p,'===')
 with zipfile.ZipFile(p) as z:
  ss=[]
  for n in z.namelist():
   if n.endswith('.xml'):
    try:ss.append(z.read(n).decode('utf-8','ignore'))
    except:pass
  s='\n'.join(ss)
  strings=re.findall(r'<t[^>]*>(.*?)</t>',s)
  # unescape entities
  import html
  strings=[html.unescape(re.sub('<[^>]+>','',x)) for x in strings]
  for i,x in enumerate(strings):
   if x.strip(): print(i,repr(x[:500]))

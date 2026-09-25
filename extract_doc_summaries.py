from docx import Document
from pathlib import Path
import re,json
root=Path(r'D:\work\2026\9\3 王统主任安排工作\自查报告（7项）')
for p in sorted(root.glob('*.docx')):
 d=Document(str(p)); txt='\n'.join(x.text.strip() for x in d.paragraphs if x.text.strip())
 print('\n===',p.name,'===')
 for line in txt.splitlines():
  if re.search(r'完成|形成|建立|制定|报送|整改|台账|报告|截至|已',line): print(line[:500])

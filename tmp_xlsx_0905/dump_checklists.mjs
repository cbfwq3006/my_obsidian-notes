import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
import fs from 'node:fs/promises';
const root='D:/work/2026/9/1 集团党组巡视河南整改台账-焦作市分公司/7项自查表(1)';
const files=['1附件：巡视整改自查问题清单（一岗双责）.xlsx','2附件：巡视整改自查问题清单（基层党建考核作用未发挥问题）.xlsx','3附件：巡视整改自查问题清单（基层党员先锋模范作用发挥不够问题进行专项自查).xlsx','4附件：巡视整改自查问题清单-基层党组织生活不规范问题自查.xlsx','5附件：巡视整改自查问题清单（学习贯彻习近平新时代中国特色社会主义思想）.xlsx','6附件：巡视整改自查问题清单（意识形态）.xlsx','7附件：巡视整改自查问题清单（全面从严治党）.xlsx'];
const out={};
for(const f of files){
 const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(root+'/'+f));
 const ss=[];
 for(const s of wb.worksheets.items){
  const u=s.getUsedRange(); ss.push({name:s.name,address:u?.address||null,values:u?.values||[]});
 }
 out[f]=ss;
}
await fs.writeFile('E:/sl_obsidian/tmp_xlsx_0905/checklists.json',JSON.stringify(out,null,2),'utf8');
for(const [f,ss] of Object.entries(out)) console.log(f,ss.map(x=>`${x.name}:${x.address}:${x.values.length}x${x.values[0]?.length||0}`).join('; '));

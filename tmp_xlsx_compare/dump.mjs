import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
import fs from 'node:fs/promises';
const p = String.raw`D:\work\2026\9\4 集团党组巡视河南整改任务\附件2-集团党组巡视河南整改台账-焦作市分公司0924.xlsx`;
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(p));
const out={};
for (const sh of wb.worksheets.items) {
 const ur=sh.getUsedRange();
 out[sh.name]={address:ur.address,values:ur.values,formulas:ur.formulas};
}
await fs.writeFile('E:\\sl_obsidian\\tmp_xlsx_values.json',JSON.stringify(out,null,2),'utf8');
console.log(Object.fromEntries(Object.entries(out).map(([k,v])=>[k,{address:v.address,rows:v.values?.length,cols:v.values?.[0]?.length}])));

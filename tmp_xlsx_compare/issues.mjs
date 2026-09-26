import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
import fs from 'node:fs/promises';
const p = String.raw`D:\work\2026\9\4 集团党组巡视河南整改任务\附件2-集团党组巡视河南整改台账-焦作市分公司0924.xlsx`;
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(p));
const sh=wb.worksheets.getItem('台账');
const vals=sh.getUsedRange().values;
const headers=vals[4];
const rows=[];
for(let i=5;i<vals.length;i++){
 const r=vals[i];
 if(r[4]!=null && String(r[4]).trim()!==''){
  rows.push({excelRow:i+1,issueNo:r[4],issue:r[5],leader:r[7],leadDept:r[8],respDept:r[9],coordDept:r[10],cities:r[11],measureNo:r[12],measure:r[13],target:r[14],deadline:r[15],selfIssue:r[17],selfLeader:r[19],selfLeadDept:r[20],selfRespDept:r[21],selfCoordDept:r[22],selfMeasureNo:r[24],selfMeasure:r[25],selfTarget:r[26],selfDeadline:r[27]});
 }
}
await fs.writeFile('E:\\sl_obsidian\\tmp_xlsx_issues.json',JSON.stringify({headers,rows},null,2),'utf8');
console.log('issues',rows.length); console.log(rows.map(x=>({no:x.issueNo,row:x.excelRow,deadline:x.deadline,issue:(x.issue||'').slice(0,50)})));

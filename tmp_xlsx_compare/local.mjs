import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
import fs from 'node:fs/promises';
const p=String.raw`D:\work\2026\9\4 集团党组巡视河南整改任务\附件2-集团党组巡视河南整改台账-焦作市分公司0924.xlsx`;
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p)); const sh=wb.worksheets.getItem('台账'); const vals=sh.getUsedRange().values;
const rows=[];
for(let i=5;i<vals.length;i++){const r=vals[i]; if(r[4]!=null&&String(r[4]).trim()!=='') rows.push({no:r[4],row:i+1,groupIssue:r[5],groupLeader:r[7],groupLeadDept:r[8],groupRespDept:r[9],groupCoordDept:r[10],groupCities:r[11],groupMeasure:r[13],groupTarget:r[14],groupDeadline:r[15],localIssue:r[17],localLeader:r[19],localLeadDept:r[20],localRespDept:r[21],localCoordDept:r[22],localCities:r[23],localMeasure:r[25],localTarget:r[26],localDeadline:r[27]});}
await fs.writeFile('E:\\sl_obsidian\\tmp_xlsx_local_issues.json',JSON.stringify(rows,null,2),'utf8');

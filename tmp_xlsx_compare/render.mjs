import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
import fs from 'node:fs/promises';
const p=String.raw`D:\work\2026\9\4 集团党组巡视河南整改任务\附件2-集团党组巡视河南整改台账-焦作市分公司0924.xlsx`;
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));
const sh=wb.worksheets.getItem('台账');
const blob=await wb.render({sheetName:'台账',range:'A1:AB35',scale:1,format:'png'});
await fs.writeFile('E:\\sl_obsidian\\tmp_xlsx_preview.png',new Uint8Array(await blob.arrayBuffer()));
console.log('done');

import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
import fs from 'node:fs/promises';
const src='D:/work/2026/9/工作周报_20260831-0906.xlsx';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(src));
console.log((await wb.inspect({kind:'workbook,sheet,table',maxChars:10000,tableMaxRows:15,tableMaxCols:12,tableMaxCellChars:200})).ndjson);
for(const s of wb.worksheets.items){
  console.log('SHEET',s.name);
  console.log((await wb.inspect({kind:'region',sheetId:s.name,range:'A1:J20',maxChars:10000})).ndjson);
  const p=await wb.render({sheetName:s.name,range:'A1:J20',scale:1.5,format:'png'});
  await fs.writeFile('E:/sl_obsidian/.tmp_weekreport/template_'+s.name+'.png',new Uint8Array(await p.arrayBuffer()));
}

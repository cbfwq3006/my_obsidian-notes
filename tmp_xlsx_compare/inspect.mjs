import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const p = String.raw`D:\work\2026\9\4 集团党组巡视河南整改任务\附件2-集团党组巡视河南整改台账-焦作市分公司0924.xlsx`;
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(p));
const a = await wb.inspect({kind:'workbook,sheet,table',maxChars:20000,tableMaxRows:12,tableMaxCols:20,tableMaxCellChars:120});
console.log(a.ndjson);

import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('D:/work/2026/9/工作周报_20260831-0906_更新版.xlsx'));
console.log((await wb.inspect({kind:'region',sheetId:'Sheet1',range:'A1:J12',maxChars:20000})).ndjson);

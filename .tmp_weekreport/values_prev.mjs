import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('D:/work/2026/9/工作周报_20260831-0906_更新版.xlsx'));
const s=wb.worksheets.getItem('Sheet1');
console.log(JSON.stringify(s.getRange('A1:J12').values));

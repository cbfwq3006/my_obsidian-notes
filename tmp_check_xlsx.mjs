import {FileBlob, SpreadsheetFile} from "@oai/artifact-tool";
const p=process.argv[2]; const input=await FileBlob.load(p); const wb=await SpreadsheetFile.importXlsx(input);
console.log((await wb.inspect({kind:"workbook,sheet,table",maxChars:20000,tableMaxRows:10,tableMaxCols:20,tableMaxCellChars:120})).ndjson);
for(const s of wb.worksheets.items){console.log('SHEET',s.name); console.log((await wb.inspect({kind:'region',sheetId:s.name,range:'A1:Z80',maxChars:30000,tableMaxRows:80,tableMaxCols:26,tableMaxCellChars:200})).ndjson)}

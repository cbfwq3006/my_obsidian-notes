import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const p=process.argv[2]; const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));
console.log((await wb.inspect({kind:'workbook,sheet,table',maxChars:5000,tableMaxRows:5,tableMaxCols:12,tableMaxCellChars:100})).ndjson);
for(const term of ['党建工作部','第一议题','巡视整改','组织生活','先锋模范','意识形态','一岗双责']) console.log(term,(await wb.inspect({kind:'match',searchTerm:term,options:{maxResults:50},maxChars:12000})).ndjson);

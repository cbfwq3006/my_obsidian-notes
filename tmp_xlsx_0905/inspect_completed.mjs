import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('D:/work/2026/9/1 集团党组巡视河南整改台账-焦作市分公司/集团党组巡视河南整改台账-焦作市分公司_已填写.xlsx'));
const s=wb.worksheets.getItem('台账');
const original=await SpreadsheetFile.importXlsx(await FileBlob.load('D:/work/2026/9/1 集团党组巡视河南整改台账-焦作市分公司/集团党组巡视河南整改台账-焦作市分公司.xlsx'));
const os=original.worksheets.getItem('台账');
for (const row of [6,11]) {
  const n=os.getRange(`N${row}`).values[0][0] || '';
  const z=s.getRange(`Z${row}`).values[0][0] || '';
  const aa=s.getRange(`AA${row}`).values[0][0] || '';
  console.log(`LENGTH row ${row}: N=${n.length}, Z=${z.length}, AA=${aa.length}`);
}
for(const r of ['Z6','AA6','Z11','AA11','Z6:AA15']) console.log(r,(await wb.inspect({kind:'computedStyle',sheetId:'台账',range:r,maxChars:3000})).ndjson);
console.log((await wb.inspect({kind:'table',sheetId:'台账',range:'Q4:AB15',include:'values,formulas',tableMaxRows:20,tableMaxCols:20,tableMaxCellChars:300})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A',options:{useRegex:true,maxResults:100},summary:'formula errors'})).ndjson);

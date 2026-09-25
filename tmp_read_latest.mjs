import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
for(const p of process.argv.slice(2)){
 console.log('\nFILE',p); try{const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p)); console.log((await wb.inspect({kind:'workbook,sheet,table',maxChars:6000,tableMaxRows:6,tableMaxCols:15,tableMaxCellChars:100})).ndjson); for(const s of wb.worksheets.items){for(const term of ['党建工作部','已完成','整改完成','整改措施','完成情况','巡视']){const x=await wb.inspect({kind:'match',sheetId:s.name,searchTerm:term,options:{maxResults:30},maxChars:7000}); if(x.ndjson.trim()) console.log(s.name,term,x.ndjson)}}}catch(e){console.log('ERR',e.message)}
}

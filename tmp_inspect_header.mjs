import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const p='D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p)); const s=wb.worksheets.getItem('Sheet1');
console.log('A1:S8', (await wb.inspect({kind:'region',sheetId:'Sheet1',range:'A1:S8',maxChars:20000,tableMaxRows:10,tableMaxCols:20,tableMaxCellChars:200})).ndjson);
console.log('all merged?', (await wb.inspect({kind:'region',sheetId:'Sheet1',range:'A1:S57',maxChars:1000})).ndjson);
for(const a of ['P1','Q1','R1','S1','P51','Q51','R51','S51','P55','Q55','R55','S55']){console.log(a,JSON.stringify(s.getRange(a).values),JSON.stringify(s.getRange(a).format));}

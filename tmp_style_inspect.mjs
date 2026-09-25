import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const p='D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));
console.log('style headers', (await wb.inspect({kind:'computedStyle',sheetId:'Sheet1',range:'R1:S5',maxChars:12000})).ndjson);
console.log('style rows', (await wb.inspect({kind:'computedStyle',sheetId:'Sheet1',range:'R51:S55',maxChars:20000})).ndjson);
console.log('region', (await wb.inspect({kind:'region',sheetId:'Sheet1',range:'P48:S57',maxChars:12000,tableMaxRows:20,tableMaxCols:10,tableMaxCellChars:100})).ndjson);

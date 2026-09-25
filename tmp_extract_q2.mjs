import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load("D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx"));const s=wb.worksheets.getItem('Sheet1');
for(const row of [51,55]){const a=s.getRange(`A${row}:S${row}`).values[0]; for(let i=0;i<a.length;i++){console.log(`${String.fromCharCode(65+i)}${row}\t${a[i]??''}`)}}

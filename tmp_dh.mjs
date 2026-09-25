import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const p='D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));const s=wb.worksheets.getItem('Sheet1');
for(const r of [51,52,53,54,55]) { const v=s.getRange(`D${r}:H${r}`).values[0]; console.log(r,JSON.stringify(v)); }

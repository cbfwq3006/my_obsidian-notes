import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load("D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx"));
const s=wb.worksheets.getItem('Sheet1');
for(const row of [51,52,53,54,55]){console.log('ROW',row); const r=s.getRange(`A${row}:S${row}`); console.log(JSON.stringify(r.values)); console.log('formulas',JSON.stringify(r.formulas));}

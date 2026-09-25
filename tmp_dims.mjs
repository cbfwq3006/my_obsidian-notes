import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx'));const s=wb.worksheets.getItem('Sheet1');
for(const c of ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S']){const rg=s.getRange(`${c}1`); console.log(c,'width',rg.format.columnWidth,'widthPx',rg.format.columnWidthPx);}
for(const r of [1,2,50,51,52,55,56,57]){console.log('row',r,'height',s.getRange(`A${r}`).format.rowHeight,'heightPx',s.getRange(`A${r}`).format.rowHeightPx);}

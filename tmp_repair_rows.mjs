import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const p='E:/sl_obsidian/outputs/20260923_推动落实情况更新/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务完成情况-截至20260923.xlsx';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));const s=wb.worksheets.getItem('Sheet1');
const origD=['付刚','王志','王志','王志','付刚'];
const origH=['党建工作部（党委宣传部、党委统战部）/工会','人力资源部','党建工作部/工会','党建工作部/工会','党建工作部（党委宣传部、党委统战部）/工会'];
s.getRange('D51:D55').values=origD.map(x=>[x]); s.getRange('H51:H55').values=origH.map(x=>[x]);
const out=await SpreadsheetFile.exportXlsx(wb);await out.save(p);console.log('repaired');

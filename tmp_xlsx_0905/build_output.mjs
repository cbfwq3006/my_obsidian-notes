import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
import fs from 'node:fs/promises';

const inputPath = 'D:/work/2026/9/1 集团党组巡视河南整改台账-焦作市分公司/集团党组巡视河南整改台账-焦作市分公司.xlsx';
const outputPath = 'D:/work/2026/9/1 集团党组巡视河南整改台账-焦作市分公司/集团党组巡视河南整改台账-焦作市分公司_已填写.xlsx';
const previewPath = 'E:/sl_obsidian/tmp_xlsx_0905/completed.png';

const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(inputPath));
const sheet = wb.worksheets.getItem('台账');

// The existing city-company entries are anchored at rows 6 and 11; preserve all other cells and formatting.
sheet.getRange('Z6').values = [[
  '严格执行“第一议题”制度，建立议题来源审核、会前复核和记录归档机制，定期自查纠偏。'
]];
sheet.getRange('AA6').values = [[
  '完成“第一议题”制度执行情况自查，建立党委会学习内容审核和常态化督导机制，防止不符合要求的内容纳入“第一议题”。'
]];
sheet.getRange('Z11').values = [[
  '聚焦重点内容制定学习计划，深化研讨并结合一线调研，党建工作部跟踪复核。'
]];
sheet.getRange('AA11').values = [[
  '完成中心组学习自查整改，补齐规定内容，深化研讨并推动理论学习与一线调研、实际问题解决相结合。'
]];

// Keep the existing table style while making the newly entered text readable.
sheet.getRange('Z6:Z10').format.wrapText = true;
sheet.getRange('AA6:AA10').format.wrapText = true;
sheet.getRange('Z11:Z15').format.wrapText = true;
sheet.getRange('AA11:AA15').format.wrapText = true;
sheet.getRange('A6:AB6').format.rowHeight = 52;
sheet.getRange('A11:AB11').format.rowHeight = 72;

await fs.mkdir('E:/sl_obsidian/tmp_xlsx_0905', {recursive:true});
const preview = await wb.render({sheetName:'台账', range:'Q4:AB18', scale:2, format:'png'});
await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));
const out = await SpreadsheetFile.exportXlsx(wb);
await out.save(outputPath);
console.log(JSON.stringify({outputPath, previewPath, z6:sheet.getRange('Z6').values, aa6:sheet.getRange('AA6').values, z11:sheet.getRange('Z11').values, aa11:sheet.getRange('AA11').values}));

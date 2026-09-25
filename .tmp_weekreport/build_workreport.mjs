import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';

const src = 'D:/work/2026/9/工作周报_20260831-0906.xlsx';
const outDir = 'D:/work/2026/9';
const out = `${outDir}/工作周报_20260907-0913_更新版.xlsx`;
const previewPath = 'E:/sl_obsidian/.tmp_weekreport/workreport_20260907-0913.png';

const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(src));
const sheet = wb.worksheets.getItem('Sheet1');

// Clear prior period's editable content while preserving the template's formatting and merges.
sheet.getRange('C4:C7').clear({ applyTo: 'contents' });
sheet.getRange('C9:C12').clear({ applyTo: 'contents' });
sheet.getRange('H4:I7').clear({ applyTo: 'contents' });
sheet.getRange('H9:I12').clear({ applyTo: 'contents' });
sheet.getRange('J4:J7').clear({ applyTo: 'contents' });
sheet.getRange('J9:J12').clear({ applyTo: 'contents' });

sheet.getRange('C2').values = [['2026/9/7-2026/9/13']];

sheet.getRange('C4:C7').values = [
  ['党委层面：\n1.报送消费帮扶情况统计表；\n2.帮扶资金拨付已部分完成；\n3.完成三季度省公司集中研讨列席工作；\n4.下发消费帮扶“兴农周”本地化文件；\n5.推进集团党组巡视整改落实方案及整改台账，开展党内法规执行情况自查整改材料梳理。'],
  ['支部层面：\n1.收集各支部集中研讨时间，与评估组沟通列席工作事宜；\n2.审核各支部三季度党课；\n3.完成党员组织关系转接；\n4.组织参加省公司深化“五星”支部创建工作推进会；\n5.跟进9月主题党日学习安排，督促各支部将焦作市第十三次党代会精神纳入学习。'],
  [''],
  [''],
];
sheet.getRange('J4:J7').values = [
  ['郑苗、祝文娟'],
  ['郑苗、祝文娟'],
  [''],
  [''],
];

sheet.getRange('C9:C12').values = [
  ['党委层面：\n1.报送消费帮扶活动总结表；\n2.组织兴农周展销活动；\n3.消费帮扶合同签订；\n4.按9月15日节点完成整改报告报送；\n5.推进党内法规执行情况专项整改，9月18日前报送排查整改情况，做好10月31日前专项整改报告准备。'],
  ['支部层面：\n1.盯市公司三季度集中研讨列席工作；\n2.跟进各支部9月主题党日落实及平台录入，纳入焦作市第十三次党代会精神学习；\n3.跟进党员先锋岗水晶牌制作及照片收集后续工作。'],
  [''],
  [''],
];
sheet.getRange('J9:J12').values = [
  ['郑苗、祝文娟'],
  ['郑苗、祝文娟'],
  [''],
  [''],
];

// Keep text readable in the template's wrapped content cells.
sheet.getRange('C4:C7').format.wrapText = true;
sheet.getRange('C9:C12').format.wrapText = true;
sheet.getRange('H4:I7').format.wrapText = true;
sheet.getRange('H9:I12').format.wrapText = true;
sheet.getRange('J4:J7').format.wrapText = true;
sheet.getRange('J9:J12').format.wrapText = true;

await fs.mkdir(outDir, { recursive: true });
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(out);
const preview = await wb.render({ sheetName: 'Sheet1', range: 'A1:J12', scale: 1.5, format: 'png' });
await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));

console.log(JSON.stringify({out, previewPath}));
console.log((await wb.inspect({ kind: 'table', range: 'Sheet1!A1:J12', include: 'values,formulas', tableMaxRows: 12, tableMaxCols: 10, maxChars: 16000 })).ndjson);
console.log((await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A', options: { useRegex: true, maxResults: 100 }, summary: 'final formula error scan' })).ndjson);



import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const input = "D:/work/2026/9/工作周报_20260914-0920.xlsx";
const output = "D:/work/2026/9/工作周报_20260914-0920_更新版.xlsx";
const preview = "E:/sl_obsidian/.tmp_weekly_report_20260918/preview_updated.png";

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(input));
const sheet = workbook.worksheets.getItemAt(0);

sheet.getRange("C4:G4").values = [[
  "党委层面：\n" +
  "1.完成第一议题6项学习及理论学习中心组研讨发言\n" +
  "2.完成集团党组巡视整改落实方案及整改台账报送\n" +
  "3.汇总完善巡视整改专项自查报告7项及3项整改台账\n" +
  "4.整理支部更名及部分支部书记调整上会材料\n" +
  "5.完成地市网格单元党员基本情况统计表填报"
, null, null, null, null]];
sheet.getRange("J4").values = [["李兵、王统、申琳、郑苗"]];

sheet.getRange("C5:G5").values = [[
  "支部层面：\n" +
  "1.完成基层党建考核、党员先锋模范作用、基层党组织生活不规范等专项自查整改报告\n" +
  "2.审核王文龙发展对象相关材料，持续推进李佳鹏、和安宁接收预备党员工作\n" +
  "3.完成党员先锋岗水晶牌照片汇总并对接制作\n" +
  "4.收集审核各支部三季度党课材料\n" +
  "5.跟进市公司三季度集中研讨列席工作"
, null, null, null, null]];
sheet.getRange("J5").values = [["郑苗、祝文娟"]];

sheet.getRange("C6:G6").values = [[
  "宣传及其他：\n" +
  "1.报送省公司综述稿件1篇，编审稿件10篇\n" +
  "2.报送意识形态整改报告\n" +
  "3.报送消费帮扶活动总结表，组织兴农周展销活动，完成消费帮扶合同签订\n" +
  "4.报送8月份绩效材料\n" +
  "5.完善2026年本地党建考核方案及相关考核要点"
, null, null, null, null]];
sheet.getRange("J6").values = [["申琳、郑苗、祝文娟"]];

sheet.getRange("C9:I9").values = [[
  "党委层面：\n" +
  "1.跟进巡视整改专项报告报送及整改台账后续落实\n" +
  "2.准备党委第一议题和理论学习中心组学习材料\n" +
  "3.持续完善党建考核方案并做好上会准备\n" +
  "4.审核补选党委委员、补选党代表工作形成的支委会和党员大会记录"
, null, null, null, null, null, null]];
sheet.getRange("J9").values = [["李兵、王统、郑苗"]];

sheet.getRange("C10:I10").values = [[
  "支部层面：\n" +
  "1.推进李佳鹏、和安宁接收预备党员及有关材料归档\n" +
  "2.跟进党员先锋岗水晶牌制作发放\n" +
  "3.督促各支部完成“三会一课”、9月主题党日、三季度党课及集中研讨材料归档\n" +
  "4.对系列内更名支部进行修改\n" +
  "5.做好专兼职党务工作者履职资料月底上传"
, null, null, null, null, null, null]];
sheet.getRange("J10").values = [["郑苗、祝文娟、申琳"]];

sheet.getRange("C11:I11").values = [[
  "其他：\n" +
  "1.报送兴农周情况报告\n" +
  "2.完成消费帮扶合同盖章并邮寄至支付公司，做好帮扶产品到货发放\n" +
  "3.报送征集素材、党建工作动态及省公司组图1个\n" +
  "4.完成红色教育基地复核填报"
, null, null, null, null, null, null]];
sheet.getRange("J11").values = [["郑苗、申琳"]];

const heights = {4: 112, 5: 126, 6: 118, 9: 100, 10: 118, 11: 105};
for (const [r, h] of Object.entries(heights)) sheet.getRange(`A${r}:J${r}`).format.rowHeight = h;

const check = await workbook.inspect({kind: "table", range: "Sheet1!A1:J12", include: "values,formulas", tableMaxRows: 12, tableMaxCols: 10, maxChars: 16000});
console.log(check.ndjson);
const errors = await workbook.inspect({kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: {useRegex: true, maxResults: 100}, summary: "final formula error scan", maxChars: 3000});
console.log(errors.ndjson);

const image = await workbook.render({sheetName: "Sheet1", range: "A1:J12", scale: 1.3, format: "png"});
await fs.writeFile(preview, new Uint8Array(await image.arrayBuffer()));
const out = await SpreadsheetFile.exportXlsx(workbook);
await out.save(output);
console.log(JSON.stringify({output, preview}));

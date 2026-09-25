import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const input = "D:/work/2026/9/工作周报_20260907-0913_更新版.xlsx";
const output = "D:/work/2026/9/工作周报_20260914-0920.xlsx";
const preview = "E:/sl_obsidian/.tmp_weekly_report_20260918/preview.png";

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(input));
const sheet = workbook.worksheets.getItemAt(0);

sheet.getRange("C2:E2").values = [["2026/9/14-2026/9/20", null, null]];

sheet.getRange("C4:G4").values = [[
  "党委层面：\n" +
  "1.完成集团党组巡视整改落实方案及整改台账报送\n" +
  "2.汇总完善巡视整改专项自查报告7项及3项整改台账\n" +
  "3.完成地市网格单元党员基本情况统计表填报"
, null, null, null, null]];
sheet.getRange("J4").values = [["李兵、王统"]];

sheet.getRange("C5:G5").values = [[
  "支部层面：\n" +
  "1.完成基层党建考核、党员先锋模范作用、基层党组织生活不规范等专项自查整改报告\n" +
  "2.审核王文龙发展对象相关材料，持续推进李佳鹏、和安宁接收预备党员工作\n" +
  "3.完成党员先锋岗水晶牌照片汇总并对接制作\n" +
  "4.收集审核各支部三季度党课材料"
, null, null, null, null]];
sheet.getRange("J5").values = [["郑苗、祝文娟"]];

sheet.getRange("C6:G6").values = [[
  "宣传及其他：\n" +
  "1.完善2026年本地党建考核方案，梳理巡视整改、清朗行动、统战团委及五星支部考核要点\n" +
  "2.完成授课效果评价表等材料准备"
, null, null, null, null]];
sheet.getRange("J6").values = [["申琳、祝文娟"]];

sheet.getRange("C7:G7").values = [[
  "团委层面：\n" +
  "1.印发青年员工心理健康专题培训通知，组织开展专题培训\n" +
  "2.梳理2026年度共青团和青年工作质量评价体系\n" +
  "3.推进团青奖励报账，提前谋划团干部培训和“青马工程”学员推荐"
, null, null, null, null]];
sheet.getRange("J7").values = [["行鹏敏、祝文娟"]];

sheet.getRange("C9:I9").values = [[
  "党委层面：\n" +
  "1.跟进巡视整改专项报告报送及整改台账后续落实\n" +
  "2.准备党委第一议题和理论学习中心组学习材料\n" +
  "3.持续完善党建考核方案并做好上会准备"
, null, null, null, null, null, null]];
sheet.getRange("J9").values = [["李兵、王统"]];

sheet.getRange("C10:I10").values = [[
  "支部层面：\n" +
  "1.推进李佳鹏、和安宁接收预备党员及有关材料归档\n" +
  "2.跟进党员先锋岗水晶牌制作发放\n" +
  "3.督促各支部完成9月主题党日、三季度党课及集中研讨材料归档\n" +
  "4.做好专兼职党务工作者履职资料月底上传"
, null, null, null, null, null, null]];
sheet.getRange("J10").values = [["郑苗、祝文娟"]];

sheet.getRange("C11:I11").values = [[
  "其他：\n" +
  "1.持续做好宣传稿件编审、公众号发布和省公司素材报送\n" +
  "2.完成党建考核补充材料整理\n" +
  "3.做好9月份相关材料报账和归档"
, null, null, null, null, null, null]];
sheet.getRange("J11").values = [["申琳、祝文娟"]];

sheet.getRange("C12:I12").values = [[
  "团委层面：\n" +
  "1.根据正式通知做好团干部培训报名\n" +
  "2.提前物色并准备“青马工程”学员推荐人选\n" +
  "3.完善共青团和青年工作质量评价佐证材料"
, null, null, null, null, null, null]];
sheet.getRange("J12").values = [["行鹏敏、祝文娟"]];

// Keep the established template visual language; only adapt row heights to current text volume.
const heights = {4: 84, 5: 108, 6: 70, 7: 88, 9: 82, 10: 102, 11: 76, 12: 82};
for (const [r, h] of Object.entries(heights)) sheet.getRange(`A${r}:J${r}`).format.rowHeight = h;

const check = await workbook.inspect({kind: "table", range: "Sheet1!A1:J12", include: "values,formulas", tableMaxRows: 12, tableMaxCols: 10, maxChars: 15000});
console.log(check.ndjson);
const errors = await workbook.inspect({kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: {useRegex: true, maxResults: 100}, summary: "final formula error scan", maxChars: 3000});
console.log(errors.ndjson);

const img = await workbook.render({sheetName: "Sheet1", range: "A1:J12", scale: 1.4, format: "png"});
await fs.writeFile(preview, new Uint8Array(await img.arrayBuffer()));
const out = await SpreadsheetFile.exportXlsx(workbook);
await out.save(output);
console.log(JSON.stringify({output, preview}));

import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const templatePath = "D:/work/周月季半年年/月报/7月工作总结及8月工作计划20260802.xlsx";
const outputDir = "E:/sl_obsidian/outputs/20260901_8月工作总结及9月工作计划";
const outputPath = path.join(outputDir, "8月工作总结及9月工作计划.xlsx");
const previewPath = path.join(outputDir, "preview.png");

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(templatePath));
const ws = workbook.worksheets.getItemAt(0);

const setValue = (addr, value) => {
  ws.getRange(addr).values = [[value]];
};

setValue("C2", "8月");
setValue("I2", new Date(2026, 8, 1));
setValue("A8", "9\n月\n工\n作\n计\n划");

setValue(
  "C4",
  "党委：\n1、政治理论学习和议事决策：持续做好党委会“第一议题”、党委理论学习中心组学习和党委会党建议题材料准备，完成中心组小结、网络意识形态上会材料及8月党委会“三重一大”材料归档。\n2、巡视整改和专项自查：围绕省公司巡视整改要求，梳理学习贯彻、班子“一岗双责”、组织生活、党员先锋模范和党建考核等重点任务，推进基层党建考核作用未发挥、党员先锋模范作用发挥不够、组织生活不规范等专项自查整改。\n3、重点事项报送：完成省第十二次党代会代表推荐人选相关材料衔接，更新清砥工程台账，开展上半年“三重一大”执行情况总结，规范党委用印申请流程和材料管理。"
);
setValue(
  "C5",
  "基层党支部：\n1、组织生活和主题党日：督促各支部开展“三会一课”、主题党日和党组织生活规范化管理，完成活动通知、材料准备、联通先锋平台录入提醒和资料归档。\n2、整改整治和台账闭环：对学习教育台账、正确政绩观整改台账和党建考核问题清单逐项复盘，形成班子和个人台账汇总表，持续补齐缺项、完善闭环。\n3、党员发展和队伍建设：组织入党积极分子报名摸排，推进发展对象政审、档案审查和材料归集等工作，完善发展党员电子材料。\n4、品牌创建和考核申报：推进二季度“立足岗位做贡献、服务发展当先锋”评选结果兑现、三季度党员先锋岗申报和公示，衔接国企开放日活动及帮扶资金使用情况。"
);
setValue(
  "C6",
  "宣传及其他工作：\n1、宣传报道：持续做好信息编审、公众号推送、版面制作和党建动态报送，围绕八一、微巡察、国企开放日等重点工作形成宣传成果。\n2、材料报送和专项配合：完成意识形态问题自查、清朗行动材料整理邮寄，参加市直工委党务人员培训，做好微巡察现场检查资料调阅和问题记录。\n3、日常保障：推进党建费用报销、中心组发言稿准备和党建工作动态上报等日常工作。\n4、流程沉淀：围绕党建考核、立足岗位做贡献等周期性事项，进一步梳理工作流程，提升规范化水平。"
);
setValue(
  "C7",
  "团委工作：\n1、团青基础工作：做好新员工入职主题团日、团员推优、团委考核矩阵和团组织关系资料整理。\n2、青年活动和宣传：推进青年宣讲团大赛意见征集、青年科技创新创意大赛、青年精神素养提升和主题团课资料准备。\n3、协同支撑：结合国企开放日、宣传报道和党建工作，完善团青宣传素材和支撑材料归档。"
);

setValue("J4", "已完成");
setValue("J5", "已完成");
setValue("J6", "已完成");
setValue("J7", "已完成");

setValue(
  "C9",
  "党委层面：\n1、继续做好9月党委会、党委理论学习中心组学习和“第一议题”材料准备，完成党委会议题归档。\n2、按节点推进巡视整改、党建考核本地化考核方案和专项整改报告报送，完善佐证材料。\n3、继续推进学习贯彻习近平新时代中国特色社会主义思想、全面从严治党和正确政绩观等相关材料整理和报送。"
);
setValue(
  "C10",
  "支部层面：\n1、下发9月主题党日文件，督促各支部按时开展并完成联通先锋平台录入。\n2、持续做好基层党建考核、党员先锋模范作用、组织生活不规范等专项自查整改，补齐缺项清单。\n3、继续推进发展对象政审、党员发展材料归集和组织生活整改材料整理。\n4、做好国企开放日后续材料归档和支部台账更新。"
);
setValue(
  "C11",
  "宣传及其他：\n1、形成意识形态自查整改报告和学习贯彻习近平新时代中国特色社会主义思想自查报告，持续做好宣传信息编审和党建动态报送。\n2、配合完成9月重点活动宣传策划、素材整理和上报。"
);
setValue(
  "C12",
  "团委：\n1、完成团委考核清单梳理，做好青年活动、团员推优和团青材料归档。\n2、结合9月工作安排，继续推进青年活动组织和宣传素材报送。"
);

setValue("J9", new Date(2026, 8, 30));
setValue("J10", new Date(2026, 8, 30));
setValue("J11", new Date(2026, 8, 30));
setValue("J12", new Date(2026, 8, 30));

await fs.mkdir(outputDir, { recursive: true });

const preview = await workbook.render({
  sheetName: ws.name,
  autoCrop: "all",
  scale: 1,
  format: "png",
});
await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);

console.log(JSON.stringify({ outputPath, previewPath }, null, 2));

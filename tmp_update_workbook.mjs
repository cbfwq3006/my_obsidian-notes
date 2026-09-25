import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const inputPath='D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx';
const outputDir='E:/sl_obsidian/outputs/20260923_推动落实情况更新';
const outputPath=outputDir+'/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务完成情况-截至20260923.xlsx';
await fs.mkdir(outputDir,{recursive:true});
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(inputPath));
const s=wb.worksheets.getItem('Sheet1');
const p51=`截至2026年9月23日，“第一议题”和党委理论学习中心组学习制度持续规范落实；上半年累计召开党委会25期、开展“第一议题”学习131项，完成中心组学习6次。完成学习贯彻习近平新时代中国特色社会主义思想专项自查整改，补齐2023—2026年重点学习内容，完善选题审核、跟进学习和季度复盘机制。正确政绩观学习教育完成阶段总结并启动“回头看”，乡村振兴、消费帮扶等工作同步推进，阶段目标总体达成。`;
const q51=`按照年度统筹、月度推进、周度落实的节奏推进。三季度下发9月主题党日安排，完成省公司三季度集中研讨列席及支部研讨时间协调；完成正确政绩观学习教育总结，9月部署“回头看”，明确9月底研究整改销号、10月10日前研究开展情况。消费帮扶统计报送、资金拨付、“兴农周”本地化文件及展销活动按计划推进。`;
const r51=`一是完成理论学习专项自查，补齐滞后专题，建立“第一议题”选题三级审核、重要讲话和指示批示跟进学习、季度“回头看”机制；中心组成员累计“四下基层”53次，解决问题79项，完善制度9项。二是完成正确政绩观学习教育动员部署、读书班、专题研讨、专题党课、问题查摆整改及总结，启动复盘检视“回头看”。三是组织9月主题党日和三季度集中研讨列席，推进宣传、典型选树、党员先锋岗等工作。四是完成消费帮扶统计、资金拨付和“兴农周”安排，持续落实乡村振兴帮扶任务。`;
const p55=`截至2026年9月23日，持续推进中央巡视、集团党组巡视及省公司党委巡察整改，已完成集团党组巡视河南整改落实方案和相关台账更新，形成“一岗双责”、党建考核、党员先锋模范作用、党组织生活、理论学习、意识形态、全面从严治党等7项专项自查整改报告。阶段性整改任务已完成，需长期坚持事项持续推进，整改质效和成果转化机制进一步巩固。`;
const q55=`按计划完成巡视整改任务承接、问题认领、责任分解和正式方案报送；9月18日至20日完成中央巡视整改台账、现场检查评估共性问题台账、省公司党委巡察整改台账更新汇总，并完成7项专项报告。后续按照10月10日、11月10日、12月20日等节点持续更新报送整改台账和整改报告。`;
const r55=`一是对照集团党组巡视反馈意见，建立整改方案和台账，逐项明确责任领导、责任部门、整改措施、目标和时限。二是围绕7个方面开展专项自查，补齐制度、流程、资料和监督短板，建立节点提醒、复核销号、季度督导和成果转化机制。三是动态更新中央巡视、集团巡视共性问题和省公司巡察整改台账，强化党委专题研究、监督审核和日常督办。四是坚持已完成事项巩固提升、阶段性事项跟踪问效、长期事项常态推进，防止问题反弹。`;
// Preserve template formatting; update only the requested rows and corresponding screenshot labels.
s.getRange('D51:D55').values=[['付刚'],[null],[null],[null],['付刚']];
s.getRange('H51:H55').values=[['党建工作部（党委宣传部、党委统战部）/工会'],[null],[null],[null],['党建工作部（党委宣传部、党委统战部）/工会']];
s.getRange('P51:S51').values=[[p51,q51,r51,'是']];
s.getRange('P55:S55').values=[[p55,q55,r55,'是']];
// Add the new status header using the existing header style, then set body status style to match the adjacent progress cells.
s.getRange('S1').copyFrom(s.getRange('R1'),'all');
s.getRange('S1').values=[['任务是否完成序时进度']];
s.getRange('S51').copyFrom(s.getRange('R51'),'all');
s.getRange('S55').copyFrom(s.getRange('R55'),'all');
s.getRange('S51:S55').values=[['是'],[null],[null],[null],['是']];
const out=await SpreadsheetFile.exportXlsx(wb); await out.save(outputPath);
console.log(outputPath);

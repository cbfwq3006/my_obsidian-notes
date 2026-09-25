import fs from "node:fs/promises"; import {FileBlob,SpreadsheetFile} from "@oai/artifact-tool";
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load("D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx"));
for(const [name,range] of [['head','A1:S5'],['targets','A49:S57']]){const img=await wb.render({sheetName:'Sheet1',range,scale:0.25,format:'png'}); await fs.writeFile(`E:/sl_obsidian/tmp_${name}.png`,new Uint8Array(await img.arrayBuffer()));}

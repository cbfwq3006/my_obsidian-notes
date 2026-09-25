import fs from "node:fs/promises";
import {FileBlob, SpreadsheetFile} from "@oai/artifact-tool";
const input=await FileBlob.load("D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx");
const wb=await SpreadsheetFile.importXlsx(input);
console.log((await wb.inspect({kind:'region',sheetId:'Sheet1',range:'A44:S57',maxChars:30000,tableMaxRows:20,tableMaxCols:19,tableMaxCellChars:500})).ndjson);
const img=await wb.render({sheetName:'Sheet1',range:'A44:S57',scale:1,format:'png'});
await fs.writeFile('E:/sl_obsidian/tmp_q2_rows44_57.png',new Uint8Array(await img.arrayBuffer()));

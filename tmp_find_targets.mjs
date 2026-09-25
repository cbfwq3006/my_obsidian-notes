import {FileBlob,SpreadsheetFile} from "@oai/artifact-tool";
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load("D:/work/2026/7/1 党组16号文豫联通党委1号文/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务目标、计划和举措-二季度.xlsx"));
for(const term of ['任务十三','13-1','13-2','13-3','13-4','任务十四','14-1']) console.log(term,(await wb.inspect({kind:'match',searchTerm:term,options:{maxResults:20},summary:term,maxChars:5000})).ndjson);

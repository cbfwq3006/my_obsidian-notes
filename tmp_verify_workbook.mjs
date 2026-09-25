import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const p='E:/sl_obsidian/outputs/20260923_推动落实情况更新/焦作公司党委认真落实习近平总书记重要指示批示精神推动企业高质量发展行稳致远实施方案年度重点任务完成情况-截至20260923.xlsx';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p)); const s=wb.worksheets.getItem('Sheet1');
console.log('KEY', (await wb.inspect({kind:'table',sheetId:'Sheet1',range:'D51:S55',include:'values,formulas',tableMaxRows:10,tableMaxCols:20,tableMaxCellChars:500,maxChars:30000})).ndjson);
console.log('ERRORS', (await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A',options:{useRegex:true,maxResults:300},summary:'final formula error scan'})).ndjson);
for(const [n,r] of [['whole','A1:S57'],['focus51','M51:S51'],['focus55','M55:S55']]){const img=await wb.render({sheetName:'Sheet1',range:r,scale:n==='whole'?0.5:1,format:'png'}); await fs.writeFile(`E:/sl_obsidian/outputs/20260923_推动落实情况更新/${n}.png`,new Uint8Array(await img.arrayBuffer()));}

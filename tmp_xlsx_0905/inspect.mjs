import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const inputPath = 'D:/work/2026/9/1 集团党组巡视河南整改台账-焦作市分公司/集团党组巡视河南整改台账-焦作市分公司.xlsx';
const input = await FileBlob.load(inputPath);
const wb = await SpreadsheetFile.importXlsx(input);
console.log((await wb.inspect({kind:'workbook,sheet,table',maxChars:12000,tableMaxRows:8,tableMaxCols:32,tableMaxCellChars:120})).ndjson);
const sheets = wb.worksheets.items;
for (const s of sheets) {
  console.log('SHEET', s.name);
  const used = s.getUsedRange();
  console.log('USED', used ? used.address : 'none');
  if (used) {
    const vals = used.values;
    console.log('ROWS', vals.length, 'COLS', vals[0]?.length);
    console.log(JSON.stringify(vals.slice(0, Math.min(vals.length, 30))));
  }
  console.log((await wb.inspect({kind:'computedStyle',sheetId:s.name,range:'A1:AA15',maxChars:5000})).ndjson);
}
const render = await wb.render({sheetName:sheets[0].name,autoCrop:'all',scale:1,format:'png'});
const fs = await import('node:fs/promises');
await fs.writeFile('E:/sl_obsidian/tmp_xlsx_0905/original.png', new Uint8Array(await render.arrayBuffer()));

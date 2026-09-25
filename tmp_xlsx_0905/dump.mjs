import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const input = await FileBlob.load('D:/work/2026/9/1 集团党组巡视河南整改台账-焦作市分公司/集团党组巡视河南整改台账-焦作市分公司.xlsx');
const wb = await SpreadsheetFile.importXlsx(input);
const s = wb.worksheets.getItem('台账');
const vals = s.getRange('A1:AB199').values;
const out=[];
for(let i=0;i<vals.length;i++){
  const r=vals[i];
  if(i<5 || r.slice(16).some(v=>v!==null && v!=='')) out.push({row:i+1, A:r[0],B:r[1],C:r[2],D:r[3],E:r[4],F:r[5],G:r[6],H:r[7],I:r[8],J:r[9],K:r[10],L:r[11],M:r[12],N:r[13],O:r[14],P:r[15],Q:r[16],R:r[17],S:r[18],T:r[19],U:r[20],V:r[21],W:r[22],X:r[23],Y:r[24],Z:r[25],AA:r[26],AB:r[27]});
}
await (await import('node:fs/promises')).writeFile('E:/sl_obsidian/tmp_xlsx_0905/rows.json', JSON.stringify(out,null,2), 'utf8');
console.log('rows',out.length);
console.log(JSON.stringify(out.slice(0,12),null,2));

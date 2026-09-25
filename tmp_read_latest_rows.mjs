import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const p=process.argv[2];const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));const s=wb.worksheets.getItemAt(0); for(let r=1;r<=60;r++){let v=s.getRange(`A${r}:P${r}`).values[0]; if(v.some(x=>x!==null&&x!=='')) console.log(r,JSON.stringify(v));}

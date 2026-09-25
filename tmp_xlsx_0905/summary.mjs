import fs from 'node:fs/promises';
const rows=JSON.parse(await fs.readFile('E:/sl_obsidian/tmp_xlsx_0905/rows.json','utf8'));
for(const r of rows){
 if(r.row<=5) continue;
 console.log(JSON.stringify({row:r.row,E:r.E,F:r.F?.slice(0,120),R:r.R?.slice(0,180),S:r.S?.slice(0,180),T:r.T,U:r.U,V:r.V,W:r.W,X:r.X,Y:r.Y,Z:r.Z,AA:r.AA,AB:r.AB,nN:r.N?.length||0,nO:r.O?.length||0,nZ:r.Z?.length||0,nAA:r.AA?.length||0}));
}

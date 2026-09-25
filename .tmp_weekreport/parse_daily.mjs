import fs from 'node:fs'; import path from 'node:path';
for(const f of fs.readdirSync('E:/sl_obsidian/工作日报').filter(x=>x.startsWith('2026-09-')&&x.endsWith('.md'))){
 const p='E:/sl_obsidian/工作日报/'+f; const t=fs.readFileSync(p,'utf8'); console.log('===='+f); for(const l of t.split(/\r?\n/)){if(l.startsWith('- ')&&/(工作总结|完成|党建|宣传|整改|党课|中心组|会议|党内法规|五星|先锋|主题党日|第一议题)/.test(l)) console.log(l.slice(0,700));}
}

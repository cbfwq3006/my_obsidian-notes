import fs from 'node:fs';
for(const d of ['07','08','09']){
 const p=`E:/sl_obsidian/工作日报/2026-09-${d} 工作日报.md`; const lines=fs.readFileSync(p,'utf8').split(/\r?\n/);
 console.log('\n===='+d);
 for(let i=0;i<lines.length;i++){
  if(/工作总结|三季度|整改|党课|党内法规|集中研讨|五星|先锋岗|主题党日|宣传|第一议题|中心组|三会一课|组织关系|消费帮扶|兴农周|水晶牌/.test(lines[i])){
   console.log((i+1)+':'+lines[i].slice(0,500));
  }
 }
}

# AI数据看板（动态版）

> 说明：本页依赖 Obsidian 的 `Dataview` 插件。  
> 用途：动态查看 AI 知识库建设、摄取队列、输出成品和近期资料活跃度。  
> 配套静态分析：[[projects/AI数据看板]]

## 一、知识库总览

```dataviewjs
const folders = [
  ["wiki/来源", "来源页"],
  ["wiki/概念", "概念页"],
  ["wiki/实体", "实体页"],
  ["wiki/对比", "对比页"],
  ["raw", "原始资料"],
  ["projects", "项目页"],
  ["outputs", "输出成品"]
];

const rows = folders.map(([path, label]) => [label, dv.pages(`"${path}"`).length]);
dv.table(["模块", "数量"], rows);
```

## 二、摄取状态快照

```dataviewjs
const pages = dv.pages('"工作日报" or "01 Inbox" or "projects"');
const rows = [
  ["待摄取", pages.where(p => p.codex_ingest == "pending").length],
  ["已处理", pages.where(p => p.codex_ingest == "done").length],
  ["跳过入库", pages.where(p => p.codex_ingest == "skip").length],
  ["已标记入库", pages.where(p => p.wiki_update == true).length],
  ["高价值待沉淀", pages.where(p => p.material_value == "high" && p.wiki_update != true).length]
];
dv.table(["指标", "数量"], rows);
```

## 三、待摄取清单

```dataview
TABLE date AS 日期, material_value AS 价值, wiki_update AS 已入库, file.mtime AS 最后更新
FROM "工作日报" OR "01 Inbox" OR "projects"
WHERE codex_ingest = "pending"
SORT file.mtime DESC
```

## 四、已处理但近期更新的页面

```dataview
TABLE date AS 日期, material_value AS 价值, file.mtime AS 最后更新
FROM "工作日报" OR "01 Inbox" OR "projects"
WHERE codex_ingest = "done"
SORT file.mtime DESC
LIMIT 20
```

## 五、超期未处理提醒

> 重点看已放入队列、但超过 7 天还未处理的记录。

```dataview
TABLE date AS 日期, material_value AS 价值, file.mtime AS 最后更新
FROM "工作日报" OR "01 Inbox" OR "projects"
WHERE codex_ingest = "pending" AND date <= date(today) - dur(7 days)
SORT date ASC
```

## 六、本月沉淀活跃度

```dataviewjs
const monthStart = dv.date("today").startOf("month");

const sourceMonth = dv.pages('"工作日报" or "01 Inbox" or "projects"')
  .where(p => p.file.mtime >= monthStart).length;

const wikiMonth = dv.pages('"wiki"')
  .where(p => p.file.mtime >= monthStart).length;

const outputsMonth = dv.pages('"outputs"')
  .where(p => p.file.mtime >= monthStart).length;

dv.table(
  ["指标", "数量"],
  [
    ["本月更新的工作/项目页", sourceMonth],
    ["本月更新的 wiki 页面", wikiMonth],
    ["本月更新的输出成品", outputsMonth]
  ]
);
```

## 七、近期输出成品

```dataview
TABLE file.mtime AS 更新时间
FROM "outputs"
SORT file.mtime DESC
```

## 八、AI专题资料池

> 说明：本区按**文件名和路径**识别 AI 相关资料，适合快速回看，不等同于全文检索。

```dataviewjs
const aiRegex = /(AI|Codex|Claudian|Claude Code|skill|Hermes|Obsidian)/i;
const pages = dv.pages('"raw" or "projects" or "obsidian笔记/参考资料" or "2026" or "工作日报"')
  .where(p => aiRegex.test(p.file.name) || aiRegex.test(p.file.path))
  .sort(p => p.file.mtime, 'desc')
  .slice(0, 30);

dv.table(
  ["资料", "路径", "更新时间"],
  pages.map(p => [p.file.link, p.file.path, p.file.mtime])
);
```

## 九、核心工作流入口

- [[projects/Obsidian-Claudian-Codex每日工作流]]
- [[projects/Codex自动摄取队列]]
- [[projects/AI数据看板]]

## 十、每周复盘建议

- 先看“摄取状态快照”，判断有没有积压；
- 再看“超期未处理提醒”，优先清空旧的 `pending`；
- 再看“本月沉淀活跃度”，判断最近是“只记不沉淀”还是“边用边沉淀”；
- 最后看“近期输出成品”，确认 AI 是否真正转化成材料产出。


# Codex 自动摄取队列

这个页面用于在 Obsidian 里集中查看哪些日记、项目笔记需要 Codex 摄取进 wiki。

## 每日记录待摄取

```dataview
TABLE date AS 日期, material_value AS 价值, wiki_update AS 是否已入库
FROM "工作日报" OR "01 Inbox" OR "projects"
WHERE codex_ingest = "pending"
SORT date DESC
```

## 已摄取但可复查

```dataview
TABLE date AS 日期, file.mtime AS 更新时间
FROM "工作日报" OR "01 Inbox" OR "projects"
WHERE codex_ingest = "done"
SORT file.mtime DESC
LIMIT 20
```

## 给 Codex 的固定指令

请处理 `E:\sl_obsidian\projects\Codex自动摄取队列.md` 中 `codex_ingest: pending` 的笔记：

1. 先判断哪些内容值得进入 `wiki/`，哪些只留在原笔记。
2. 对有长期复用价值的内容，创建或更新 `wiki/来源/` 页面。
3. 如涉及已有概念/实体，更新对应 `wiki/概念/` 或 `wiki/实体/`。
4. 更新 `wiki/index.md` 和追加 `wiki/log.md`。
5. 将已处理笔记的 `codex_ingest` 改为 `done`，并在“Codex 处理记录”写明更新了哪些页面。

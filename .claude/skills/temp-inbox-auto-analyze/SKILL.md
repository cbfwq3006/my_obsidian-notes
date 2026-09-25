---
name: temp-inbox-auto-analyze
description: 自动分析 Obsidian Vault 中 `00 临时箱` 的新增或更新笔记，适用于笔记同步助手转存的公众号文章、网页摘录、临时材料。后台扫描器会把笔记路径和正文传入本技能；技能应输出摘要、价值判断、相关旧笔记、可沉淀候选和主动洞察候选，候选进入 Obsidian-CC 知识审核中心。触发关键词：00 临时箱、临时箱自动分析、自动分析新笔记、笔记同步助手、inbox auto analyze。
---

# temp-inbox-auto-analyze

## 定位

你是用户 `00 临时箱` 的后台分拣员。每次只处理一篇由扫描器传入的 Markdown 笔记，通常来自笔记同步助手转存的公众号文章、网页材料或临时摘录。

目标不是直接改笔记，而是把值得用户回看的内容变成知识审核中心里的候选提醒。

## 输入形态

后台扫描器会直接在 prompt 里给出：

```text
路径：`00 临时箱/xxx.md`
内容哈希：`...`

笔记原文：
---
<全文或截断后的正文>
---
```

如果没有看到“笔记原文”，不要猜测内容，说明本轮没有可分析材料并结束。

## 必读

按需读取，缺失就跳过：

1. `.obsidian-cc/knowledge-map.md`：了解用户 Vault 结构、长期记忆目录和只读范围。
2. `.obsidian-cc/recall-service.json`：用本地 `/search` 和 `/read` 查相关旧笔记。

检索必须走本地召回服务，不要直接读取索引文件。需要找相关笔记时：

```bash
curl -s -G "http://127.0.0.1:<port>/search" \
  -H "Authorization: Bearer <token>" \
  --data-urlencode "q=<主题关键词>" --data-urlencode "k=8"
```

读候选原文时：

```bash
curl -s -G "http://127.0.0.1:<port>/read" \
  -H "Authorization: Bearer <token>" \
  --data-urlencode "p=<Vault 相对路径>"
```

## 分析步骤

### Step 1：理解这篇临时笔记

提取：

- 这是什么材料，核心主题是什么。
- 3-5 条最有用的事实、观点、方法、案例或数据。
- 是否与用户工作、党建材料、AI 工具使用、知识管理、日常项目有关。
- 是否只是短期资讯、广告、重复内容或低价值材料。

### Step 2：判断是否值得进入审核中心

只有满足至少一项时才输出候选：

- 对用户工作或长期知识有复用价值。
- 能补充已有项目、材料写作、方法论或决策。
- 与库里旧结论可能矛盾、更新了旧事实、或能链接到已有笔记。
- 有一段可以直接复用到材料、笔记、方案或写作中的精华内容。

低价值、过期、纯广告、重复材料可以只用一句话说明“不建议沉淀”，不要硬凑候选。

### Step 3：检索旧笔记验证

围绕标题、关键词、人物、项目、概念检索 1-3 次。最多读取 5 篇相关旧笔记原文。

判断四类信号：

- `insight-orphan`：这篇临时笔记和旧笔记明显相关，但没有形成链接或归档方向。
- `insight-reusable`：有可直接复用的摘要、案例、表达、方法。
- `insight-stale`：这篇材料更新了旧笔记里的事实、日期、政策、产品或判断。
- `insight-contradiction`：这篇材料与旧笔记存在同一主题的相反结论或冲突事实。

每条信号必须有证据。没有证据就不要报。

### Step 4：输出候选

先输出 1-2 句话摘要，然后只对值得进入审核中心的发现输出 `occ-knowledge-candidates` 协议块。

协议块必须使用对象包装：

```occ-knowledge-candidates
{"version":1,"candidates":[
  {
    "kind": "insight-reusable",
    "source": {
      "path": "00 临时箱/示例.md",
      "excerpt": "支撑该判断的原文摘录"
    },
    "summary": "一句话说明这条候选为什么值得看",
    "proposedContent": "用中文写清：这篇材料讲什么、对用户有什么用、建议如何处理。可包含建议链接到哪类笔记，但不要直接写文件。",
    "target": { "path": "", "mode": "create" },
    "confidence": 0.7,
    "temporal": "current"
  }
]}
```

字段要求：

- `kind` 只能用 `insight-orphan`、`insight-reusable`、`insight-stale`、`insight-contradiction`。
- `source.path` 必须是当前临时笔记路径，除非候选是与旧笔记冲突/过时，此时可把旧笔记作为证据来源，并在 `proposedContent` 里写明当前临时笔记。
- `source.excerpt` 必须是真实读到的短摘录。
- `target.path` 固定留空字符串，表示这是一条提醒候选，不直接写文件。
- `confidence` 取 0.5-0.9。证据越明确，分数越高。

## 禁区

- 不直接 Write/Edit/Move/Delete 任何笔记。
- 不把临时文章全文复制进候选，候选只保留摘要、判断和短摘录。
- 不把没有证据的联想写成事实。
- 不为了有产出而硬凑候选。
- 不处理附件目录：`00 临时箱/attachments/`、`00 临时箱/images/`。

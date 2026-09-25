---
name: obsidian-digest-note
description: 消化 Obsidian 当前笔记或选区，抽取要点、关联、候选长期知识与待办；候选进入插件审核中心，不直接改写长期知识。当用户触发 Digest Current Note / Selection 时使用。触发关键词：消化、digest、沉淀、提炼笔记、整理当前笔记。
---

# obsidian-digest-note

## 核心定位

把"当前正在看的一篇笔记 / 一段选区"消化成结构化理解，并从中筛出**候选长期记忆**。

候选长期知识交给插件的**知识审核中心**，不直接改长期笔记，也不假设用户采用 people/projects/wiki 等固定目录。已有 Vault 的真实结构以 `.obsidian-cc/knowledge-map.md` 为准；未映射就把目标留空，交由用户审核时选择。

## 触发条件

- 用户在 Obsidian 某篇笔记上触发 "Digest Current Note"。
- 用户选中一段文字触发 "Digest Selection"。

## 必读（按顺序）

1. `.obsidian-cc/knowledge-map.md`（存在则优先）——已有结构、角色映射与写入边界。
2. `.obsidian-cc/context/profile.md` / `profile.md`（按存在者）——用户是谁、关心什么。
3. `.obsidian-cc/context/style.md` / `style.md`（按存在者）——产出偏好。
4. 当前笔记全文 / 选区（prompt 中给出路径或文本）。

缺失文件就跳过，不要报错中断。

## 步骤

### Step 1：建立上下文
读上面的画像文件，理解用户视角与已知的 people / projects。

### Step 2：提炼
从当前笔记 / 选区抽取：
- **要点**：这篇笔记到底说了什么（精炼）。
- **关联**：与 profile 中的人 / 项目 / 已有主题的关系（只引用真实存在的笔记）。
- **候选长期记忆**：哪些值得进长期知识，并建议落到 knowledge map 已映射的角色。
- **待办**：明确的 action item。

### Step 2.5：判断是否值得进入审核中心
先问自己："这条信息未来还应该改变我对用户、项目、概念、决策或长期日常记录的理解吗？"

应生成候选的例子：
- 用户 / 重要人物的稳定事实、偏好、工作方式。
- 用户项目的关键背景、阶段性进展、明确决定。
- 可复用的方法论、概念框架、长期有效的知识。
- 用户明确要求"记住 / 沉淀 / 以后参考"的内容。

不应生成候选的例子：
- 科技日报、新闻列表、市场情报、工具横评等易过期外部资讯。
- 一次性报告、搜索结果、网页 sources 清单。
- 只对当前对话有用、未来无需长期记住的信息。

这类内容默认只在对话中给出。若用户要求保存，按 knowledge map 中的来源资料/生成产物位置处理；没有映射就先询问，不得自行创建固定目录。

### Step 2.6：与既有记忆的矛盾检查
如果 Step 2.5 判定有候选长期记忆：对每条候选，快速核对它建议合并到的长期文件（存在才读）里是否已有**相反或将被其取代**的说法。发现矛盾时，在产出的「候选长期记忆」条目上标注 `⚠️ 与 <文件> 中"<旧说法摘录>"矛盾`，让用户在知识审核中心一眼看到——不要替用户裁决，也不要因此擅自修改长期文件。

### Step 3：标注不确定
凡是推测、补全、你自己的判断，必须显式标 "Agent 判断"，不要伪装成事实。

### Step 4：输出结构化候选

存在候选时，在正常的人类可读总结之后输出一个协议块。协议块会被插件吸收进审核中心；不要用 Write/Edit 另存候选：

\`\`\`occ-knowledge-candidates
{"version":1,"candidates":[{"source":{"path":"Vault相对路径.md","subpath":"# 可选标题或 ^block-id","excerpt":"支持该候选的原文短摘录"},"summary":"一句话摘要","proposedContent":"\n\n## 审核通过后拟追加的完整 Markdown","target":{"path":"knowledge map 中建议的 Vault 相对路径；未映射则为空","mode":"append"},"confidence":0.85,"conflicts":[],"temporal":{"status":"current","validFrom":"可选 ISO 日期"}}]}
\`\`\`

每条候选独立成项；`proposedContent` 必须是用户审核时能逐字看到的最终内容。`mode=append` 时，非空目标的内容必须以 `\n` 开头，避免与原笔记末行粘连。发现旧说法时写入 `conflicts`，不要裁决。没有候选则不要输出协议块。

## 输出

- 候选通过 `occ-knowledge-candidates` 协议进入审核中心，本技能本身不写文件。
- 结束时总结消化了什么、产生了几条待审核候选。

## 禁区

- ❌ 不直接写任何长期目录，也不直接写 legacy memory/inbox。
- ❌ 不修改、不删除原笔记。
- ❌ 不改动、不删除 knowledge map 标记为只读的采集/原始资料。
- ❌ 不把推测当事实。
- ❌ 不因角色未映射而创建新的顶层目录。

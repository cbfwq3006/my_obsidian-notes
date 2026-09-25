---
name: obsidian-review-inbox
description: 审核 Obsidian 的 memory/inbox/ 待确认沉淀，归纳整理成一份"可确认清单"，标明每条建议合并到哪一层长期记忆。不执行合并，只产出供用户确认的清单。触发关键词：审核 inbox、整理收件箱、review、待确认、收件箱积压。
---

# obsidian-review-inbox

## 核心定位

第二大脑管线的**第二步**：把 `memory/inbox/` 里零散累积的待确认沉淀，归纳成一份清晰的「**可确认清单**」，让用户一眼看清"有哪些东西等着进长期记忆，分别该去哪一层"。

**只读 + 产出清单，绝不执行合并**。合并由 `obsidian-apply-memory` 在用户确认后进行。

## 触发条件

- 用户说"审核一下 inbox / 整理收件箱 / review 待确认内容"。
- inbox 积压较多，用户想做一次集中清理前的盘点。

## 必读（按顺序）

1. `profile.md` —— 用户是谁、关心什么。
2. `vault.md` —— 目录用途与写入规则。
3. `memory_policy.md` —— 哪些值得长期记住、合并到哪一层。
4. `memory/inbox/` 下的全部 `*.md`（按日期，近→远）。

缺失文件就跳过，不要报错中断。

## 步骤

### Step 1：扫描 inbox
列出 `memory/inbox/` 下所有文件，读取内容（已有的"建议的长期记忆改动"小节尤其重要）。

### Step 2：归纳去重
把跨多天、重复或相关的条目合并同类项，按主题/对象聚合。识别：
- 关于**人**的稳定事实 → 建议 people/
- 项目进展 / 关键决定 → 建议 projects/ 或 decisions/
- 可复用概念 / 方法 → 建议 wiki/
- 一次性、易过期、未证实 → 建议**丢弃或留存**，并说明理由。

### Step 3：判定状态
每条标注：
- **建议目标层**（people / projects / wiki / decisions / daily / 丢弃）。
- **置信度**：是事实还是 "Agent 判断"。
- **来源**：来自哪个 inbox 文件。

### Step 4：产出可确认清单
把清单**写入** `memory/inbox/_review-<YYYY-MM-DD>.md`（下划线前缀，便于和日常 inbox 区分），结构见下。同时在对话里给出摘要。

## 输出

写入 `memory/inbox/_review-<YYYY-MM-DD>.md`：

```md
# Inbox 审核清单（<YYYY-MM-DD>）

> 这是供你确认的清单。确认后，可让我用 obsidian-apply-memory 执行合并。

## 建议合并

### → people/
- [ ] [置信度] 内容摘要（来源：inbox/xxx.md）→ 建议落到 people/<谁>.md

### → projects/
- [ ] …

### → wiki/
- [ ] …

### → decisions/
- [ ] …

## 建议丢弃 / 暂留
- 内容 —— 理由（过期 / 未证实 / 一次性）

## 待补充信息
- 哪些条目信息不足、需要你补充后才好沉淀
```

结束时用一两句话告诉用户：盘了多少条、建议合并多少、丢弃多少，并提示"确认后可执行 apply-memory"。

## 禁区

- ❌ 不执行任何长期目录的写入 / 合并（那是 apply-memory 的职责）。
- ❌ 不修改、不删除既有 inbox 文件的内容（审核清单是新文件）。
- ❌ 不改动 raw/。
- ❌ 不把推测当事实——推测一律标 "Agent 判断"。

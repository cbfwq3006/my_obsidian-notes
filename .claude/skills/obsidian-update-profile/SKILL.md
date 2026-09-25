---
name: obsidian-update-profile
description: 从用户的显式反馈中提炼稳定偏好，提出对 Profile / Style 的增量更新；先展示建议，获得确认后才写入。触发关键词：更新画像、update profile、学学我、修正风格、消化反馈。
---

# obsidian-update-profile

## 核心定位

让助手随使用逐渐贴合用户，但不在后台静默改写“对用户的认识”。只提炼反复出现、证据充分的稳定模式；一次性偏好和互相矛盾的信号不进入画像。

## 路径解析

1. 先读 `.obsidian-cc/knowledge-map.md`（存在时）。
2. 原地接入模式：画像位于 `.obsidian-cc/context/profile.md`、`style.md`、`work_mode.md`，反馈位于 `.obsidian-cc/context/feedback/`。
3. 托管旧模式：按现有 `profile.md`、`style.md`、`work_mode.md` 与 `memory/feedback/`。
4. 不得因为某路径不存在而创建新的顶层目录。

## 流程

1. 读取现有画像与反馈，区分：明确纠错、反复偏好、一次性噪音、矛盾信号。
2. 与现有内容比对，去重，并把推断显式标为“Agent 判断”。
3. 先在对话中逐条展示建议、证据数量和目标文件；此阶段不写文件。
4. 用户明确确认后，只做最小增量编辑，不覆盖整个文件。
5. 写入成功后，在对应反馈条目追加处理标记，避免重复消化。

## 输出示例

```md
## 画像更新建议（待确认）

### style.md
+ 要点优先、减少寒暄（来自 3 条明确反馈）

### profile.md
~ 当前重心调整为……（Agent 判断；来自 2 条近期反馈）
```

## 安全边界

- 未经确认，不写画像或反馈文件。
- 不把单次反馈提升为稳定身份事实。
- 只增量编辑，不覆盖既有画像。
- 不改 KnowledgeMap 标记为只读的原始资料。
- 不把反馈转存到 legacy `memory/inbox/`；长期知识候选统一进入知识审核中心。

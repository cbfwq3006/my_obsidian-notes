---
name: obsidian-work-dashboard
description: 基于当前 KnowledgeMap 和 Vault 真实变化，生成今天值得关注的工作驾驶舱。默认只在对话中输出；仅在用户明确要求保存且已映射生成产物目录时写文件。适用于每日启动、今天看什么、项目总览、daily brief。
---

# obsidian-work-dashboard

## 核心定位

把用户已有的 Vault 变成“今天该关注什么”的入口，不要求迁移到插件规定的目录。

## 先理解当前 Vault

1. 先读 `.obsidian-cc/knowledge-map.md`（若存在），把它作为目录、只读和长期知识边界。
2. 再读 KnowledgeMap 指向的 context 文件；托管旧布局才回退到根目录的 `profile.md`、`work_mode.md`、`memory_policy.md`。
3. 用本地召回先找最近活跃的项目、决策、日志、来源与生成产物，再只深读少量关键笔记。
4. KnowledgeMap 未映射的角色视为未知，不创建 `projects/`、`reports/`、`raw/`、`memory/` 等默认目录。

## 输出内容

- 今日重点：最值得推进的 3–5 件事。
- 活跃对象：最近有变化或反复出现的项目、课题、栏目、客户、代码库等。
- 阻塞/等待：缺决策、缺信息、等回复或长期停滞的事项。
- 待消化材料：有依据地指出新近采集/来源材料；没有可靠信号就省略。
- 待审核知识：只提示用户打开统一知识审核中心，不读写 legacy `memory/inbox/`。
- 风险与下一步：每条带 Vault 来源；无直接来源的建议标“Agent 判断”。

默认在对话中给一份可扫读的驾驶舱，不自动落盘。用户明确要求保存时：

- 只写 KnowledgeMap 已映射的“生成产物”文件夹；
- 目标是 tag / Property / Base 或尚未映射时，先请用户选择具体文件路径；
- 不覆盖已有内容，除非用户明确指定。

## 禁区

- 不直接改人物、项目、概念、决策、日志等长期知识。
- 不改 KnowledgeMap 标记为只读的材料。
- 不把驾驶舱或候选知识写进 legacy `memory/inbox/`。
- 不把职业模板强加给用户；组织维度必须来自 Vault 证据或用户说明。

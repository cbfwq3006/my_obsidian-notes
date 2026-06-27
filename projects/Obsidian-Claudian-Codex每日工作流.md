# Obsidian + Claudian + Codex 每日工作流

## 每天怎么记

1. 在 Calendar 或 Periodic Notes 中创建当天日记，使用 `每日记录模板`。
2. 普通流水账写在“工作记录”。
3. 以后可能写材料、复盘、汇报会用到的内容，写在“值得进入知识库的内容”。
4. 保持 frontmatter 中 `codex_ingest: pending`，表示等待 Codex 判断是否入库。
5. 如果当天没有任何沉淀价值，把 `codex_ingest` 改成 `skip`。

## Codex 怎么自动摄取

当前设计是“半自动”：Obsidian 自动形成队列，Codex 按队列批量摄取。真正让 Codex 完全无人值守自动改 wiki，风险较高，容易把流水账也写进知识库。

推荐每天或每周对 Codex 说：

`请处理 E:\sl_obsidian\projects\Codex自动摄取队列.md 中待摄取的记录，更新 wiki，并把处理过的笔记状态改为 done。`

## 写材料怎么调用知识库

固定说法：

`请基于 E:\sl_obsidian\wiki 中已有内容，生成一份 XXX，保存到 E:\sl_obsidian\outputs。`

如果材料和某个项目有关，可以补一句：

`同时参考 E:\sl_obsidian\projects\项目名 中的过程材料。`

## 状态字段

- `codex_ingest: pending`：等待 Codex 判断并摄取。
- `codex_ingest: done`：已经处理。
- `codex_ingest: skip`：只留痕，不进 wiki。
- `wiki_update: true`：本笔记内容已经进入 wiki。
- `material_value: high/medium/low`：以后写材料的复用价值。

## 判断什么应该进入 wiki

应该进入：

- 反复会用到的工作方法。
- 可复用的讲话、通知、汇报表达。
- 典型案例、问题清单、整改措施。
- 重要政策、制度、会议精神的提炼。
- 能支撑以后写材料的数据、事实、口径。

不建议进入：

- 纯日程流水账。
- 一次性电话沟通。
- 无复用价值的临时文件名。
- 未核实的个人判断。

## 固定格式周报生成

用户提供的周报附件格式为 Excel 表《工作总结与工作计划》，固定分为两块：

1. 本周完成情况
2. 下周计划

每块按以下四类组织：党委层面、支部层面、其他、团委层面。生成周报时应优先按 `templates/固定格式周报模板.md` 输出，必要时再生成同格式 Excel。

固定指令：

`请按 E:\sl_obsidian\templates\固定格式周报模板.md 的格式，结合本周 E:\sl_obsidian\工作日报、手写日历记录和 D:\work\2026 本周新增文件，生成本周工作总结与下周计划。`

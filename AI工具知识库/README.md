---
type: project
created: 2026-07-13
updated: 2026-07-13
tags:
  - AI工具知识库
  - 自动抓取
  - 行业资讯
---

# AI工具知识库

## 目标

每天自动抓取 AI 行业资讯、工具测评和教程文章，按主题归档；每周生成 1 份知识复盘报告，提炼核心观点和趋势。

## 文件夹说明

- [[AI工具知识库/01_行业资讯]]：行业新闻、公司动态、监管政策、资本与竞争格局。
- [[AI工具知识库/02_工具测评]]：新工具、工具榜单、产品体验、对比评测。
- [[AI工具知识库/03_教程文章]]：教程、指南、实操案例、提示词、工作流。
- [[AI工具知识库/04_模型产品更新]]：模型发布、API、产品更新、开源模型、能力升级。
- [[AI工具知识库/05_趋势观察]]：跨来源沉淀出的长期趋势和判断。
- [[AI工具知识库/06_每周复盘]]：每周自动生成的知识复盘报告。
- [[AI工具知识库/99_资料源]]：RSS 资料源配置和说明。

## 当前自动化

- 每日抓取脚本：`scripts/ai_tool_kb/fetch_ai_tool_kb.ps1`
- 每周复盘脚本：`scripts/ai_tool_kb/weekly_review_ai_tool_kb.ps1`
- 定时任务安装脚本：`scripts/ai_tool_kb/install_tasks.ps1`

## 使用方式

手动抓取一次：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/ai_tool_kb/fetch_ai_tool_kb.ps1
```

手动生成周复盘：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/ai_tool_kb/weekly_review_ai_tool_kb.ps1
```

## 后续可升级

1. 增加中文信息源。
2. 增加网页全文抓取。
3. 增加 AI 自动摘要、观点提炼、趋势合并。
4. 与 Obsidian wiki 的来源页、概念页打通。

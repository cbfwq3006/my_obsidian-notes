---
name: obsidian-fetch-wechat
description: 抓取微信公众号文章（mp.weixin.qq.com），按当前 KnowledgeMap 存到已有来源资料位置；可选提取长期知识候选到统一审核中心。触发关键词：公众号文章、抓这篇微信文章、收藏文章、fetch wechat。
---

# obsidian-fetch-wechat

## 核心定位

把微信文章纳入用户已有的资料系统，不创建固定 `sources/` 或 `memory/inbox/` 管线。

## 前置边界

1. 先读 `.obsidian-cc/knowledge-map.md`（若存在）。
2. “来源资料”映射到 folder 时，把该文件夹记为 `<SOURCE_DIR>`；只有 tag / Property / Base、尚未映射或映射损坏时，先请用户给出具体存档文件夹，不能猜目录。
3. 读取映射的 profile/style context；托管旧布局才回退到根目录同名文件。
4. 值得长期保留的事实只输出 `occ-knowledge-candidates` 协议，交给知识审核中心，不直接写长期笔记或 legacy inbox。

## 步骤

### 1. 识别完整 URL

提取 `mp.weixin.qq.com/s/...` 完整链接并保留查询参数。缺参数可能得到“参数错误”页。

### 2. 只读抓取

用 GET 请求把 HTML 输出到 stdout，不写中间文件：

```bash
curl -sS -L -m 25 --compressed -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 MicroMessenger/8.0.42 Language/zh_CN" "<URL>"
```

从响应中提取标题以及 `id="js_content"` / `rich_media_content` 正文，去除脚本、样式和无关导航，转成干净 Markdown。不要执行网页脚本。

### 3. 先判有效，再存档

- 能提取标题且正文超过约 100 字：继续。
- 参数错误、验证页、文章删除/迁移：停止并说明原因。
- HTTP 成功但正文为空/过短：请用户从微信复制正文粘贴过来，不保存空壳。

### 4. 写入已有来源位置

仅在 `<SOURCE_DIR>` 已明确时写入：`<SOURCE_DIR>/<YYYY-MM-DD>-<标题 slug>.md`。同名文件存在就加 `-2`、`-3`，不覆盖。

```md
---
source: <完整 URL>
title: <标题>
author: <可确认的作者或公众号；未知则写未知>
fetched: <YYYY-MM-DD>
fetched_by: obsidian-fetch-wechat
---

# <标题>

<正文 Markdown>

> 来源：[<标题>](<完整 URL>)
```

### 5. 可选消化

只有用户明确要求“提炼/消化/记住重点”时才判断长期价值：

- 稳定人物事实、项目关键背景、可复用方法可能成为候选；
- 新闻、行情、临时观点和文章正文通常只保留为来源；
- 候选用 `occ-knowledge-candidates`，来源必须指向刚保存的文件并带原文摘录、时间状态和置信度；目标未映射就留空。

## 输出

告诉用户实际保存路径、标题、是否产生审核候选。没有明确来源目录时，只说明已抓到内容并等待用户选择位置。

## 禁区

- 不写 KnowledgeMap 的只读范围，不创建 `raw/`、`sources/` 或 `memory/inbox/`。
- 不直接改人物、项目、概念、决策、日志等长期知识。
- 不把失效页、验证页或空壳保存为文章。
- 不虚构作者、正文或图片内容；推断必须标“Agent 判断”。

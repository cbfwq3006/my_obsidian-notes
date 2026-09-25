---
name: obsidian-fetch-xiaohongshu
description: 抓取小红书笔记（xiaohongshu.com / xhslink.com），按当前 KnowledgeMap 存到已有来源资料位置；可选提取长期知识候选到统一审核中心。触发关键词：小红书、红书笔记、抓这篇小红书、xhs、fetch xiaohongshu。
---

# obsidian-fetch-xiaohongshu

## 核心定位

把小红书笔记纳入用户已有的资料系统，不创建固定 `sources/` 或 `memory/inbox/` 管线。

小红书反爬很强，纯 HTTP 抓取经常只拿到登录墙或 JS 空壳。**本技能把"抓不到就转人工粘贴"当作一等路径，不是失败兜底**——拿不到正文时直接请用户粘贴，不反复重试、不伪造内容。

## 前置边界

1. 先读 `.obsidian-cc/knowledge-map.md`（若存在）。
2. “来源资料”映射到 folder 时，把该文件夹记为 `<SOURCE_DIR>`；只有 tag / Property / Base、尚未映射或映射损坏时，先请用户给出具体存档文件夹，不能猜目录。
3. 读取映射的 profile/style context；托管旧布局才回退到根目录同名文件。
4. 值得长期保留的事实只输出 `occ-knowledge-candidates` 协议，交给知识审核中心，不直接写长期笔记或 legacy inbox。

## 步骤

### 1. 识别 URL

支持三种形态：

- `xiaohongshu.com/explore/<id>` 或 `/discovery/item/<id>`：直接用。
- `xhslink.com/...`（App 分享短链）：需跟随跳转，`curl -L` 已覆盖。
- App 分享文案（含表情和 token 的一长串）：从里面提取 `http://xhslink.com/...` 部分。

URL 上的查询参数一律保留，缺参数更容易被判定为异常来源。

### 2. 只读抓取（一次，不重试）

```bash
curl -sS -L -m 25 --compressed -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1" "<URL>"
```

正文优先从 SSR 数据里取：HTML 中的 `window.__INITIAL_STATE__` JSON，笔记标题在 note 的 `title`、正文在 `desc`。取不到再退回 DOM 里的 `#detail-title` / `#detail-desc` 或 `.note-content`。

不要执行网页脚本，不下载图片。

### 3. 先判有效，再存档

- 能提取标题或正文、且正文超过约 50 字（小红书笔记普遍短，阈值低于公众号）：继续。
- 登录墙、验证页、笔记已删除/被设为私密：**停止抓取，直接请用户从 App 复制正文粘贴过来**，并说明是平台限制而非链接错误。
- 拿到 HTML 但正文为空/过短：同上转粘贴，不保存空壳。

用户粘贴的内容按同样格式存档，`fetched_by` 仍记本技能，另在 frontmatter 记 `capture: manual-paste`。

### 4. 去重检查

写入前先在 `<SOURCE_DIR>` 里搜一次相同 `source:` URL（短链要按跳转后的最终 URL 比对）。已存在就告知用户已收录过、给出路径，问清是否要覆盖更新，默认不重复写第二份。

### 5. 写入已有来源位置

仅在 `<SOURCE_DIR>` 已明确时写入：`<SOURCE_DIR>/<YYYY-MM-DD>-<标题 slug>.md`。同名文件存在就加 `-2`、`-3`，不覆盖。

标题缺失时用笔记首句截断做标题，并标注是 Agent 生成的标题。

```md
---
source: <完整 URL>
title: <标题>
author: <可确认的作者昵称；未知则写未知>
platform: xiaohongshu
fetched: <YYYY-MM-DD>
fetched_by: obsidian-fetch-xiaohongshu
---

# <标题>

<正文 Markdown>

> 来源：[<标题>](<完整 URL>)
```

### 6. 可选消化

只有用户明确要求“提炼/消化/记住重点”时才判断长期价值：

- 可复用的方法、清单、选购/避坑经验可能成为候选；
- 种草、探店、行情、个人生活记录通常只保留为来源；
- 候选用 `occ-knowledge-candidates`，来源必须指向刚保存的文件并带原文摘录、时间状态和置信度；目标未映射就留空。

小红书内容主观性强，候选置信度默认不高于中等，并在候选里标明是单一用户经验而非通用结论。

## 输出

告诉用户实际保存路径、标题、内容是抓取还是粘贴得来、是否产生审核候选。没有明确来源目录时，只说明已拿到内容并等待用户选择位置。

## 禁区

- 不写 KnowledgeMap 的只读范围，不创建 `raw/`、`sources/` 或 `memory/inbox/`。
- 不直接改人物、项目、概念、决策、日志等长期知识。
- 不把登录墙、验证页或空壳保存为笔记。
- 不为绕过反爬去伪造签名头、爆破参数或高频重试。
- 不虚构作者、正文或图片内容；推断必须标“Agent 判断”。

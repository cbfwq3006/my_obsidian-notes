---
name: obsidian-fetch-zhihu
description: 抓取知乎回答、专栏文章与想法（zhihu.com / zhuanlan.zhihu.com），按当前 KnowledgeMap 存到已有来源资料位置；可选提取长期知识候选到统一审核中心。触发关键词：知乎、知乎回答、专栏文章、抓这个知乎链接、fetch zhihu。
---

# obsidian-fetch-zhihu

## 核心定位

把知乎内容纳入用户已有的资料系统，不创建固定 `sources/` 或 `memory/inbox/` 管线。

知乎对未登录请求有较强限制，长回答常被折叠或要求登录。**拿不到完整正文时直接请用户粘贴，不重试、不截断存半截**。

## 前置边界

1. 先读 `.obsidian-cc/knowledge-map.md`（若存在）。
2. “来源资料”映射到 folder 时，把该文件夹记为 `<SOURCE_DIR>`；只有 tag / Property / Base、尚未映射或映射损坏时，先请用户给出具体存档文件夹，不能猜目录。
3. 读取映射的 profile/style context；托管旧布局才回退到根目录同名文件。
4. 值得长期保留的事实只输出 `occ-knowledge-candidates` 协议，交给知识审核中心，不直接写长期笔记或 legacy inbox。

## 步骤

### 1. 判断内容类型

知乎三种形态，正文位置不同，先判类型再抓：

| 形态 | URL 特征 | 标题来源 |
| --- | --- | --- |
| 回答 | `zhihu.com/question/<qid>/answer/<aid>` | 问题标题 + 答主 |
| 专栏文章 | `zhuanlan.zhihu.com/p/<pid>` | 文章自带标题 |
| 想法 | `zhihu.com/pin/<pid>` | 无标题，取首句 |

`zhihu.com/question/<qid>` 不带 answer id 时是问题页（含多个回答）：**先问用户要哪一个回答**，不要把整页回答一锅端存下来。

### 2. 只读抓取（一次，不重试）

```bash
curl -sS -L -m 25 --compressed -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" "<URL>"
```

正文提取顺序：

1. 优先找 SSR JSON：`js-initialData` 脚本块，回答正文在 `content`、文章在 `content`、点赞数在 `voteupCount`。
2. 退回 DOM：回答 `.RichContent-inner` / `.CopyrightRichText-richText`，文章 `.Post-RichText`，想法 `.PinItem-content`。

保留正文里的代码块、列表、引用结构，转成对应 Markdown。不要执行网页脚本。

### 3. 先判有效，再存档

- 能提取标题与正文、且正文超过约 100 字：继续。
- 登录墙、验证页、内容已删除/仅创作者可见：**停止抓取，请用户从浏览器复制正文粘贴过来**，说明是平台限制。
- 正文末尾出现“登录后查看全部”“展开阅读全文”等截断标记：视为**不完整**，同样转粘贴，不保存半截内容。

用户粘贴的内容按同样格式存档，frontmatter 记 `capture: manual-paste`。

### 4. 去重检查

写入前先在 `<SOURCE_DIR>` 搜相同 `source:` URL。同一问题下的不同回答是不同内容，按 answer id 区分，不算重复。已存在就告知路径并问是否覆盖更新，默认不重复写。

### 5. 写入已有来源位置

仅在 `<SOURCE_DIR>` 已明确时写入：`<SOURCE_DIR>/<YYYY-MM-DD>-<标题 slug>.md`。同名文件存在就加 `-2`、`-3`，不覆盖。

回答类的标题用 `<问题标题> - <答主>` 形式，便于同一问题下多个回答并存。

```md
---
source: <完整 URL>
title: <标题>
author: <答主/作者；未知则写未知>
platform: zhihu
content_type: <answer | article | pin>
fetched: <YYYY-MM-DD>
fetched_by: obsidian-fetch-zhihu
---

# <标题>

<正文 Markdown>

> 来源：[<标题>](<完整 URL>)
```

### 6. 可选消化

只有用户明确要求“提炼/消化/记住重点”时才判断长期价值：

- 领域科普、技术方案、行业分析里的稳定结论可能成为候选；
- 个人经历、争论、时事观点通常只保留为来源；
- 候选用 `occ-knowledge-candidates`，来源必须指向刚保存的文件并带原文摘录、时间状态和置信度；目标未映射就留空。

知乎回答是**个人观点而非权威结论**，候选里必须带上答主身份，不能把一家之言写成客观事实。

## 输出

告诉用户实际保存路径、标题、内容类型、是抓取还是粘贴得来、是否产生审核候选。没有明确来源目录时，只说明已拿到内容并等待用户选择位置。

## 禁区

- 不写 KnowledgeMap 的只读范围，不创建 `raw/`、`sources/` 或 `memory/inbox/`。
- 不直接改人物、项目、概念、决策、日志等长期知识。
- 不把登录墙、验证页、截断正文或空壳保存为文章。
- 不为绕过反爬去伪造签名头、爆破参数或高频重试。
- 不虚构作者、正文或图片内容；推断必须标“Agent 判断”。

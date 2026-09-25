---
type: source
tags: [Codex, Obsidian, 知识库, 卡帕西方法, 私人助教]
sources: [[00 临时箱/把牛人资料丢进 Codex+Obsidian，让他变成你的私人助教！]]
created: 2026-08-05
updated: 2026-08-05
---

# 用Codex+Obsidian打造私人助教

> 原文：[[00 临时箱/把牛人资料丢进 Codex+Obsidian，让他变成你的私人助教！]]
> 作者：大瑜
> 来源：微信公众号「大瑜聊AI」
> 发布时间：2026-07-21

## 核心痛点

在没有 AI 之前，大家收集资料都是保存到微信收藏夹中一丢。

**看起来是收藏了，其实是资料的浪费。**

譬如你在网上看到一个牛逼的博主，但能和博主对话的机会有限。

## 解决方案

现在不一样了！

只需要将这个博主的公众号、视频号内容下载到 raw 中，通过 [[Codex]] + [[Obsidian]] 重新盘活这些资料。

**简单来说：让这个博主变成你的私人助教。**

## 三步流程

### 步骤1：收集博主的资料

所谓巧妇难做无米之炊，第一步就要去各种数据来源收集这个博主的全部信息。

#### 1. 网页收藏

使用 Obsidian Web Clipper 插件

#### 2. 公众号文章

使用 Skill：
```
https://clawhub.ai/harven-droid/skills/wechat-article-archive
```

#### 3. PDF/Word 转化

两种方法：
- 使用 **Markitdown File Converter** 插件，转换为 md 文件
- 让 Codex 自己写代码，给 PDF 转化为 md 文件

#### 4. 视频下载与转录

使用 **yt-dlp** 插件：

```
只需要这样说：
将yt-dlp这个插件，下载我的视频地址，xXXXXXX
然后用Whisper转化为逐字稿，如果本机没有安装，请帮我安装。
最后整体进行错别字的修改，形成md文档，保存到raw/shipin目录中。
```

工具链：
- yt-dlp：下载视频到本地
- Whisper：转化为逐字稿

### 步骤2：将内容转化到 wiki 中

提示词模板：

```
按照卡帕西的思路，将raw里面没有进入wiki的内容，导入到wiki中。
严格按照当前 AGENTS.md 执行：
1、内容初级总结放到wiki/sources中
2、如果资料里有值得长期复用的概念、方法论或术语，
   可以另存到 wiki/concepts/，但不是必做项。
3、提取值得长期维护的"实体—关系—实体"，
   更新所有的实体页，建立关联关系图谱。
4、提问的问题和回答，整理到wiki/questions 目录，
   便于知识库继续优化
```

**最终形成知识图谱**。

### 步骤3：开始提问

#### 优势对比

比网上的"乔布斯skill"、"张雪峰skill"要好很多。

**原因**：
- 知道资料来源自哪些文章
- 知道资料被哪些内容引用

#### 提问示例

```
如果一个产品，推广的时候，用户觉得贵怎么回复他
```

AI 会按照 wiki 的内容给你推荐。

#### 核心优势

**借助 Obsidian 的双链和外链体系，你还能清楚看到回答背后的资料来源。**

这才是知识库真正强大的地方。

## 知识库的四大应用

### 1. 回答问题

根据之前的内容，清晰回答你的问题。

### 2. 生成行业报告

结合内容的整理，形成行业报告。

### 3. 生成小红书内容

借助 image2 的功能，快速生成小红书内容。

### 4. 生成口播视频

借助 hyperperframe 的插件，快速生成简单的口播视频。

## 核心方法论

### 卡帕西思路

按照 Karpathy 的思路处理知识：
1. 初级总结放到 sources
2. 概念/方法论/术语放到 concepts（可选）
3. 实体关系图谱
4. 问答整理到 questions

### 知识库架构

```
raw/                  # 原始资料
├── 公众号文章/
├── shipin/           # 视频逐字稿
├── PDF文档/
└── ...

wiki/
├── sources/          # 内容总结
├── concepts/         # 概念方法论
├── entities/         # 实体页
└── questions/        # 问答记录
```

## 工具清单

| 用途 | 工具 |
|------|------|
| 网页收藏 | Obsidian Web Clipper |
| 公众号下载 | wechat-article-archive skill |
| 文档转换 | Markitdown File Converter 或 Codex |
| 视频下载 | yt-dlp |
| 语音转文字 | Whisper |
| 小红书生成 | image2 |
| 口播视频 | hyperperframe |

## 与通用 Skill 的对比

| 维度 | 通用 Skill（如"乔布斯skill"） | Codex+Obsidian 知识库 |
|------|-------------------------------|----------------------|
| 资料来源 | 不明确 | 清晰标注来源文章 |
| 内容关联 | 无 | 双链体系，可追溯引用关系 |
| 可验证性 | 低 | 高，可查看原始资料 |
| 定制性 | 通用化 | 高度个性化 |

## 核心价值

**将"死"的收藏变成"活"的知识库**

- 从被动收藏到主动对话
- 从信息孤岛到知识图谱
- 从一次性阅读到长期复用

## 金句

> "在没有AI之前，收藏就是资料的浪费。现在，收藏可以变成私人助教。"

> "这才是知识库真正强大的地方：不仅有答案，还能看到答案背后的资料来源。"

## Related Concepts

- [[Codex]]
- [[Obsidian]]
- [[知识库]]
- [[卡帕西方法]]
- 双链笔记
- 知识图谱
- RAW-WIKI 架构
- 资料盘活

## Related Entities

- 大瑜
- Karpathy（卡帕西）
- Obsidian Web Clipper
- Markitdown File Converter
- yt-dlp
- Whisper
- image2
- hyperperframe
- clawhub.ai

---
author: 摸鱼小李
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzA5OTIzMTE1OA==&mid=2247487848&idx=1&sn=c907d91c47f63f75c2c0f8be2357e593&chksm=9191bd1a96a91c9236af6916766291484bcd108f2459d8e4eaf615ce3651a689eb7638aef980&mpshare=1&scene=1&srcid=0712kfDEWUhWnBikyKTeYsfe&sharer_shareinfo=b722ce15a8a679bfe280b3c8981d0a0f&sharer_shareinfo_first=b722ce15a8a679bfe280b3c8981d0a0f#rd
saved: 2026-07-12 15:30:16
tags:
  - 笔记同步助手
id: 15b94081-2c66-460c-a2b9-5e6b939659da
---

公众号名称：摸鱼小李

作者名称：摸鱼小李

发布时间：2026-07-07 08:19

01不能再拖延了

大家好，我是**摸鱼小李**，每次发文章，都有读者问我这个公众号排版怎么做的，一直承诺给大家做一个公众号排版工具出来（其实真的做了）也能用，但是我自己不是很满意，最近几个月一直在忙**猹与猹**的事，也没时间重构....

![[笔记同步助手/images/bcb6199ad58c727539ed8cffa3763362_MD5.png]]

不能再拖延了，刚好前天晚上和好朋友**甲木（甲木未来派）**聊天，聊到这个话题，想着要不做成skill吧，开源出来，大家可以自己根据已有的模版去泛化，这样更有趣好玩，于是我们一拍即合，做个公众号排版gzh-designskill。

![[笔记同步助手/images/6d5589eec5d1397238bc816796cca193_MD5.png]]

该 skill 目前内置了 6 套主题模版（后续会持续更新），也可以自己设计主题模版。

这个skill，适配**WorkBuddy**/**Codex**/**Claude Code**等 Agent 工具，以下就是 WorkBuddy 安装gzh-designskill 排版出的效果。

![[笔记同步助手/images/54857fa09e89d8fc6adc7c00f34dcab6_MD5.png]]

02直接让 Agent 安装

1

使用最简单的方式

直接让你的**Agent**安装。

2

复制 README 里的安装 prompt

仓库 README 里有一段“给 AI 的安装prompt”，复制粘贴给你的**Claude Code**、**WorkBuddy**或其他 AI Agent，它会自动完成安装配置，使用引导直接问它即可。

具体的Skill设计大家可以看甲木的文章，或者让**Agent**去读仓库都行。跟大家简单聊聊另一件事——如何根据现有排版，设计自己独特的版式风格。

03排版也是一种产品设计

去年 9 月开始写公众号时，我就在思考一个问题：如何更省力、更好看地让 AI 帮我排版？

![[笔记同步助手/images/d560d0d1da3800d4918b60efcf93246e_MD5.jpg]]

![[笔记同步助手/images/4aac2af4fc7f46e82617d7ba30989af8_MD5.jpg]]

中间也迭代了一些版本，旧版本一路被淘汰，最后稳定用的就是**摸鱼绿**（也内置在 skill 主题中了）。

其实这套设计的思路很简单——组件库思维。正如我开头所说，公众号推文也应该有 UI 设计。「**摸鱼绿**」这套主题设计了26 个对应的组件，Agent 会根据不同文章类型去组合不同组件，并在现有组件基础上进行泛化，最终排版成一篇完整的文章。还有个好处是随时可以更新维护，想加新组件直接加，想优化某个组件单独改。

![[笔记同步助手/images/0d5ffb74c642d8f94570a8cea5fe6996_MD5.jpg]]

04欢迎来魔改

大家也可以尝试结合自己的特色 / IP去在这套组件主题上泛化，设计自己的排版组件库，形成自己的特色排版，欢迎大家来魔改gzh-designskill，沟通交流。

另外欢迎大家加入**猹与猹**一起来玩，一起交流创作经验。

![[笔记同步助手/images/a726dde447e7b85e0bc715858ad0d0ad_MD5.jpg]]

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/d1cec6e4_1783841414049?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA5OTIzMTE1OA%3D%3D%26mid%3D2247487848%26idx%3D1%26sn%3Dc907d91c47f63f75c2c0f8be2357e593%26chksm%3D9191bd1a96a91c9236af6916766291484bcd108f2459d8e4eaf615ce3651a689eb7638aef980%26mpshare%3D1%26scene%3D1%26srcid%3D0712kfDEWUhWnBikyKTeYsfe%26sharer_shareinfo%3Db722ce15a8a679bfe280b3c8981d0a0f%26sharer_shareinfo_first%3Db722ce15a8a679bfe280b3c8981d0a0f%23rd&s=obsidian)
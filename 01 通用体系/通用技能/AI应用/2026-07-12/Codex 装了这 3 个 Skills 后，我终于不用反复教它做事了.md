---
author: 卧龙君
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzYzOTU5MTc3MA==&mid=2247484489&idx=1&sn=018db238c6ffb708bff362afb10367b1&chksm=f16d86efffc2100cbebed67654d0b68807a42c4ab0ff0c6adff25e28d9ecb329c9aa797c0965&mpshare=1&scene=1&srcid=0712oa2Xuw7wbCOo0PNbRMtP&sharer_shareinfo=cbc48c7abf411c886ecf974885e3e4a3&sharer_shareinfo_first=cbc48c7abf411c886ecf974885e3e4a3#rd
saved: 2026-07-12 11:28:50
tags:
  - 笔记同步助手
id: 1c7712d9-0992-442a-b418-595cb09b5eba
---

公众号名称：风火AI
作者名称：卧龙君
发布时间：2026-07-01 07:08

![[attachments/笔记同步图片/03028e9dd2dc455a14cc5cc52cc62d08_MD5.png]]
![[attachments/笔记同步图片/2926be279f51a0212f3ff53752787c98_MD5.png]]
![[attachments/笔记同步图片/06f4f9750d2ef6994c2a96383f53b70b_MD5.png]]

Codex 用了一周,我发现它最大的问题不是能力,是"记性"。同一个需求要教 5 遍。装了 3 个 Skills 后,它终于不用我反复教了。
我平时用 Codex 最多的场景是写代码、整理数据、做调研。
但有个很烦的事:每次开新会话,它都像失忆了一样。我要一遍一遍说"先写测试再写代码""别碰不相关的文件""做完记得问我"。
后来装了 3 个 Skills,这些问题全解决了。
不是那种"装了10个Skills覆盖80%场景"的清单文。我只推荐 3 个,但每一个都解决一个致命痛点。
01 装 grill-me:让 Codex 先问清楚再动手Codex 最大的毛病是带着错误假设就开工。
你跟它说"加个登录功能",它直接写代码,不会追问你用 OAuth 还是扫码、用户表有没有 openid 字段、老用户怎么绑定。
grill-me 就是来治这个毛病的。
装完之后,每次写代码前,Codex 会像个产品经理一样追问你:
微信登录用 OAuth2 还是扫码?你的用户表有 openid 字段吗?老用户怎么绑定微信?直到你和它对需求的理解完全一致,才动手写代码。
我装了 grill-me 之后,返工率直接降了一半。 Reddit 上有人说"it completely changed how I plan with Codex",我深有体会。
安装命令:
npx skills add mattpocock/skills --skill grill-me -y -g02 装 planning-with-files:会话崩了也不怕Codex 会话聊久了会变傻。
上下文太长之后,它改东忘西。/compact 能压缩,但压缩完结构化进度信息全丢了。
planning-with-files 解决的是"会话接力"问题。
它把计划和进度写到三个文件里:task_plan.md(要做什么)、findings.md(发现了什么)、progress.md(做到哪了)。
下次开新会话,Codex 读这三个文件就能接着干,不从头来。
我和它配合的方式是这样的: grill-me 做完规划,planning-with-files 记录进度,会话崩了,新会话读文件接着干。
三个文件,永远不丢上下文。
安装命令:
npx skills add OthmanAdi/planning-with-files -y -g03 装 Karpathy Guidelines:让 Codex 少干蠢事装了前两个,Codex 已经能打了。但还有个问题:它喜欢顺手"改进"你没要求的东西。
你让它改个 bug,它重构半个文件。你说写个登录,它给你加了注册、找回密码、短信验证。
Karpathy Guidelines 把这些行为编成四条硬规则:
先想再写:有多种理解时列出来让你选,不偷偷选一个就跑简单优先:200 行能写完的别写 500 行,不加没要求的功能手术式改动:只碰必须改的文件,不顺便"优化"旁边的代码目标驱动:定义成功标准,写测试验证,循环直到通过这四条源自 Andrej Karpathy 今年 1 月分享的 AI 编码工作流观察,GitHub 上超过 17 万 stars。
装了之后,最明显的感受是:Codex 不再"自作聪明"了。
安装命令:
npx skills add multica-ai/andrej-karpathy-skills -y -g写在最后这三个 Skills,解决的是 Codex 使用中最常见的三个痛点:
grill-me:解决"不问就动手"的问题planning-with-files:解决"会话崩了丢上下文"的问题Karpathy Guidelines:解决"自作聪明多做多错"的问题装完之后,我的感受就一句话:Codex 终于像个长期配合的同事了。
不用反复教,不用随时救火,不用盯着它别改错文件。
觉得有用的话,点赞、在看、转发 三连支持一下
我整理了一份1000+精选GPT Image 2提示词大全,各种场景都有,直接复制就能用。
关注「风火AI」,回复「提示词」免费领取。
关注「风火AI」,每天一个AI实战技巧。

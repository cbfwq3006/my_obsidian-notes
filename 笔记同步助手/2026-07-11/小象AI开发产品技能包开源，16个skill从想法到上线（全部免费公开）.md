---
author: 小象君
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkwMzE5MjY2NA==&mid=2247494612&idx=1&sn=66efe6ce2af9dbff2c765d98bc36c328&chksm=c190bb7dc8e9eb5f5e14b677bb501f0dc0be61a1892f188bbb969a05357e1ed7934e78580df3&mpshare=1&scene=1&srcid=0711EbFydM4FzM1kqgWV1dj0&sharer_shareinfo=ee9dd839bb3cf9f83e179071563c98fd&sharer_shareinfo_first=ee9dd839bb3cf9f83e179071563c98fd#rd
saved: 2026-07-11 23:40:00
tags:
  - 笔记同步助手
id: 0b33f909-a8aa-4d8a-ad60-c56dfcbd3c31
---

公众号名称：小象AI

作者名称：小象君

发布时间：2026-07-07 17:58

过去两个月，我用AI Agent 做了十几个产品。

有一个叫「数独说」的小游戏，已经上线了，大家可以去体验一下。

我用类似的游戏逻辑顺手也做了一个海外网站版的数独，也上线了。

https://sudokuhint.com/

说真的，这个速度和这个产出，放在一年前我是不敢想的。

但是，做着做着你就会发现一个事情。开发的门槛确实大大降低了，但这离你能拿出一个真正不错的、有商业价值的产品，中间还有一段不小的距离。

所以我把这两个月做十几个产品过程中，磕磕绊绊踩的各种坑，梳理了一遍，整理成了这么一个 skill 包。

https://github.com/aixiaoxiang/xx-skills

```
xx-skills/
├── README.md              # 本文件
├── SKILL.md               # Trae IDE 入口 skill
├── CLAUDE.md              # Claude Code 项目级指令
├── VERSION                # 版本号
├── LICENSE
├── .cursorrules           # Cursor 项目级规则
├── AGENTS.md              # OpenAI Codex 开放标准指令
├── .claude-plugin/
│   └── marketplace.json
├── windsurf/
│   └── rules.md           # Windsurf 项目级规则
├── docs/
│   ├── glossary.md        # 术语表
│   └── skill-link-map.mmd # skill 关系图
├── skills/
│   ├── index.json         # skill 依赖 manifest
│   ├── 01-think/          # 想清楚
│   │   ├── README.md
│   │   ├── xx-clarify/
│   │   ├── xx-research/
│   │   ├── xx-goal/
│   │   ├── xx-ai-feature/
│   │   └── xx-business/
│   ├── 02-build/          # 做出来
│   │   ├── README.md
│   │   ├── xx-prd/
│   │   ├── xx-data/
│   │   ├── xx-safety/
│   │   ├── xx-backend/
│   │   ├── xx-setup/
│   │   ├── xx-brand/
│   │   ├── xx-blocks/
│   │   └── xx-ai/
│   └── 03-run/            # 跑起来
│       ├── README.md
│       ├── xx-track/
│       ├── xx-iterate/
│       └── xx-optimize/
```

AI agent 能干的事很多，办公、写作、设计，但我还是觉得，亲手做一个能上线的产品，是最能让你感受到这波技术变革冲击力的方式。

你得真的开始去用，去体验，跟你自己的日常需求产生联系，你才能感受到那个变化。这个东西你光听别人说是没用的，你得自己试。

先说你能拿到什么。

16 个 skill，覆盖从想法到上线的完整流程，分三个阶段，想清楚、做出来、跑起来。

来自我过去两个月 10+ 个已上线小程序项目的实战经验，不是纸上谈兵。

你不用写代码，你用自然语言提需求，AI 执行，你看结果提优化。你的角色是提需求和验收，AI 的角色是执行和改进。

全部免费，持续升级迭代。

![[笔记同步助手/images/32919be604c3b9353e7149836d48a802_MD5.png]]

支持所有AI Agent，不管你用哪个工具都能上手。

Trae IDE 原生支持 skill，把 xx-skills 文件夹放到 .trae/skills/ 目录下，输入 /xxskill 就能唤起入口，它会问你「你处于什么阶段」，然后帮你路由到对应的 skill。

Claude Code 会读取项目根目录的 CLAUDE.md，把仓库的 CLAUDE.md 复制到你项目里就行。

OpenAI Codex 用 AGENTS.md，Codex 会自动加载。

Cursor 用 .cursorrules 文件，复制到项目根目录就行。

其他 AI 编程工具，通用方法，在 AI 对话里，告诉它。

```
请把下面链接里的 skill 下载安装到本地。
GitHub 地址 https://github.com/aixiaoxiang/xx-skills
```

整个技能包分三层。

第一层叫想清楚。零技术门槛，适合所有人。在你写第一行代码之前，先想清楚。

5 个 skill，需求澄清、用户调研、定目标、判断产品要不要 AI 能力、商业模式。

这一层大多数人会直接跳过，上来就写代码，但我觉得这恰恰是大多数人做不出好产品的原因。你想都没想清楚，AI 帮你写代码写得越好，你跑得越快，跑偏的概率就越大。

![[笔记同步助手/images/6f46c2535fd6d341dfaceddc5b6a2dfd_MD5.png]]

第二层叫做出来。你想清楚了，开始动手开发。

8 个 skill，从 MVP 功能定义、数据评估、安全合规、后端搭建，到项目初始化、设计系统、组件库、AI 能力接入。这一层是大家最熟悉的，也是市面上教程最多的部分，但里面的坑并不少。

![[笔记同步助手/images/b5b12aa6d919cd01053de2c93a165ece_MD5.png]]

第三层叫跑起来。产品上线了，需要数据驱动迭代。

3 个 skill，数据埋点加 AI 质量监控、迭代验收方法论、性能优化。产品上线只是开始，不盯着数据迭代，上线了也等于没上线。

![[笔记同步助手/images/9d6a16ebeb22c0a2980db1340ed36f54_MD5.png]]

16 个 skill 不一定每个都要走一遍，但至少你得知道每个环节存在，才知道自己卡在哪。

我拿「小象取色」这个小程序举个例子。

小象取色，功能很简单。拿手机摄像头取色，生成匹配的诗词和海报，国风风格，好看也好玩。

功能简单到一句话能说完。但你真做的时候，会发现一堆问题。

比如取色。你以为是摄像头取个平均色就完了？？？不是的。你在手机上用的时候，如果取平均色，那个颜色会一直在跳。你得做聚焦，以中心区域的颜色为主来判断。这是一个算法问题。

比如老手机。有些用户的手机性能比较差，你摄像头实时取色的时候，老手机会卡。你得做性能分级，低端机降级处理，不然体验会崩掉。

比如速度。你拿摄像头对着一个地方，当然希望颜色马上变，诗词马上出来。有延迟的话体验就很差。但生成需要时间，你怎么让取色和诗词生成的节奏对上？

比如上线以后。你埋点了吗？你知道用户用得最多的是哪个功能吗？你知道 AI 生成的诗词质量怎么样？这些不看数据你是不知道的。

还有，酒香也怕巷子深。你产品做好了，怎么获客？怎么留存？流量从哪来？这些东西，你不在做产品之前就想清楚，等产品上线了再想就来不及了。

你看，一个功能简单到「摄像头取个色」的小程序，背后涉及取色算法、性能优化、AI 接入策略、界面设计、数据埋点、AI 质量监控、商业模式、运营迭代。

每一个环节都有坑，每一个坑我都踩过。

这就是 16 个 skill 存在的理由。不是说你要把 16 个全走一遍才能做产品，而是你得知道这些环节存在。你不知道，就会卡在那里，还不知道自己卡在哪。那种感觉才是最难受的。

有几点我得提前说清楚，免得误导你。

skill 包能做的是帮你少走弯路，不能帮你保证结果。

目前只覆盖微信小程序场景。出海网站场景的架构已经预留了，但具体实现还在补充。

许可证方面，个人学习、开发自己的产品、社区分享，随便用，保留署名就行。付费课程、企业内训、批量分发、嵌入商业产品销售，需要单独授权。

做产品的过程中如果遇到具体问题需要交流，有答疑群（收费），可以加微信号 xxskill ，或者扫码。

![[笔记同步助手/images/31186b88cb84b68cf3086e8257444575_MD5.jpg]]

有需要的加，技能包本身是完整的，持续迭代更新的，不进群也不影响使用。

GitHub 地址再说一遍

https://github.com/aixiaoxiang/xx-skills

最后说一句。

我做这个技能包，是因为我自己在做这十几个产品的过程中，反复踩了同样的坑，走了很多弯路。

我当时就想，要是有个人把这些东西提前整理好给我，我能省多少事。

所以如果你也想用 AI 做产品，但不知道从哪开始，或者已经开始但卡住了，希望这 16 个 skill 能帮你少走一些弯路。

先想清楚，再动手做，用数据迭代。就这三句话。

以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～

谢谢你看我的文章。

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/a2693405_1783784398010?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzkwMzE5MjY2NA%3D%3D%26mid%3D2247494612%26idx%3D1%26sn%3D66efe6ce2af9dbff2c765d98bc36c328%26chksm%3Dc190bb7dc8e9eb5f5e14b677bb501f0dc0be61a1892f188bbb969a05357e1ed7934e78580df3%26mpshare%3D1%26scene%3D1%26srcid%3D0711EbFydM4FzM1kqgWV1dj0%26sharer_shareinfo%3Dee9dd839bb3cf9f83e179071563c98fd%26sharer_shareinfo_first%3Dee9dd839bb3cf9f83e179071563c98fd%23rd&s=obsidian)
---
author: 西滨
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg3ODg0NDA3MQ==&mid=2247487418&idx=1&sn=010bda5568a80234ca4120e98b9dfc18&chksm=ce25a17722df78a1e0c2e3cb6d4fbfb65520bce27de4cbf226572469ba154b1cd1936a9f0e59&mpshare=1&scene=1&srcid=0627aeJRhAqSySIludFvmhMI&sharer_shareinfo=476d6ed872739e222245a10028157267&sharer_shareinfo_first=476d6ed872739e222245a10028157267#rd
saved: 2026-06-27 23:55:33
tags:
  - 笔记同步助手
id: 2131859a-9102-4ff0-a58c-b70abcd501a6
---

公众号名称：西滨AI随想

作者名称：西滨

发布时间：2026-06-16 17:33

飞书妙搭/Feishu Spark ( https://miaoda.feishu.cn/home ) 搭建简单的小应用很方便，但是搭建复杂的业务系统还是很麻烦，这里漏一点，那里少一点，就算是嘴炮来让妙搭 Vibe Coding，也无名火起。我也是突发奇想，能否让 Codex 来当教练/专家，指导妙搭来实现系统？试了一下，还算流畅，中间也碰到一些坑，最终效果还不错。

事情缘起于朋友让我开发一套简单的楼盘销售系统，嗯，由于实在太简单，就没打算搞独立的数据库，准备就用飞书多维表格来当存储。（飞书多维表格非常不错：《[以飞书多维表格作为后端，建立完全自动刷新的网站](https://mp.weixin.qq.com/s?__biz=Mzg3ODg0NDA3MQ==&mid=2247487078&idx=1&sn=621e89a5ed5e5f147daaabcf20a3c6c1&scene=21#wechat_redirect)》）

先在 Codex 中新建一个项目（注意，只要是需要持续跟进的，哪怕是网页版的 ChatGPT，建议也建立项目。这样上下文会收敛到项目，交流会顺畅很多）。

然后输入下面的提示词开始：

   朋友委托开发一个楼盘销售系统，这个系统使用的人数<5人。我计划用飞书的多维表格来搭建。你先设计好多维表格，我再在飞书多维表格里面将其转换为应用。  主要的表可能就包括房源、客户。  房源表可以参考《市区在卖房源.xlsx》，但是要额外添加图片和视频字段，方便发图片和视频给客户查看。你需要进行分析，不能照搬《市区在卖房源.xlsx》 。因为系统和Excel表不一样。  客户都是个人，要记录基本信息如联系方式等，以及客户的买房需求。  你先生成 README.md 和 AGENTS.md。  

我这里先让 Codex 生成 README.md、AGENTS.md。README.md 和 AGENTS.md 是项目的一体两面描述，README.md 给人类阅读，AGENTS.md 给智能体阅读，侧重点不同。这两个规范调整好之后，后面沟通就畅快了。

这里和 Codex 交互几轮，多维表格就建好了。Codex 自动处理了「房源」和「客户」之间的关联，还增加了「推荐记录」和「跟进记录」两个表。

搞到这种程度，不挑剔的话，其实也能直接用了。只是交互体验像几个表格，不像系统。

![[笔记同步助手/images/97f27dc85f1308ebaba86e92bf547dbe_MD5.jpg]]

进入妙搭，添加项目的 README.md、AGENTS.md，使用专家模式，然后引用之前的多维表格。

![[笔记同步助手/images/8ed75e54d686ca939393aee75c0f0719_MD5.jpg]]

很快，妙搭生成了一份概要设计：

![[笔记同步助手/images/781e3fb51528ae8e07294a708aeaf1c2_MD5.jpg]]

继续生成「开发计划」，之后就开始实现。速度飞快，不过只完成了只读的版本，也没有独立的推荐记录和跟进记录列表。

![[笔记同步助手/images/ec85a06bff96a7eb01df51306cd0b4b8_MD5.jpg]]

跟妙搭聊了两次之后就感觉它的代码能力一般。当然可能也跟这两年大模型的发展以及一直用 Claude Code、Codex 有关，如果是两年前碰到妙搭，估计也会「惊为天人」。

一开始想让 Codex 通过 Chrome 插件指挥浏览器里面的妙搭来修改应用。查看了一下，浏览器里面 Codex 的扩展还在（还是 Connected 状态），Codex 里面的 Chrome 插件却无影无踪了。之前也有这种情况，估计 Chrome 插件又有什么 bug，给雪藏了。

然后尝试让 Codex 用内置浏览器来指挥妙搭。

![[笔记同步助手/images/933cd047b079e2eb86b69c8cfdf1b2f1_MD5.jpg]]

这次跑通了，效率只能说一般，AI 使用 UI 果然还是瓶颈。

眼不见为净，就给 Codex 设置了目标（根据语言，用 /目标 或者 /goal 设置）：一直指导妙搭完成符合我们需求的应用，最后做好 Base 端核验。

这中间再次踩坑。碰到额度限制后，目标就不能恢复执行了，又更新了若干个 Codex 版本才能恢复。

Codex 在执行目标过程中，自我进化，探索出与妙搭交互的最佳实践。内置浏览器只用来做验收，通过命令行来和妙搭沟通修改。具体如下：

-   `lark-cli apps +chat`：把修复需求发给妙搭云端 Agent
-   `lark-cli apps +session-get`：轮询它是否完成、读它改了哪些文件和验证结果
-   内置浏览器：只用来打开预览页做冒烟测试
-   `lark-cli base`：用来核验 Base 表结构和数据

不得不称赞飞书拥抱 cli 的力度，飞书家族的 cli 真的值得再次点赞。

我和 Codex 对妙搭的能力达成了共识。我提醒 Codex 妙搭的能力有欠缺，需求要细一点。Codex 也承认后面必须拆细，不能再一次性喂 Prompt。

![[笔记同步助手/images/aa9745c9b0b05b5594e6e40ffc730643_MD5.jpg]]

回到标题的问题：Codex 指导妙搭，能绽放怎样的火花？

从这次实践来看，核心经验有三条：

1.  **先用 Codex 把需求收敛成规范文档**（README.md + AGENTS.md + 表结构），让妙搭接到的不是模糊的嘴炮，而是明确的指令。
2.  **拆细需求，逐步喂给妙搭**。妙搭一次吃不下太复杂的 Prompt，但拆成小步骤后完成度很高。
3.  **让 Codex 自己探索最佳交互方式**。设定目标后，Codex 自发地从低效的浏览器操作切换到 CLI 交互，效率提升明显。

本质上，这是一种「强 AI 指导弱 AI」的协作范式——Codex 负责架构设计和任务拆解，妙搭负责落地执行。两者各取所长，比单独用任何一个都高效。

往远了想，这种模式不止适用于妙搭。任何「能力尚可但需要精确指令」的低代码平台、自动化工具，都可以用同样的方式接入一个更强的 AI 来当教练。未来的开发方式，可能就是 AI 之间的分工协作，而人类只需要把需求讲清楚。

  

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/67962ea9_1782575730266?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg3ODg0NDA3MQ%3D%3D%26mid%3D2247487418%26idx%3D1%26sn%3D010bda5568a80234ca4120e98b9dfc18%26chksm%3Dce25a17722df78a1e0c2e3cb6d4fbfb65520bce27de4cbf226572469ba154b1cd1936a9f0e59%26mpshare%3D1%26scene%3D1%26srcid%3D0627aeJRhAqSySIludFvmhMI%26sharer_shareinfo%3D476d6ed872739e222245a10028157267%26sharer_shareinfo_first%3D476d6ed872739e222245a10028157267%23rd&s=obsidian)
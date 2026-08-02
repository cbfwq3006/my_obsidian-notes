---
author: 石臻
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247501014&idx=1&sn=5d70e921cb6fc6eae2fe69d47033c1c9&chksm=ce4e95cc0fce7cd82837d2b4a3de3df596e6f1d299fa9658a0e18db90f6928368b3b5dde497e&mpshare=1&scene=1&srcid=0728FAGJVZorcdoyTvpUc7Yi&sharer_shareinfo=6f2e4fb34b6b8257660f081b71dc8be0&sharer_shareinfo_first=6f2e4fb34b6b8257660f081b71dc8be0#rd
saved: 2026-07-28 17:13:10
tags:
  - 笔记同步助手
id: 13337d92-2a77-40b0-a773-b75d6dfe2941
---

公众号名称：石臻说AI

作者名称：石臻

发布时间：2026-06-15 10:43

⭐ 设为星标 · 第一时间收到推送

![[attachments/笔记同步图片/b4ca068192e025fde9c4569c43046ec7_MD5.png]]

石臻说AI 编辑:石臻

> **导读:** 很多人用 AI 写代码,卡住的地方不是模型不够强,而是任务交代得太散:一句"帮我做完这个功能",后面就开始反复补充、纠偏、救火。  
> 这套 \`/goal\` 用法的核心不是偷懒少写几个字,而是把"目标、拆解、验收"交给 Codex 先整理清楚,再让多个 agent 带着各自的目标并行工作。

## 先理解这个用法

过去我们写 prompt,经常会把"需求描述、执行步骤、注意事项、验收标准"揉在一段话里。短任务还好,一旦任务变长,Codex 很容易只抓住最显眼的那部分,后面的约束慢慢就散了。

更稳的做法是先让 Codex 写自己的 `/goal`:把你的意图改写成清晰目标,再列出范围、子任务、风险和验收标准。人给方向,agent 先把方向翻译成任务。

![[attachments/笔记同步图片/00655bef7e4de43281475a060dfce5dc_MD5.gif]]

这和普通 prompt 的区别很大。

普通 prompt 像是"我给你一串指令,你照着做"。这套方法更像是先开一个小型项目会:你说想要什么,Codex 先把任务定义、拆解方式、子任务边界、验收标准写出来,然后再开工。

说白了,`/goal` 不是一句魔法咒语,它更像 agent 的工作协议。

真正有用的不是"让 AI 自己决定一切",而是让 AI 先把你的模糊意图翻译成可执行计划。

## 可复制的 5 步工作流

先看这张流程图。以后你要让 Codex 跑长任务,可以直接按这个顺序来。

![[attachments/笔记同步图片/2c35dfcc67a744d0044962bbe4e04a7b_MD5.png]]

**第一步:你只写"意图",不要急着写完整计划。**

比如你想做一个 Three.js 过山车第一视角 demo,不需要一上来把所有技术细节都安排死。你可以先写清楚最终体验、约束和交付物:

> 💡 PROMPT
> 
> 提示词参考:  
> 我想做一个 Three.js 第一视角过山车 demo。需要有循环轨道、下坠、倾斜转弯、至少一次倒挂、速度感、地形、天空盒和音效。最终交付一个单 HTML 文件。

**第二步:要求 Codex 先给自己写 goal。**

这一步是整个方法的核心。不要直接说"开始做",而是让它先把任务转换成可执行目标。

> 💡 PROMPT
> 
> 提示词参考:  
> For this task, write yourself a new goal first. Turn my request into a concrete objective with scope, constraints, subtasks, and acceptance criteria. Then execute against that goal.

如果你想用中文,也可以这样写:

> 先不要急着实现。请先为你自己写一个新的 /goal:把我的需求改写成清晰目标,列出范围、约束、子任务、验收标准。确认这个 goal 后,再按它执行。

**第三步:如果任务够大,让它派生子 agent。**

这里还有一句很关键:让 Codex 并行 spawn agents,把工作拆成独立片段,每个 agent 都有自己的 dedicated `/goal`。

![[attachments/笔记同步图片/3f15822a20d8d76c7175e52c926a7d87_MD5.jpg]]

你可以把这段加在后面:

> 💡 PROMPT
> 
> 提示词参考:  
> If this benefits from parallel work, spawn agents for independent pieces. Give each agent its own dedicated /goal, make their deliverables explicit, and synthesize the results when they return.

这句话的价值在于,它不是简单说"多线程干活"。它要求每个子 agent 带着自己的任务边界出发:谁负责研究,谁负责实现,谁负责测试,谁负责审查。

**第四步:让主线程负责汇总,而不是让子 agent 互相抢方向。**

并行 agent 最大的坑,是大家都很努力,但最后拼不起来。所以主线程必须保留"总编"角色:收集子结果,判断冲突,合并方案,决定下一步。

你可以明确写一句:

> Keep the main path responsible for coordination. Subagents should return findings or patches, but the main agent must synthesize and make final decisions.

**第五步:要求它把 goal 当作可更新对象。**

长任务最怕跑着跑着目标漂移。一个好用的补充要求是:如果 Codex 发现原目标不完整,可以更新 goal,但必须说明为什么改。

> If the goal needs to change, update it explicitly and explain what changed before continuing.

这会让 agent 少一点"悄悄换题",多一点可追踪的项目感。

## 什么时候适合用,什么时候别用

这套方法特别适合三类任务。

| 场景 | 为什么适合 |
| --- | --- |
| 长代码任务 | 需要持续跟踪目标和验收标准 |
| 多模块改造 | 可以拆给不同 agent 分别研究 |
| 探索型项目 | 先让 agent 把不确定性梳理出来 |

不适合的场景也很明确:小修小补、单文件改一行、你已经有非常精确的实现方案。这时候再让 Codex 写 goal,反而会多一层仪式感。

![[attachments/笔记同步图片/73d31fbb28f91ed24f7a31cfd1d48862_MD5.jpg]]

我的经验是:只要任务会超过 20 分钟,或者你预感中途要反复补充需求,就值得先让 Codex 写 goal。

这一步看起来慢,其实是在省后面的返工。

### 一套可以直接粘贴的模板

下面这段可以直接收藏。以后你把第一段任务描述换掉,后面的结构基本不用动。

> 💡 PROMPT
> 
> 通用模板:  
> I want to accomplish the following task:  
> \[在这里写你的真实需求\]  
> Before implementing, write yourself a new /goal. Turn my intent into a concrete objective with scope, constraints, subtasks, risks, and acceptance criteria.  
> If the work can be parallelized, spawn agents for independent pieces. Give each agent its own dedicated /goal and explicit deliverable.  
> Keep the main path responsible for coordination and final synthesis. If the goal needs to change, update it explicitly and explain why before continuing.

如果你是做代码任务,我建议再补三条:

> Read the existing codebase first and follow local patterns.

> Do not make unrelated refactors.

> Verify the result with the most relevant tests or checks before finishing.

这三条很朴素,但很管用。它们把 agent 从"自由发挥"拉回到工程现场。

如果你想全程用中文,也可以用这个版本:

> 💡 PROMPT
> 
> 中文模板:  
> 我想完成下面这个任务:  
> \[在这里写你的真实需求\]  
> 开始实现前,请先为你自己写一个新的 /goal。把我的意图整理成具体目标,明确范围、约束、子任务、风险和验收标准。  
> 如果这个任务适合并行,请为相互独立的部分派生 agents。每个 agent 都要有自己的 dedicated /goal,并说明它需要交付什么。  
> 主线程负责协调和最终汇总。如果执行过程中需要修改 goal,请先明确说明改了什么、为什么改,再继续执行。

### 最后说句实话

`/goal` 这类能力会让 agent 更像一个能维护上下文的合作者,但它不会自动替你想清楚产品判断。

你仍然要负责意图:要做什么、为什么做、哪些东西不能碰、结果怎么算完成。

Codex 负责把这些意图整理成工作目标,再把目标拆给合适的执行单元。人的角色不是消失,而是从"逐字写指令"变成"定义方向和验收"。

可以把这套方法记成一句话:不要只让 Codex 干活,先让它写清楚自己要怎么干活。任务越长、越复杂,\`/goal\` 的收益越明显。

> 📚 往期精选

> [微软开源 Webwright:把点击操作变成可重复执行的脚本](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247500853&idx=1&sn=237983234382ea37d15c4a8490f84116&chksm=cff55e3ef882d728b4a38cc11fceaa9e2b41a1143ebf51c23c8b0fa21da4ebe1f2717074f74f&scene=21#wechat_redirect)

> [这Github上9.3k人点赞的插件让Hermes更聪明](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247500752&idx=1&sn=61b95a0b6be0b4b182506a0f2b700b45&chksm=cff559dbf882d0cdc1481e46628012418be5128853512c1452fb1dd343e7912df8470c0272a2&scene=21#wechat_redirect)

> [AI记忆的主权之争: 别把AI记忆交给大厂](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247500267&idx=1&sn=490c30d5b0852b5afdf1137c531d9369&chksm=cff55be0f882d2f677cebc38f3c4fc3e40db95f3cc376a8ba7988bb60dcba0b8591a20e547e7&scene=21#wechat_redirect)

> [小白扫盲!AI Agent 入门指南:用最直白的方式,把这个概念彻底讲清楚](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247500170&idx=1&sn=c5689589ca40ceefb87ec75292652429&chksm=cff55b81f882d29742cc8b93c269e3b147635cd59c9f0f6da41570f0feedd01460a2b1771159&scene=21#wechat_redirect)

> [小白扫盲!OpenClaw、Claude Code、Agent、MCP……9个AI概念一次搞懂](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247499863&idx=1&sn=f14716e6f66d610175dc75707a7490c3&chksm=cff55a5cf882d34a4f1432ff33ed21d8f295fe07a0e2b2d73b2b33860ebebee7de55047c762b&scene=21#wechat_redirect)

> [你一直在忽略Claude Code最强大的功能: .claude/ 文件夹拆解](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247499855&idx=1&sn=db98be0e462874618a7a8368e92b613a&chksm=cff55a44f882d3524af217d5159f31f7bf2014d1ad0b36a0e44e5ee1889d39462504e6abca43&scene=21#wechat_redirect)

> [OpenClaw 大更新:插件市场上线,/btw 侧边提问,AI agent 从工具变成了平台](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247499750&idx=1&sn=29714d8b7c8f8a5571d929dd84a70246&chksm=cff565edf882ecfb087fc4e1ccc4bf349519d0039ae9ac1823c05df2be584f42c7fdab3d97e7&scene=21#wechat_redirect)

> [Anthropic 的 Claude 架构师认证考试,有人把它拆碎了免费给你](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247499551&idx=1&sn=4491b6e855eeec7aededaa9ae5d3e74d&chksm=cff56514f882ec0279f491e507790cc72ed2d16950ccde8d50d2ffdc62796b78ff0227065d32&scene=21#wechat_redirect)

> [Claude skill-creator重磅更新,给你的AgentSkill装上单元测试](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247498849&idx=1&sn=57e163a2dd06b4b7ff3afe20b2f69a5a&chksm=cff5666af882ef7c17e669817a8968210b602636ef64e552507f8f01ba3b0b2f4a01ef617faa&scene=21#wechat_redirect)

> [突发!美国政府禁止外国国民使用Fable5](http://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247500999&idx=1&sn=1bd92e5bc2beb1a93230cb3cf4b36b7c&chksm=cff55eccf882d7da8e92a4d22fe7335e251766acd1f4cb59b58bae071011e791a58c70cca107&scene=21#wechat_redirect)

— **完** —

---

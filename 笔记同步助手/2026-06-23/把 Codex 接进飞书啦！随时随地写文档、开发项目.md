---
author: K姐Koi
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkxNDczMjA4Ng==&mid=2247507285&idx=1&sn=28a3091733049f2c125b7173ab0b7a8c&chksm=c06de0f1d8e3142c308421db46c5bc46e857dbf138a3db6a429684ab02530f1c36f397f426ae&mpshare=1&scene=1&srcid=0623JrfaWZF6ZHtoevC0dqod&sharer_shareinfo=3e610be02bdd5a87d857d5b7648531d0&sharer_shareinfo_first=3e610be02bdd5a87d857d5b7648531d0#rd
saved: 2026-06-23 06:21:17
tags:
  - 笔记同步助手
id: eff41b8a-a1dd-48b7-a469-4ba8802ae1a8
---

公众号名称：K姐研究社

作者名称：K姐Koi

发布时间：2026-06-06 09:14

![[笔记同步助手/images/aaead0798424dca3ca6d2792dc123f18_MD5.png]]

**大家好，这里是K姐。**

**一个帮助你把AI真正用起来的女子。**

前几天刷到了博主@张咋啦Zara 把 Claude Code 接入飞书，可以像跟同事对话一样，用手机让 Claude Code 处理工作内容。

我们平时大部分工作沟通、沉淀都在飞书上，这样确实能省不少事。

![[笔记同步助手/images/a28eddd2b07f9094fc0b972ac23fe7fc_MD5.png]]

不过，我日常处理文件、梳理灵感用得更多的是 Codex，借着@张咋啦Zara 推荐的桥接工具，我把 Codex 也接到了飞书里。

出门在外脑子里突然闪现灵感，在手机飞书上发条消息，Codex 立刻就能帮我理出个方案框架。看不懂的业务报表，随手截个图发过去，Codex 能直接带图分析。

<上下滑动查看全部内容>

下面把我摸索出来的接入步骤和实测效果分享给大家，跟着做几分钟就能搞定。

![[笔记同步助手/images/241ee8085388c9a360cd9e95575b9c53_MD5.png]]

**连接教程**

开始前我们需要确保 Codex 是可运行，如果我们有Code 需求，还需要在 VS Code 里安装 ChatGPT / Codex 的扩展。

这次我们要用到的 Bridge 是 Codex Remote Feishu。

## GitHub：https://github.com/kxn/codex-remote-feishu

macOS / Linux 直接运行：

```
curl -fsSL https://raw.githubusercontent.com/kxn/codex-remote-feishu/master/install-release.sh | bash
```

Windows PowerShell 运行：

```
irm https://raw.githubusercontent.com/kxn/codex-remote-feishu/master/install-release.ps1 | iex
```

![[笔记同步助手/images/247fd23bbe89deca99f0a135ff01a0f8_MD5.png]]

脚本运行后会在浏览器打开一个Codex Remote Feishu v1.8.4 安装程序。

![[笔记同步助手/images/c30473e67454eec8146a8da0915a2b66_MD5.png]]

跟着这个安装程序一步步走就行，环境检测成功后，就可以扫码在飞书创建应用了，点击立即创建即可。

![[笔记同步助手/images/d8a6b3b0959a4d7bc740ffb92d2809fd_MD5.png]]

如果有缺失的权限，直接把给出的代码复制，然后点击跳转到飞书后台权限设置界面。

![[笔记同步助手/images/46475297f5b99a01d6edf6422daa7ced_MD5.png]]

点击批量导入/导出权限，把刚才复制的东西填进去，然后点击新增权限即可。

![[笔记同步助手/images/24a403222e665a607b750f5412d70694_MD5.png]]

![[笔记同步助手/images/8c58742012865f83d6ce9aba55100865_MD5.png]]

接下来它会让机器人尝试发送事件订阅测试，一般都没问题，如果不通过，大家去飞书后台配置一下就好。

![[笔记同步助手/images/c8bebe4b516d0d6a1069d465e273ad5c_MD5.png]]

接下来是回调测试，一般也不会有问题。

![[笔记同步助手/images/33a6c045854c9eddab6d5fc4647275cd_MD5.png]]

接下来是机器人配置，大家点击进入飞书后台配置即可，如果不配置的话，所有东西都需要靠手敲 / 命令来实现，手机上很不方便。

我这里就只先设置了一个stop命令，大家还想要其他的一键命令可以自己多设置几个。

![[笔记同步助手/images/4362f1ea13f6d936e510d49aaa8e4eec_MD5.png]]

![[笔记同步助手/images/fed5d5c039ceccf9c95609af0464b1d3_MD5.png]]

自动启动不用管，检测通过后，就会进入 VS Code 集成，如果没有这个需求的直接点击先不使用按钮即可跳过。

![[笔记同步助手/images/79169958310f437c0b38343ac6198f8f_MD5.png]]

接入完成后，我们发布机器人的新版本，就可以在飞书里使用了。

下面两个设置，以大家的使用情况来勾选。

![[笔记同步助手/images/bad3ad5e23d4b67d5e38475d07afa4ee_MD5.png]]

![[笔记同步助手/images/6085c2578db445085a42a0a6389bdc49_MD5.png]]

**实测体验**

开始任务之前我们要先选择我们的工作区（就是选择在哪个项目下面进行对话），输入/list 即可进入选择界面。

![[笔记同步助手/images/5be6bcad9b6ad5d9007de380c36aa46a_MD5.png]]

-   **case1 用手机新建文档**
    

出门在外，工作也不会落下，手机遥控 Codex 帮我新建文档，然后开工：

> 提示词：帮我在这个项目下新建一个文件夹，名字叫做手机办公。

![[笔记同步助手/images/14be631e9a98a02490e2e26497bb2a74_MD5.png]]

30 秒就帮我们建好了文件夹，在外用手机也能上班了，真开心！什么牛马发言！

-   **case2 信息文档**
    

平时需要做一些信息收集也可以让它帮我们做，再调用飞书官方 CLI 工具 lark cli 帮我们生成云文档，把信息储存下来：

> 提示词：收集最近 30 天 AI 相关的福利资讯，从中选 10 个你认为最好的福利，调用 lark cli 这个工具创建一个飞书文档，叫福利收集，把福利信息放到里面。

![[笔记同步助手/images/32399dc490ca583b48edf12478c4e6fa_MD5.png]]

Codex 自己收集信息，调用工具，创建飞书云文档也就花了 18 分钟。

<上下滑动查看全部内容>

做的文档很满足我的要求，10 个福利都很详细，包括如何领取，时限啥的都有。

-   **case3 做 PPT**
    

以前做 PPT 还要自己慢慢敲字，慢慢收集信息，现在定好主题和要求，在飞书里直接丢给 Codex 就好：

> 提示词：在当前这个 PPT 云文档里，使用已有的模板风格，搜集必要信息，改成一版介绍 Codex 的 PPT。
> 
> ![[笔记同步助手/images/2b06163d292be304a04f06011f9ae223_MD5.png]]

整个风格和我给它的差不多，20 页左右的 PPT 全部都改完也就花了半小时，工作效率还是很不错的，做出来的效果也很好。

![[笔记同步助手/images/93c040456756cf93e78b8274fa4031a5_MD5.jpg]]

> 📹 此处为视频内容（vid: wxv\_4547896047456681991）（上图为封面），未能直接提取，请前往原文查看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzkxNDczMjA4Ng==&mid=2247507285&idx=1&sn=28a3091733049f2c125b7173ab0b7a8c&chksm=c06de0f1d8e3142c308421db46c5bc46e857dbf138a3db6a429684ab02530f1c36f397f426ae&mpshare=1&scene=1&srcid=0623JrfaWZF6ZHtoevC0dqod&sharer_shareinfo=3e610be02bdd5a87d857d5b7648531d0&sharer_shareinfo_first=3e610be02bdd5a87d857d5b7648531d0#rd)

-   **case4 生成网页**
    

让 Codex 帮我们跑一次选题实测：

> 提示词：运行我的选题 skill，把结果做成一个 html 文件放在这个文件夹里。

![[笔记同步助手/images/6b9cf7fc47e4d34c7ac58b292d417518_MD5.png]]

根本不用坐在电脑面，也能把活干了，出来的效果还很好，非常方便且高效。

<上下滑动查看全部内容>

-   **case5 前端设计**
    

用 Codex 的时候能感觉到，它做前端相对弱一些，但是我们先让 Codex 生成一张图，再照着图做前端，就能出来很好的效果：

> 提示词：用 Image-2 生成 3 张后台数据看板的视觉稿。要求偏专业 SaaS，信息密度高，颜色克制，有清晰导航、指标卡、趋势图和任务列表。

![[笔记同步助手/images/b8e25d7162c4c410b50ebed9990f400b_MD5.png]]

拿到图之后，再挑一张继续说：

> 提示词：按这张图的视觉方向，实现一个 React + Tailwind 的前端页面。不要照抄图片细节，重点复刻信息层级、布局节奏和颜色气质。

<上下滑动查看全部内容>

我还在外面逛街他就把结果发给我看了，手机工作太爽了！

![[笔记同步助手/images/869dcf62714c8ce71c941f7cec32c764_MD5.png]]

结果也很好，以前 Codex 写页面，容易从组件和布局开始推，出来就很简单，很难看。

现在给它一张图，有了审美锚点，出来的效果就好多了。

或许有友友问，如果我每天都在电脑前写代码，可能第一感觉是：我直接用 Codex 不就行了？

但只要我们遇到这些场景，飞书接入就很有价值：

经常用手机处理工作消息。

希望不打开电脑也能继续推进项目。

想把截图、文件、进度都放在飞书里协作。

已经把飞书当成团队工作入口。

![[笔记同步助手/images/3a6ab83015c4cdcb441d2ec79fdb9c00_MD5.png]]

**一些分享**

目前我在 Codex 里调用的模型主要是 GPT-5.5，强确实是强，但高强度使用需要上 Pro 套餐，一个月折合人民币得要上千块，对于绝大部分个人来说还是挺贵的。

其实我们日常办公 90% 的场景发挥不出 GPT-5.5 的全部实力，如果切换到国产模型，1/10 的价格，就能实现 90% 顶尖模型的能力，这个性价比对大多数人来说都非常划算。

但光有高性价比的模型是不够的。

Codex 和飞书打通彻底改变了我的工作方式，让我理解了更重要的是要有能够发挥出 120% 模型能力的顶级产品应用，只有把 AI 揉进每天的工作细节里，构建起新的人机协同工作流，技术才算真正落了地。

作者：yuye&K姐

投稿邮箱：tougao@kseek.ai

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/e2d7c00b_1782166875856?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzkxNDczMjA4Ng%3D%3D%26mid%3D2247507285%26idx%3D1%26sn%3D28a3091733049f2c125b7173ab0b7a8c%26chksm%3Dc06de0f1d8e3142c308421db46c5bc46e857dbf138a3db6a429684ab02530f1c36f397f426ae%26mpshare%3D1%26scene%3D1%26srcid%3D0623JrfaWZF6ZHtoevC0dqod%26sharer_shareinfo%3D3e610be02bdd5a87d857d5b7648531d0%26sharer_shareinfo_first%3D3e610be02bdd5a87d857d5b7648531d0%23rd&s=obsidian)
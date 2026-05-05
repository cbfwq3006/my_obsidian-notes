---
author: 林大友
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489510&idx=1&sn=1758a48c5a2671579c88f5a54059a3d6&chksm=c50d99dcccf486470795d0928e3863142ee70755bc6a2784c00f8ea46767b48f18bf9c036d3e&mpshare=1&scene=1&srcid=0505hd2UQ51cbWoQgGly2wi4&sharer_shareinfo=9071c31f2ec9be7e9c3891689ed8f7f2&sharer_shareinfo_first=9071c31f2ec9be7e9c3891689ed8f7f2#rd
saved: 2026-05-05 19:36:32
tags:
  - 笔记同步助手
id: 89dbb6e3-67fe-4631-8333-4be8afb83b90
---

公众号名称：林小卫很行

作者名称：林大友

发布时间：2026-04-17 08:09

原文链接：[https://xiaoweibox.top](https://xiaoweibox.top)

> 这是一个「Obsidian × AI」系列。
> 
> 我会从最基础的认知开始，慢慢写到资料整理、写作工作流，再到怎么把 AI 接进来。
> 
> 如果你还没看过前几篇，可以先看 [Obsidian 入门25：认识 Templater插件，让笔记自己长出结构](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489471&idx=1&sn=a6320badc3225fcb33f528ade2f3fb7d&scene=21#wechat_redirect)

---

学完 Obsidian 基础之后，你可能会想：能不能让 AI 帮我处理这些笔记？

这个问题听起来不复杂，但实际操作的时候，你会发现网上动不动就出现“命令行”、“IDE”、“MCP”这些词。好像这些都是程序员的专属工具。

这篇文章就是来解决这个门槛的。只讲四件事：**它们到底是什么，你日常生活中其实已经在用类似的思维**。

---

## 能打开整个文件夹的超级记事本（IDE）

你平时在电脑上写文字，用的是 Word 或者 Pages。你打开一个文件，编辑，保存。

IDE 的全称是 Integrated Development Environment，集成开发环境。它不只能打开一个文件，还能打开一整个文件夹，理解这个文件夹里所有文件之间的关系。

你可以把它理解成一个**能读懂整个文件夹内容的记事本**。

我第一次用这个思路做事，是因为想用 AI 读懂我几年的日记。试过直接把日记拖进 Gemini，它限制 10 个附件，失败了。试过 Obsidian 的 Copilot 插件，它只能看懂当前正在看的那一篇，不知道库里还有什么。

![[笔记同步助手/images/93e419ccbe9e08f11775cfff1be8599e_MD5.png]]

直到我把整个日记库拖进一个 IDE，它居然能回答“我这几个月在焦虑什么”。

这就是 IDE 的本事。

**免费的选择，VSCode**

很多人知道 Cursor，但 Cursor 的高级功能需要订阅。其实有一个完全免费的选择：VSCode，Visual Studio Code（当然如果要用上 AI 的能力，都是需要花钱的）。

VSCode 同样能做到把整个文件夹拖进去，让 AI 读懂里面的内容。操作方式和 Cursor 完全一样，拖进去，输入提示词，敲回车。

![[笔记同步助手/images/ea9efae70237673b487ba5bbfc253de3_MD5.png]]

---

## 用文字跟电脑说话（CLI）

说完 IDE，再说说 CLI。

CLI 的全称是 Command-Line Interface，命令行界面。它是另一种跟电脑说话的方式，你直接用文字下指令，电脑执行，不用点图标或按按钮。

![[笔记同步助手/images/45eb860d938e96b033b30ff389e278bd_MD5.png]]

### 两种跟电脑说话的方式

GUI，Graphical User Interface，图形界面。你点图标、拖文件、按按钮。电脑在幕后把你每一个操作翻译成它能听懂的语言。这是大多数人每天在用的方式。

CLI，你直接发指令给电脑的“后台”。省掉了图形界面这个中间层，直接跟执行者说话。

### 你每天都在用 CLI

你有没有在 Obsidian 里按 Cmd+P，然后输入 `>` 调出命令面板？那个输入框本质上就是一个 CLI 入口。你输 `> 新建笔记`，Obsidian 收到这条指令，帮你创建一篇日记。只是 Obsidian 把界面做得很漂亮，让你感觉不到你在“写代码”。

**一个生活里的比喻**

GUI 就像去自助餐，你看着菜单点菜，有图片有介绍，你不需要知道厨房里发生了什么。

CLI 就像你直接进厨房跟厨师说，“我要一份番茄炒蛋，蛋要嫩一点。”省掉了菜单这个中间环节，直接跟执行者说话，效率更高。

![[笔记同步助手/images/4b3a9043347982cde6f6c853c6df6751_MD5.png]]

Caude code, Codex, Gemini CLI 等就是把这个功能单独抽出来：你在终端里直接给 Claude/chatGPT/Gemini 发消息，它直接回答你。

---

## 让 AI 记住怎么做事的食谱卡（Skill）

现在你知道了 IDE 和 CLI。最后还有一件事，我们后面会一直用到。

Skill 没有一个官方的标准全称，你可以理解它为**一套可复用的指令模板**。

### 番茄炒蛋的食谱卡

你学会做番茄炒蛋之后，你不需要每次重新想“先放油还是先放蛋”，你有一张食谱卡，照着做就行。

Skill 就是给 AI 留的一张食谱卡。

没有 Skill 的时候，你每次让 AI 帮你做周记，都得先把背景重新说一遍，“我每天写日记，格式是这样的，你需要先读当周的日记，然后总结三个要点。”AI 每次都是从零开始。

有了 Skill，你把这段话提前写好，告诉 AI，“记住，这就是你每次帮我做周记的方式。”AI 照着做，不用你每次重复。

我们后面会专门讲 Skill。现在只需要知道一件事，**它是一张食谱卡，让 AI 不用每次重新学怎么做一道菜**。

---

## 让 AI 真正操控电脑的转换头（MCP）

最后简单提一句 MCP。

MCP 的全称是 Model Context Protocol，模型上下文协议。它是一种让 AI 能真正调用外部工具的协议。

你有没有遇到过这种情况，你有一台打印机，有一台电脑，它们没法连接，因为接口对不上？

MCP 就是那个“转换头”。有了它，AI 不只能跟你说话，还能去读你的文件夹，帮你发一封邮件，查一下今天的天气。

![[笔记同步助手/images/5cf75889d39a474fc24a348ebd8525a1_MD5.png]]

这篇不展开，后面专门讲。你现在只需要知道一件事，MCP 让 AI 从“回答问题”变成“真正帮你做事”。

---

## 结尾

四个概念搞懂之后，我们下一期就可以正式开始用 AI 处理你的笔记了。

感谢关注，下期见！

---

## 进阶阅读

-   [Obsidian 入门25：认识 Templater插件，让笔记自己长出结构](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247489471&idx=1&sn=a6320badc3225fcb33f528ade2f3fb7d&scene=21#wechat_redirect)
    
-   [我的AI工作流：Obsidian日记库 → Cursor侧写 → Gemini上下文](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247483868&idx=1&sn=99e6e3d3ecaccb0171a6df9ce351b585&scene=21#wechat_redirect)
    
-   [保姆级教程：将 Gemini CLI和Claude code集成到 Obsidian](https://mp.weixin.qq.com/s?__biz=Mzk2NDAwMzAzMw==&mid=2247485994&idx=1&sn=65c2efa26a21907a43ba57634e7cdfea&scene=21#wechat_redirect)
    

  

对了，我建了一个Obsidian 交流群，如果在使用过程中碰到了问题，欢迎加入来一起交流呀

![[笔记同步助手/images/9734431db00d1dc34ac086eae43e9428_MD5.jpg]]

---

![[笔记同步助手/images/598122f59d81014208fe298221a2c249_MD5.jpg|cover_image]]

Original 林大友 林小卫很行

Read more
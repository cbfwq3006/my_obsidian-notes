---
author: Benson
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzk0Mjc1NjM3Ng==&mid=2247483773&idx=1&sn=fe2c73665a24b2a160458af3f46d1e17&chksm=c2327edf62afc4a1322df1283cafa9986b82d6eeaeb871f461d1fefe3ce8acdc1ba8b20d6b9e&mpshare=1&scene=1&srcid=0707LAqtCy784dNNeJ9x6KkV&sharer_shareinfo=0c7c1cabd715a39cc788870fe8efb4bb&sharer_shareinfo_first=0c7c1cabd715a39cc788870fe8efb4bb#rd
saved: 2026-07-07 21:28:59
tags:
  - 笔记同步助手
id: 4b0af34c-d4e1-4c8d-9771-f183a8e0c77c
---

公众号名称：清平曰

作者名称：Benson

发布时间：2026-07-07 00:43

**Agents Anywhere：用手机控制编程Agent**

> 最近用 Codex、Claude Code 写代码，很容易碰到一个小尴尬：  
> Agent 确实越来越能干活了，但人还是经常被绑在电脑前。  
> 你在 Mac 上开了一个 Codex 任务，它开始读代码、改文件、跑命令。任务还没结束，你要出门。  
> 你在公司 Windows 电脑上跑 Claude Code，想回家之后继续看进度。  
> 或者你有一台 Linux devbox，Agent 在上面跑得好好的，但每次想看一眼，都要 SSH 上去。  
> 明明是 AI 在替你写代码，最后人还是像值班一样守着设备。

**项目介绍**

最近看到一个开源项目，正好在解决这个问题：  

Agents Anywhere

  
GitHub：  
https://github.com/anywhere-labs/Agents-Anywhere  
一句话介绍：

> 用手机控制任何设备上的编程 Agent。

**先看效果**

你可以把 Agents Anywhere 理解成一个“手机里的 Agent 控制台”。  
Codex、Claude Code 继续运行在原来的电脑、服务器或 devbox 上；你人在外面，用手机查看进度、继续发指令、看文件、开终端。

![[笔记同步助手/images/48ba19e6f69617d9cd72c099939b38e5_MD5.png]]

这张图左边是手机上的 Session 列表，可以看到不同任务和对应设备；右边是某个 Agent Session 的对话界面，可以继续给正在运行的 Agent 发消息。

> 比如早上你在电脑上开了一个任务，让 Codex 改一个功能。  
> 任务还在跑，你人出门了。  
> 以前你要么等回去再看，要么远程桌面，要么 SSH，要么干脆先放着。  
> 现在可以直接在手机上打开 Agents Anywhere，看它改到哪一步，补一句需求，或者让它继续往下做。  
> 电脑继续在家里写代码。  
> 你人在外面，用手机指挥它。

**不只是聊天，还能看文件和终端**

如果只是把 Agent 对话搬到手机上，其实还不够。  
写代码这件事，不只是“发一句话，然后等回复”。  
真实工作流里，你经常需要看文件、查日志、跑测试、进终端。  
Agents Anywhere 把这些能力也放进来了。

![[笔记同步助手/images/4a3c94ddda3ddb7f2b7a333a00ed51f5_MD5.png]]

-   你可以在手机上查看远程设备里的项目文件，预览代码内容。
    
-   如果想确认某个改动，可以直接打开对应文件看。
    
-   它也支持远程 Terminal。
    

比如你想看测试有没有过，或者想检查一段日志，不一定非要打开电脑。  
手机上就能进入那台设备的 terminal，看命令输出，必要时继续执行命令。

> 这就比单纯的“手机聊天框”更完整一些。  
> Agent 在那台机器上写代码，你在手机上看 Session、看文件、看终端。

**Web 端也能当控制台**

手机不是唯一入口。  
如果你人就在电脑前，或者团队希望通过浏览器管理设备和 Session，也可以直接用 Web 控制台。

![[笔记同步助手/images/969a79dce80c48b20675d727344eeddd_MD5.png]]

Web 端可以看到设备、Session、文件面板和 Shell 面板。

> 也就是说，Agents Anywhere 不是单纯做一个移动端 App，而是在做一个跨设备的控制面：  
> 手机上随时接管任务。  
> 浏览器里完整管理设备和 Session。  
> 远程设备上由 Connector 连接本地 Agent 和工作区。

**核心概念与架构**

**统一管理所有设备**

Agents Anywhere 里有一个重要概念：  

Device

-   你的 Mac 是一个 Device。
    
-   Windows 电脑是一个 Device。
    
-   Linux 服务器、远程 devbox、云沙箱，也都可以是 Device。
    

每台 Device 上，又可以运行不同的 Agent。  
目前项目已经支持 Codex 和 Claude Code。  
后续开发计划里，还会继续接入更多 Agent，比如 OpenClaw 以及其他编程 Agent Runtime。

> 所以它想做的不是某一个 Agent 的移动端，而是一个统一入口。  
> 你打开手机，看到的不只是一个工具，而是：  
> 哪台设备在线。  
> 哪台设备上有哪些 Agent。  
> 哪些 Session 正在跑。  
> 哪个任务可以继续接管。  
> 文件、终端、代码上下文在哪里。

如果未来你本机跑 Codex，服务器上跑 Claude Code，另一台 devbox 上跑 OpenClaw，那每个工具各开一个入口就会很乱。  
Agents Anywhere 想补的，就是这一层统一控制面。

**它到底是怎么工作的**

Agents Anywhere 主要由三部分组成：

-   Client
    

你直接使用的入口，包括 Web 控制台和移动端 App。你在这里查看设备、进入会话、发送指令、查看文件和终端。

-   Server
    

中间服务，负责账号、设备、Session 状态、命令路由，以及 Client 和 Connector 之间的通信。

-   Connector
    

跑在被控制的设备上，比如你的 Mac、Windows PC、Linux server 或 devbox。  
它负责连接本地的 Codex / Claude Code runtime，并在本机执行实际任务。  
简单说，链路是：

> 手机 / Web -> Server -> 受控设备上的 Connector -> 本地 Codex / Claude Code -> 本地代码、文件、终端

> 关键点在这里：  
> 你的代码、终端和 Agent runtime 都留在受控设备上。  
> Agents Anywhere 提供的是控制入口和路由能力，不是把你的代码搬到别的地方重新运行。  
> 手机只是控制器。  
> 真正干活的，还是你自己的电脑、服务器或 devbox。

**适用场景**

**什么场景会很爽**

第一种，是你有一台常开的开发机。  
比如家里的 Mac mini、办公室电脑，或者一台专门跑开发任务的机器。你可以让 Codex / Claude Code 在那台机器上跑任务，然后人在外面用手机看进度、补需求、接着指挥。  
第二种，是你有 Linux 服务器或远程 devbox。  
以前你可能是 SSH 上去开 tmux，让 Agent 在里面跑。能用，但手机上看起来并不舒服，操作也不适合频繁交互。  
Agents Anywhere 的思路，是把这个过程产品化：Session、文件、终端、设备状态，都放到一个控制面里。  
第三种，是你同时使用多个 Agent。  
今天用 Codex，明天用 Claude Code，后面可能还会用 OpenClaw 或其他 Agent Runtime。  
如果这些 Agent 都能被接入同一个控制面，你就不用记住每个工具、每台机器、每个远程入口分别在哪里。  
打开 Agents Anywhere 就行。

**与官方手机端的区别**

**和官方手机端有什么区别？**

这里可能会有人问：

> Codex、Claude Code 自己不是也有手机端吗？

确实，如果你只想在手机上使用某一个官方产品，而且下载、账号、网络环境都很顺，官方手机端能解决一部分问题。  
但 Agents Anywhere 的重点不太一样。

-   第一，它做的是统一控制面。
    

你控制的不是“一个 App 里的一个 Agent”，而是很多台 Device，以及这些 Device 上正在运行的不同 Agent。  
比如你的 Mac 上跑 Codex，公司电脑上跑 Claude Code，Linux devbox 上以后跑 OpenClaw。  
这些设备和 Agent，都可以被接到同一个入口里。  
对需要管理多台设备、多条 Session、多种 Agent 的人来说，这会比每个工具各开一个入口清楚很多。

-   第二，对国内用户更友好一些。
    

很多官方手机端在国内安装会比较麻烦。  
Android 往往依赖 Google Play 相关服务。  
iOS 也不是只有网络环境就够了，很多时候还需要外区 Apple ID，切到海外 App Store 才能下载。  
Agents Anywhere 这边，Android 可以直接到 GitHub Releases 下载 APK 安装。  
iOS 目前还没正式上线 App Store，按当前计划会同时在国区和外区 App Store 上线，预计大概 1-2 周，具体以 App Store 审核和实际上线时间为准。

> 还有一个实际使用上的点：  
> 手机端本身不需要开代理也能用。  
> 因为手机端到 service，再从 service 到 Connector App，这条控制链路可以走国内环境。  
> 你只需要保证真正运行 Agent 的那台 Device 自己能正常访问它需要的模型和服务。  
> 手机只负责控制。

-   第三，中转站友好。
    

如果你本地的 Codex / Claude Code 是通过配置文件接到国内中转站，Agents Anywhere 也可以继续沿用这套本地 Runtime。  
本地 Codex / Claude Code 怎么连模型，是由那台 Device 自己的配置决定的。  
你可以用官方 API，也可以按自己的环境配置中转服务。  
但官方手机端通常走的是官方自己的产品链路。  
如果你的工作流依赖本地配置、企业网关、国内中转站，或者团队内部的模型路由，官方移动端不一定能直接复用。

> Agents Anywhere 的优势就在这里：  
> 它不强行改变你本地 Agent 的连接方式，只是把控制入口搬到手机和 Web 上。

**安全与部署**

**代码和会话安全吗？**

这是一个很重要的问题。  
Agents Anywhere 的工作流里，Client、Server 和 Connector App 之间需要同步会话状态、命令和部分上下文信息。  
也就是说，如果你使用官方线上服务，代码内容、终端输出和 Agent session 信息可能会经过服务端转发。

> 如果你对代码安全、隐私或公司内部项目比较敏感，更推荐使用自部署版本。

Agents Anywhere 从一开始就支持自部署。  
你可以自己部署一套 Server，只给自己或自己的团队使用。  
这样代码、会话和设备连接都在你自己控制的服务里，不依赖官方线上服务。  
自部署场景也支持比较完整的子账号管理。  
比如你可以给自己的 team 部署一套，让团队成员分别登录、管理设备、控制各自的 Agent session，用在内部开发环境或私有服务器上。

-   个人尝鲜：可以申请官方 beta 服务。
    
-   代码敏感：建议自部署。
    
-   团队使用：可以自部署一套给自己的 team。
    
-   企业或内部项目：推荐私有化部署。
    

**写在最后**

Agents Anywhere 已经开源。  
如果你正在用 Codex、Claude Code，或者有自己的 Mac、Windows 电脑、Linux 服务器、远程 devbox，想试试用手机接管这些设备上的编程 Agent，可以直接来 GitHub 看看：  
https://github.com/anywhere-labs/Agents-Anywhere  
如果你想申请内测，可以进入github首页找到内测入口

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/7652caf9_1783430937357?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzk0Mjc1NjM3Ng%3D%3D%26mid%3D2247483773%26idx%3D1%26sn%3Dfe2c73665a24b2a160458af3f46d1e17%26chksm%3Dc2327edf62afc4a1322df1283cafa9986b82d6eeaeb871f461d1fefe3ce8acdc1ba8b20d6b9e%26mpshare%3D1%26scene%3D1%26srcid%3D0707LAqtCy784dNNeJ9x6KkV%26sharer_shareinfo%3D0c7c1cabd715a39cc788870fe8efb4bb%26sharer_shareinfo_first%3D0c7c1cabd715a39cc788870fe8efb4bb%23rd&s=obsidian)
---
author: 老 K
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg==&mid=2247493753&idx=1&sn=3a43524ee1134d2a218189a285465aab&chksm=c03905e432c0f777906f7d98eb54002eb206c66f84ccf798a141a05e21395c7df2929115777d&mpshare=1&scene=1&srcid=07105yUxt8bU1bJe7yoRzzZ4&sharer_shareinfo=7451dc7e214e8255721b74f722567c3c&sharer_shareinfo_first=7451dc7e214e8255721b74f722567c3c#rd
saved: 2026-07-10 07:48:21
tags:
  - 笔记同步助手
id: b929de6c-2425-479b-8a0b-2eb7a22223e9
---

公众号名称：老码小张
作者名称：老 K
发布时间：2026-06-27 22:27

![[attachments/笔记同步图片/4eda03c25e5e86776d5d7ce7112345d8_MD5.png]]
![[attachments/笔记同步图片/e33dc927500b536f7c5574e61485341f_MD5.png]]
![[attachments/笔记同步图片/a04c76b7356dfff85b026aef86755275_MD5.png]]
![[attachments/笔记同步图片/96e052ade1050cfbdd1d7ecf9278efa0_MD5.png]]
![[attachments/笔记同步图片/950b753a9dbc91300366a9bb63da5f42_MD5.png]]
![[attachments/笔记同步图片/b2aa16e4dfc3a4d8c987a75c44552215_MD5.png]]
![[attachments/笔记同步图片/ea626bf97208de52bd127eec5ae08dc3_MD5.png]]
![[attachments/笔记同步图片/ce4ea6c4536f2df1c6ed76348e872d57_MD5.png]]
![[attachments/笔记同步图片/bd48355755e7913e9bfabb35a34b51c6_MD5.png]]
![[attachments/笔记同步图片/88be7b3eb6cf04149316eb95c43362a6_MD5.png]]

朋友们,你为什么用 Obsidian?可定不是因为它的 Markdown 编辑器比别人好用,一定是可能和俺一样,是因为双链、本地、图谱,我猜的没错的还,你是想要一个真正属于自己的第二大脑。
但我打赌,你 Vault 里 80% 的笔记,写过之后就再也没打开过第二次。
Obsidian 第一次立功,基于我的项目背景,给我画了一个架构图会议记录、网页剪藏、读书笔记、灵感碎片、PDF 报告,你起初和我一样,往里塞了上千条,但它们就是躺在那里。占着磁盘,不占大脑带宽。这也就是说,你的这个所谓的第二大脑,根本没有消化系统。
市面上的 Obsidian AI 插件少说几十款,我都试过。它们做的是几乎都是同一件事:在侧栏开一个Agent 对话框,帮你写文件,棒你做下总结,或者闲聊,但是从来没有一个可以系统化的帮你消化你的知识,帮你沉淀你的知识。嗯,有朋友也可能是技术出身,也聊过,他们会用 Claude Code或者龙虾去维护 Obsidian Vault,也许可以解决问题,但是总归是怪怪的,你想啊,我要编辑改动个Obsidian 文件,我还要开一个命令行,这多少看起有点古怪,尤其是一个小女生,这特码的会整那个玩意啊。我觉得直接在 Obsidian 中打开,才是最直接的。
然后,大家其实对我挺了解的,我写过好多个 Agent,其中 small Rust Hermes群友反馈也挺好用,token 消耗也少,该有的功能也都有,也确实可以基本做到越用越懂你吧,这点自信还是有的。
那么,从 Rust 版本到桌面端,从记忆检索到技能市场。这套东西让我想清楚了一件事:Agent 不该只是聪明,它要越用越懂你。
所以我干了件疯狂的事:把 Hermes 的核心引擎整个搬进 Obsidian。 是所有 Hermes 验证过的核心能力,完整地搬进了 Obsidian 的 Vault。这个产品我管它叫 obsidian-cc。
Obsidian-cc全貌,右侧即使一个 agent 对话框我敢说一句话:用上它之后,Obsidian 的能力被拉高了不止 10 倍。 下面就是扯一扯为啥这么讲。
先来看看,这个 Obsidian长什么样,它是聊天 × 文件系统 × 技能市场你点右上角的 ✨ 图标打开面板,第一眼看到的是这样的对话界面。它跟你见过的所有 AI 聊天窗口都不一样,因为它从底层就是为了 Obsidian 的 Vault 设计的。
@ 引用任何笔记@ 引用任何笔记你在输入框敲一个 @,立即弹出整个 Vault 的模糊搜索框。文件名匹配、路径匹配,按相关度排序。
选一篇笔记,它变成一个 chip 附在消息上方。Agent 收到消息时,会带上这条引用。
这意味着什么?你不用复制粘贴,不用解释上下文。你想让 Agent 基于你引用的文件进行分析,就是这么简单,当然,你需要引入新的外部文件,也是可以直接粘贴对话框的,这个后面会讲。
/ 触发技能技能敲一个 /,弹出的不是普通命令面板——是所有可用技能。
/compact                  压缩当前会话上下文      命令
/clear                    清空并开启新会话        命令
/obsidian-digest-note     消化当前笔记或选区       技能
/obsidian-review-inbox    审核 inbox 待确认沉淀    技能
/obsidian-apply-memory    合并 inbox 到长期记忆    技能
/obsidian-update-profile  从反馈学习更新画像       技能
/obsidian-vault-doctor    给 Vault 做体检          技能
/obsidian-create-skill    创建新技能              技能这个细节我打磨了很久。 技能选择不应该是"打字的一部分",它是一个独立的 mode。Pill 模式让它跟普通聊天文本视觉分离,按 Backspace 在空输入框上一键清除,跟删一个 chip 一样的肌肉记忆。
当然有人可能会文,你就支持这么多技能吗??to young too simple,some times native ,朋友,Obsidian-cc 是基于 Claude code 内核的,你想想一下,安装技能和自定义技能是难事吗?可以说是家常便饭,不过,普通用户这些个基本核心的内置技能用上就够了,骨灰级用户需要自己创建技能,完全可以自己创建,适用于不同的工作场景,比如搞自媒体创作,可能需要学习文风的技能等等。
拖拽 / 粘贴文件 → 自动入 raw/直接粘贴文件进入对话框,引用外部文件那是简单的一逼这不来了吗?你截了张图,Ctrl+V 粘贴。普通 AI 插件这时候要么不支持,要么把图片 base64 塞进 prompt 烧 token。
obsidian-cc 不一样。它会:
1. 自动创建 raw/ 目录(如果还没有)2. 把图片存成 raw/(重名自动加后缀)3. 把文件路径作为附件 chip 附在消息上4. 提示「已存入 raw/截图.png」为什么这样设计? 因为图片是原始证据。烧进 prompt 一次就没了,存到 raw/ 之后可以反复引用、可以追溯、可以让 Agent 之后再消化。这是 Hermes 教我的——原始材料永不丢失。
拖拽也一样。PDF、Word、截图、任意文件,拖进来都进 raw/。
流式渲染:每一步都看得见每一步调用都一清二楚思考块是可折叠的——你想看 Agent 在想什么就展开,不想看就不占视觉空间。
工具调用块也是可折叠的,还带结果回显。Read、Write、Edit、Glob、Grep、Bash、WebFetch、Skill——每个工具都有专属图标。
文本块是流式渲染的。但有个细节我特别较真:流式过程中用纯文本,不每 token 重渲染 markdown。为什么?因为流式过程中你想选中文字复制,每次重渲染会打断你的选区。文本块结束的时候才一次性渲染成 markdown。这是 Hermes 桌面版踩过的坑,直接避开了。
每条 Agent 消息下面都有 👍 / 👎 / 复制。 这个不是装饰,我把他定义为产品的核心机制:
你点 👍 / 👎 → 落入 memory/feedback/.md
↓
用 /obsidian-update-profile 技能消化这些反馈
↓
提炼出对 profile.md / style.md 的更新建议
↓
你逐条确认 → Agent 越用越懂你这就是真正的"越用越懂你"。 这个可是是有数据管线支撑的闭环。
最最重要的,Hermes 的灵魂,六大核心技能光有对话界面不算什么。obsidian-cc 真正的杀手锏是六个精心设计的核心技能。每一个都对应第二大脑的一个真实痛点,六个串起来构成完整的"消化—沉淀—生长"闭环。这是基于我们 small Hermes 的经验来的。
技能干什么解决什么痛点obsidian-digest-note消化当前笔记/选区 → inbox笔记写完没人整理obsidian-review-inbox审核 inbox → 可确认清单inbox 越积越多没人审obsidian-apply-memory确认后合并到长期记忆沉淀进 people/projects/wikiobsidian-update-profile从反馈学习 → 更新画像Agent 越用越懂你obsidian-vault-doctorVault 体检报告raw/未消化、断链、孤儿笔记obsidian-create-skill让 Agent 自己造技能元能力:大脑能长出新大脑这六个不是孤立的命令,是一条流水线。
举个真实场景。你今天开会,做了一篇会议笔记。晚上回来:
1. 打开笔记 → 右键 → "用第二大脑消化这篇笔记"(这是上下文菜单直接集成的,不用打字)。digest-note 跑一遍,提炼出关键决议、涉及的人、可沉淀内容,写入 memory/inbox/2026-06-27.md。2. 几天积累下来,inbox 有点多。打 /obsidian-review-inbox,它扫一遍所有 inbox,归纳去重,生成一份可确认清单:哪几条进 people、哪几条进 projects、哪几条该丢弃,每条标了置信度和来源。3. 你审一遍清单,确认。打 /obsidian-apply-memory。它先出合并计划——具体写哪些文件、各加什么、是追加还是新建。你点头之后才执行。这是确认门,不是一步到位。4. 过程中你点了几次 👎("Agent 判断:客户对价格敏感"——其实那次客户只是流程性问价)。打 /obsidian-update-profile,它消化 feedback,提炼出"该用户对市场推断要保持克制"这类稳定模式,更新 profile.md 和 style.md。每次写入都再弹一次确认卡,逐条放行。5. 月底了,打 /obsidian-vault-doctor。它扫整个 Vault,告诉你:raw/ 有 8 个 PDF 没消化、people/ 里张三的页面 3 个月没更新、有 5 处断链。一份体检报告,列出每类问题的下一步建议技能。6. 你发现"整理老婆生日清单"这件事自己经常做。打 /obsidian-create-skill,跟 Agent 说"我想做一个整理礼物清单的技能"。它问清楚意图、产出草稿、你确认后落到 /.claude/skills/gift-planner/SKILL.md。从此这个 Vault 多了一个属于你的专属技能。第六个技能是产品的核心理念:插件只提供共性基础设施,场景化能力由用户在自己的 Vault 里生长。 这不是空话——你创建的技能会自动出现在 / 菜单里,跟内置技能用起来一模一样。
三层文件分层:raw / sources / 长期记忆这个设计来自 Hermes 的三层信任模型。你的 Vault 里东西不是一视同仁的:
raw/                原始证据(PDF/Word/截图)   永不删除,结构上拒绝写入
sources/            Agent 为原件生成的影子 MD   可重做(raw 还在)
memory/inbox/       待审核的沉淀                 自由写
memory/feedback/    👍/👎 反馈                   自由写
people/             人物长期记忆                 写入需确认
projects/           项目长期记忆                 写入需确认
wiki/               概念/知识沉淀                写入需确认
decisions/          决策记录                     写入需确认
daily/              日报                         写入需确认
palace/             任务路由房间卡                写入需确认
profile.md          我是谁                       写入需确认
vault.md            Vault 用途                   写入需确认
style.md            我的风格                     写入需确认
memory_policy.md    沉淀规则                     写入需确认信任等级分明。 原始证据绝对可信(且不可改),抽取结果可重做,长期记忆经过人类确认。
Memory Palace:不存知识,存路线最后讲一个最概念性的东西。
大多数 Agent 记忆系统解决的是"怎么记住更多"——往向量库塞 embedding,按相似度捞回来。
obsidian-cc 走了另一条路:Memory Palace。它不存知识本身,存的是路线——遇到某类任务,先读哪些文件、按什么顺序读、哪些是硬约束、输出写到哪里。
palace/
README.md
digest_note_room.md      ← 消化笔记时走这条路每张房间卡固定五段:
## 触发场景
## 必读(按顺序)
## 条件读
## 输出位置
## 坑 / 禁区比如 digest_note_room.md 规定:消化一篇笔记前,必须先读 profile.md → vault.md → style.md → 当前笔记。涉及人就去读 people/.md,涉及项目就读 projects/.md。输出只能进 memory/inbox/。
为什么这样设计? 因为"记住什么"和"怎么使用记忆"是两件事。一个学生把课本全背下来了(向量检索),但考试不知道先看哪道题——成绩不会好。Memory Palace 教 Agent 怎么调取和使用记忆,不替它记忆。
写在最后我做了大半年的 Hermes。从 3000 行 Rust 的骨架,到桌面端,到记忆检索闭环,到技能市场。每一步都在回答同一个问题:怎么让 Agent 不只是聪明,还能有记忆、有判断、能生长。
obsidian-cc 是这个母题的最终答案——我把它从编程场景,推到了个人知识管理。
Obsidian 是世界上最适合做第二大脑的容器。它本地、它双链、它图谱、它有最活跃的插件生态。但它一直缺一个消化系统。
obsidian-cc 就是那个消化系统。
这次,我们把 Hermes 验证过的引擎、、Memory Palace——完整搬进 Vault 的本地 Agent 生长引擎。
用上之后,Obsidian 终于名副其实地成了你的第二大脑。 它真的会消化、会沉淀、会从你的反馈里学习、会在你的 Vault 里长出专属技能。
效率拉满,不是因为它响应快。是因为你 2000 条笔记里那 1800 条死数据,终于开始自己生长了。
群友反馈,安装简单,易用。
朋友,如果你是 Obsidian 重度用户,已经被"笔记越来越多但用不起来"困扰很久了——这就是等你的那个东西。我欢迎你刀我的群中来体验这个产品。
注意,本项目属于本人所有,可以通过小张老师  微信公众号菜单-群友们-obsidian-cc  添加入群,方可获取obsidian-cc体验和交流及其源码。
进群才可以获取项目:https://github.com/looping-engineering/obsidian-cc
Welcome to your real second brain.

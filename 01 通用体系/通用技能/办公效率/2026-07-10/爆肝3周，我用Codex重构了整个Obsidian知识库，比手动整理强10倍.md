---
author: 人工智能技术栈
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzIwNjcyNDU4OA==&mid=2247484502&idx=1&sn=b6edbfec27e420d681b0e7931295d9aa&chksm=9699294ae50c67e59d233368fb041cb43dd802816a9a60a07bb96a888d64800449b72a175427&mpshare=1&scene=1&srcid=0710WDlE74wTg1kTfVuqSUvQ&sharer_shareinfo=e4feb1e11d161cd6e3ec69a6d41b7993&sharer_shareinfo_first=e4feb1e11d161cd6e3ec69a6d41b7993#rd
saved: 2026-07-10 07:45:47
tags:
  - 笔记同步助手
id: d7655055-8aef-4973-939b-84f37775a58f
---

公众号名称：人工智能技术栈
作者名称：人工智能技术栈
发布时间：2026-07-09 23:57

![[attachments/笔记同步图片/f0e00fe1501e17c3cdb5be90c84f930f_MD5.jpg]]

人在深夜,盯着Obsidian里1274篇未整理的笔记发呆。
这些笔记跨了三年——从读研时的论文摘抄,到工作后的会议纪要,到随手收藏的网页剪藏。文件夹套了五六层,标签打了上百个,但真正需要用的时候,什么都找不到。
直到我把Codex接进了Obsidian。
三周后,我的知识库从"文件仓库"变成了一个能自动整理、主动关联、每日推送简报的思考系统。今天把完整流程交出来,从安装到跑通,跟着做就行。
先说结论:为什么是Codex + Obsidian你可能试过各种知识管理方案——Notion AI、飞书文档、印象笔记,甚至Roam Research。但大部分方案都有一个致命问题:整理环节全靠人。
你收藏了一篇文章,得手动分类。打了个标签,得手动建关联。攒了一周笔记,得自己复盘总结。只要你忙一周没整理,知识库就开始腐烂。
Codex补上了这块。
OpenAI在2025年4月开源了Codex CLI——一个运行在终端的AI编程代理。它能直接读写本地文件,理解项目结构,跨文件执行复杂任务。说白了,它不是一个代码补全工具,而是一个能独立干活的AI助手。
当Codex通过MCP协议接入Obsidian后,它能做到:
扫描你所有笔记,发现你没注意到的隐藏关联自动整理Inbox里的杂乱素材,归档到对应文件夹读取一周的会议记录,生成摘要和行动项分析双向链接图谱,找出孤立节点和知识盲区根据研究笔记草拟文章、报告、邮件Obsidian负责存储和关联,Codex负责整理和思考。 一个当仓库,一个当仓管员兼分析师。
第一步:装好两个工具Obsidian(免费)
去 obsidian.md/download 下载安装包,Windows/Mac/Linux全支持。打开后选择"Create new vault",命名你的知识库,选一个本地路径。
Codex CLI(免费)
Codex CLI需要Node.js环境。打开终端,三行命令搞定:
# 安装Codex CLI
npm install -g @openai/codex
# 设置API密钥
export OPENAI_API_KEY="你的API密钥"
# 启动
codex
如果你在国内,可以通过中转服务或镜像站接入OpenAI API。具体配置方案CSDN上有详细教程,搜"Codex CLI 国内配置"就能找到。
安装完成后,运行 codex --version 确认安装成功。当前最新版本是v0.133.0。
第二步:搭建知识库目录结构不要一上来就搞复杂的文件夹体系。越复杂的结构越难坚持。
推荐四层极简结构:
你的知识库/
├── AGENTS.md          # Codex的操作规范(核心!)
├── Inbox/             # 收件箱:所有新内容统一入口
├── Notes/             # 笔记库:已整理的外部知识
├── Ideas/             # 灵感库:自己的思考和感悟
└── Projects/          # 项目库:正在推进的工作
为什么只有四个文件夹?
Inbox是入口,所有东西先进来,不分类不打标签。Notes存外部内容,Ideas存自己的思考,Projects存行动中的项目。三分法够用了——你的知识不是图书馆,不需要杜威十进制分类法。
如果你喜欢更细的结构,也可以参考Karpathy的LLM Wiki模式,用raw/wiki双层结构。但我的建议是:先从四个文件夹开始,跑通了再说。
第三步:写AGENTS.md——给Codex立规矩这是最关键的一步。AGENTS.md是Codex的操作手册,它决定了Codex怎么理解你的知识库、怎么执行任务。
在知识库根目录创建 AGENTS.md,写入以下内容:
# Knowledge Base Rules
## Who I Am
- Name: [你的名字]
- Work: [你的职业]
- Focus: [你今年最想提升的能力]
## Vault Structure
- /Inbox — 所有新捕获的原始素材,未整理
- /Notes — 外部文章、学习资料、干货内容
- /Ideas — 个人原创思考、灵感、复盘
- /Projects — 正在推进的工作与项目
## Operating Rules
1. 所有新内容先进入Inbox,不直接写入其他文件夹
2. 整理Inbox时,自动分类到Notes/Ideas/Projects
3. 每次写入或修改笔记后,更新对应文件的frontmatter(标签、日期、关联)
4. 发现笔记之间的关联时,主动添加双向链接 [[]]
5. 所有操作保留原始来源链接和保存时间
6. 拒绝网络通用套话,回答只基于我的私有笔记
7. 执行前展示确认清单,执行后发送汇报
这个文件有多重要? Codex每次接入你的知识库时,会优先读取AGENTS.md。它决定了Codex是你的知识库管家,还是一个只会套模板的AI。
把 [ ] 里的内容替换成你自己的信息,写得越具体,Codex的输出越贴合你。
第四步:用MCP把Codex接进ObsidianMCP(Model Context Protocol)是连接Codex和Obsidian的桥梁。目前有三个方案,按需选择:
方案A:obsidian-codex-mcp(轻量首选)
专为Codex CLI设计,不需要安装Obsidian插件,直接操作vault目录中的Markdown文件。12个核心工具,覆盖读写、检索、结构管理。
git clone https://github.com/dot-RealityTest/obsidian-codex-mcp.git
cd obsidian-codex-mcp
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
然后在 ~/.codex/config.toml 中配置:
[mcp.obsidian]
command = "/path/to/obsidian-codex-mcp/.venv/bin/python"
args = ["-m", "obsidian_codex_mcp"]
env = { OBSIDIAN_VAULT_PATH = "/你的知识库路径" }
方案B:enquire-mcp(高级检索)
如果你的vault超过1000篇笔记,推荐这个。44个工具,六层混合检索(BM25 + 向量嵌入 + BGE重排序 + HNSW索引),支持PDF和OCR。大型vault下检索响应在10ms以内。
npm install -g @oomkapwn/enquire-mcp
enquire-mcp setup --vault /你的知识库路径
方案C:mcp-obsidian(经典方案)
需要安装Obsidian的Local REST API插件。适合已经在用这个插件的用户。
我的建议: 从方案A开始,12个工具足够跑通完整流程。等你笔记超过1000篇,再升级到方案B。
第五步:配置Web Clipper——低摩擦收集知识库能不能持续运转,80%取决于收集摩擦力有多低。
安装Obsidian官方Web Clipper插件(免费)。支持Chrome、Edge、Arc等主流浏览器。
设置两步就够:
把默认保存位置改成 Inbox文件命名规则设为 {{date|date:"YYYY-MM-DD"}} - {{title}}以后刷到好文章,点一下浏览器右上角的插件图标,网页自动转成Markdown,带着来源链接进入Inbox。不分类、不打标签、不改文件名。
你只负责"看到好内容就点一下",剩下的交给Codex。
第六步:夜间让Codex消化Inbox白天收集,晚上整理。这是整个系统的核心节奏。
每天晚上,打开Codex,输入一句话:
整理今天的Inbox。按内容属性分类到Notes/Ideas/Projects,优化文件名和格式,保留来源链接,挖掘笔记之间的隐藏关联,生成今日简报。
Codex会自动执行:
逐篇扫描Inbox中的新内容识别内容属性——是外部知识、个人灵感、还是项目资料归档到对应文件夹,优化Markdown格式清理网页剪藏自带的冗余广告内容发现新笔记与已有笔记的关联,添加双向链接生成一份当日知识简报,总结重点和可复用的灵感我试过一次性让Codex处理23篇Inbox笔记,全程不到3分钟。如果手动整理,光格式化和建双链就得花一个多小时。
第七步:每日简报和每周复盘每日简报——让知识库主动反馈
在Codex中设置自动化指令:
每天早上自动运行:读取Inbox近24小时新内容和Notes近7天笔记,找出3个我没发现的隐藏关联,总结本周核心思考模式,提炼1个值得深度思考的问题,生成Markdown简报存入Inbox。
每天早上打开Obsidian,就能看到一份专属简报。它的价值不是总结你做了什么,而是帮你把零散信息串起来,提醒你忽略的关联和问题。
每周复盘——15分钟系统升级
每周一在Codex输入:
通读整个知识库,重点复盘本周新增内容。输出四样东西:我正在形成但尚未总结的核心观点、新旧认知矛盾、知识体系盲区、本周最高杠杆的一件事。直接挑战我的固有认知,拒绝无效总结。
这一步的重点不是"总结做了什么",而是发现:观点怎么在变化、哪些旧认知和新信息冲突、哪里还有盲区、下一步最该做什么。
我的三周实测数据第一周:接入MCP,导入历史笔记427篇,Codex自动添加双向链接186条,找出孤立节点53个。
第二周:开始用Web Clipper + 夜间整理的节奏。新增素材68篇,Codex自动归档率92%,手动干预6篇。每周复盘发现3个之前完全没注意到的知识关联。
第三周:知识图谱从一团乱麻变成能看出明显聚类结构。Inbox不再积压,日均处理时间不到3分钟。最明显的感受是——写文章时打开Obsidian搜素材,从翻半天变成问Codex一句话。
写在最后知识库的失败,从来不是因为工具不够好,而是因为整理成本太高、人坚持不下去。
Codex + Obsidian这个组合,解决的是知识管理最核心的矛盾:让整理环节从"人的负担"变成"AI的工作"。 你只负责持续输入——看到的文章、突发的灵感、工作的记录。整理、关联、复盘、启发,交给Codex。
这不是一个更复杂的文件夹系统,而是一个能把信息转化为思考的反馈循环。
丢5条笔记进去试试。当Codex从几条零散信息中找到你没看到的关联时,你就明白这套系统的价值了。
有问题评论区聊,觉得有用就转发给同样被知识管理困扰的朋友。

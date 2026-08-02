---
author: 输出小能手
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzYzODU0Mzc1NA==&mid=2247483795&idx=1&sn=c204a96101dc5aeddf62785babb23649&chksm=f1ff7394cac4319ada0645acdc5479c13cf6d855cf6df901c8bd69699a296e23e6e555fce7b6&mpshare=1&scene=1&srcid=0627aVxVw6poBQx7bFSqyTJq&sharer_shareinfo=8fd5d71d0c8f3114ce927783444d5f82&sharer_shareinfo_first=8fd5d71d0c8f3114ce927783444d5f82#rd
saved: 2026-06-27 23:53:24
tags:
  - 笔记同步助手
id: 93d3fc85-40bd-420c-93c9-30f08c4c8123
---

公众号名称：我用AI做事
作者名称：输出小能手
发布时间：2026-05-21 10:49

![[attachments/笔记同步图片/a08fa5bc734fd9804d8931f7712683cb_MD5.png]]

把 Markdown 知识库变成可执行工作台的实战指南
其实
Obsidian 并没有一个"官方一键接入 Codex"按钮,但官方能力已经足够把两者连成一个稳定工作流:用 Vault 作为共享文件系统,用 Obsidian CLI 负责读写与调度,用 Obsidian URI 负责跳转与自动化,用 Codex 负责分析、生成、整理和执行。
一、为什么 Obsidian 和 Codex 适合一起用why
Obsidian 把笔记存成 Markdown 纯文本,Vault 本质上就是你本地文件系统中的一个文件夹;而 Codex 天然适合处理目录、文件、命令和文档。只要让 Codex 工作在 Vault 根目录,两者就拥有同一份事实源。
Obsidian 的笔记是 Markdown 纯文本文件,Vault 就是一个本地文件夹,并且当外部工具修改文件时,Obsidian 会自动刷新;同时,Codex 可在 CLI、IDE、Web 等多种界面运行,并可以连接 MCP、Shell 等外部能力。这意味着"知识库即工作区"是可验证、可维护、可扩展的,不是临时技巧。
如果把视角拉大一点,这种工作流很像从 Google 搜索时代延伸出来的知识处理范式:信息先被结构化,再被检索、链接、复用,最后进入执行层。今天的区别在于,Codex 把"执行层"接到了知识库旁边。
二、官方可行的 3 种接入方式way
方式
核心能力
适用场景
推荐度
Vault 直连
在 Vault 根目录运行 Codex,直接读写 Markdown
知识库整理、项目笔记、研究报告
高
Obsidian CLI 协同
用 `obsidian` 命令读写当前 Vault
自动写日报、搜笔记、批量落库
高
Obsidian URI 自动化
从外部一键打开、创建、搜索指定笔记
快捷入口、跳转、工作流编排
中
推荐做法不是只选一种,而是把三种能力叠加:日常以 Vault 直连为主,批量操作靠 Obsidian CLI,跳转体验用 URI 做补强。
三、推荐架构:Vault 直连 + CLI 协同 + URI 跳转
这是最稳的组合。Codex 在 Vault 根目录工作,所有输出都直接落到笔记目录;Obsidian 负责可视化浏览、双链、标签、图谱和模板;Obsidian CLI 让你在终端里精准读写指定笔记;Obsidian URI 负责从终端、快捷指令、浏览器或其他应用一键打开目标笔记。
Knowledge-Vault/
00-Inbox/
10-Projects/
20-Research/
30-Meetings/
90-AI/
AGENTS.md
README.md
.obsidian/
目录设计原则
不要把 Vault 再套进别的 Vault。Obsidian 官方明确不建议"vault 里再嵌 vault",否则链接更新可能出问题。建议把 Codex 要处理的项目、研究、会议和 AI 输出直接放在同一个 Vault 里分目录管理。
四、接入步骤
步骤 1:准备 Vault
新建或选定一个 Obsidian Vault,确保它是你愿意长期维护的主知识库。Obsidian 官方说明里提到,Vault 就是本地文件夹,所以最重要的不是花哨插件,而是目录结构清晰、命名稳定。
# 示例:在 Vault 中为 Codex 预留目录
00-Inbox      # 临时输入、待清洗信息
10-Projects   # 项目方案、开发记录、任务拆解
20-Research   # 调研文档、资料汇总、竞品分析
90-AI         # Codex 输出、提示词、自动化脚本
步骤 2:确认终端里的 Codex 可用
文章编写时,本机终端中 `codex --help` 与 `codex --version` 可正常执行。你至少要保证终端里能识别 `codex` 命令,然后让它以 Vault 根目录作为工作目录启动。
# 在 Vault 根目录启动 Codex
cd /path/to/Knowledge-Vault
codex
# 或显式指定工作目录
codex -C /path/to/Knowledge-Vault
这样做的意义是让 Codex 直接读取和写入你的 Markdown 笔记,而不是在一个脱离知识库的临时目录里工作。
步骤 3:开启 Obsidian CLI
根据 Obsidian 官方帮助,Obsidian CLI 需要新版安装器,并且要在 Obsidian 的 `Settings -> General` 中打开 `Command line interface`。启用后,你可以在终端里直接控制 Vault。
# 基础验证
obsidian help
obsidian search query="Codex"
obsidian create path="90-AI/Codex-Playbook.md" content="# Codex Playbook"
官方文档还说明了一个关键点:如果终端当前目录本身就是 Vault 根目录,那么 Obsidian CLI 默认会把这个 Vault 当作目标,这和 Codex 的目录式工作方式非常匹配。
步骤 4:给 Codex 补上 OpenAI 官方文档能力
如果你希望 Codex 在整理 API 笔记、写 SDK 文档、做方案调研时优先查 OpenAI 官方资料,最稳的做法是把 Docs MCP 加进去。OpenAI 官方给出的命令是:
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
官方还建议在 `AGENTS.md` 里加一句约束,让 Codex 遇到 OpenAI 相关问题时优先走官方文档 MCP。
Always use the OpenAI developer documentation MCP server if you need to work with the OpenAI API, ChatGPT Apps SDK, Codex, without me having to explicitly ask.
步骤 5:在 Vault 根目录加入 AGENTS.md
这是把 Codex 训练成"懂你这套知识库规则的长期助手"的关键。你不用写太长,但规则要具体,尤其是命名、双链、标签、来源标注和输出落点。
# AGENTS.md 示例
Treat this vault as a long-lived knowledge base.
Prefer updating existing notes over creating duplicates.
Preserve Obsidian wikilinks such as [[Topic Name]].
Write new AI outputs under 90-AI/.
When summarizing sources, keep original links and add a short source block.
When editing meeting notes, keep action items in checkbox format.
步骤 6:把高频动作改造成命令模板
接入不是"能连上"就结束,真正提升效率的是把高频动作固化。比如日报、会议纪要整理、研究摘要、项目拆解,都应该收敛成固定命令或固定提示词。
# 1. 给今日日志追加待办
obsidian daily:append content="- [ ] Review Codex output" open
# 2. 读取当前项目方案后交给 Codex加工
obsidian read path="10-Projects/Obsidian-Codex-Plan.md"
# 3. 让 Codex把访谈笔记整理成执行摘要
codex -C /path/to/Knowledge-Vault "Read 30-Meetings/customer-interview.md and rewrite it into an executive summary under 90-AI/. Preserve source links and action items."
步骤 7:用 URI 做跳转和自动化入口
Obsidian 官方 URI 支持 `open`、`new`、`daily`、`search` 等动作,非常适合把 Codex 的结果快速带回 Vault。尤其是在 macOS 快捷指令、浏览器书签、Raycast、Keyboard Maestro 这类工具里,URI 的价值很高。
# 打开指定笔记
obsidian://open?vault=Knowledge-Vault&file=90-AI/Codex-Playbook
# 创建或追加一条 AI 记录
obsidian://new?vault=Knowledge-Vault&file=90-AI/Codex-Inbox&append=true&content=New%20idea
# 直接打开搜索
obsidian://search?vault=Knowledge-Vault&query=Codex
五、最值得落地的 4 个场景
1.研究资料入库:让 Codex 读取网页、PDF、Markdown 草稿,整理成带来源的 Obsidian 笔记。
2.会议纪要清洗:把原始纪要改写成"结论、行动项、风险、待确认"结构,并保留原文链接。
3.项目文档协同:让 Codex 在 `10-Projects/` 下维护方案、里程碑、问题清单和评审记录。
4.个人知识中台:通过 `90-AI/` 统一保存 Codex 输出,让 AI 结果能被二次检索、双链和复用。
六、常见坑与规避方式
不要把临时测试输出散落到 Vault 根目录。给 Codex 预留固定落点,例如 90-AI/。
不要让 Codex 随意改写你的命名体系。目录、标签、双链规则最好写进 AGENTS.md。
不要在 Vault 里再嵌套另一个 Vault。Obsidian 官方明确提醒这样可能导致链接更新异常。
如果你使用 Git 管理 Vault,优先忽略 .obsidian/workspace.json 和 .obsidian/workspaces.json,否则界面布局会频繁制造噪音变更。
Obsidian CLI 依赖桌面端运行。批量脚本执行前,先确认 Obsidian 已启动或允许首个命令自动唤起。
七、推荐给团队的最小实施方案
如果你要在团队里推,而不是自己玩,建议只做最小闭环:一个共享 Vault 结构、一份 `AGENTS.md`、一个 Docs MCP、三到五条稳定命令。先让团队把"文档可执行"跑通,再慢慢增加模板、自动化和快捷入口。
最小闭环清单1. 统一 Vault 目录结构2. 所有人启用 Obsidian CLI3. Codex 工作目录固定指向 Vault 根目录4. 加入 Docs MCP5. 统一 AGENTS.md 规则6. 固化 3 条高频命令:日报追加、项目摘要、研究入库
最后
Obsidian 接入 Codex 的本质,不是给笔记软件塞一个聊天框,而是把你的知识库改造成一个可以被读取、整理、检索、执行的工作台。只要共享的是同一个 Vault,Obsidian 负责组织知识,Codex 负责推动工作,这套组合就能持续放大效率。
真正值得投入的不是"装了多少插件",而是你有没有把目录结构、规则、命令和输出落点做成一套稳定系统。

---
author: 搞 AI 的Wayne
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzE5ODI3Mzk5OQ==&mid=2247483788&idx=1&sn=95b74ed63bf65b0af567005e185f6ea4&chksm=97aed24d0586ef98d5f2c4c507afc2ea75a8a74fad19846624b906d3567764bf738f9967e95c&mpshare=1&scene=1&srcid=0714f9Ts7ksXYAUejvd799Lk&sharer_shareinfo=53277a1249f270db9f7b8b262a65af2c&sharer_shareinfo_first=53277a1249f270db9f7b8b262a65af2c#rd
saved: 2026-07-14 07:43:57
tags:
  - 笔记同步助手
id: 96d624df-74fb-428e-be43-c5a502c72a92
---

公众号名称：搞AI的Wayne
作者名称：搞 AI 的Wayne
发布时间：2026-05-23 19:20

![[attachments/笔记同步图片/c6796b977de3de6fd5b246aa0b2439cc_MD5.jpg]]
![[attachments/笔记同步图片/d0eb3ae5929ec31ceaa7880f15d883a3_MD5.jpg]]
![[attachments/笔记同步图片/d6a893468898967abe52d52e6abe4693_MD5.jpg]]

我用飞书多维表格,给自己的 Codex skills 做了一套"能力管理台账"如果你自己读这篇觉得太长、太细,可以直接把这篇文章发给你的 Codex,让它照着文章里的方法,帮你盘点本机 skills、设计飞书多维表格、写同步器,并接入全局 Stop hook。
Hello Codex:
请你阅读这篇文章,并按照文章里的方法,帮我搭建一套 Codex skills 管理台账。要求:1. 扫描我本机可见的所有 SKILL.md。2. 区分系统内置、用户自建、全局共享、插件内置、插件缓存可见等来源。3. 提取每个 skill 的名称、来源路径、创建时间、修改时间、主要目的、触发方式、AGENTS 索引状态、能力域、权限风险和当前状态。4. 设计一张飞书多维表格来管理这些 skills,并用唯一键避免同名 skill 被误合并。5. 增加 Skill包 字段,把同一个 skill 包下的子 skill 归到一起。6. 写一个同步器,支持 dry-run、新增、更新、失效标记和本地 catalog 同步。7. 接入 Codex 全局 Stop hook,让任意 Codex 窗口任务结束后自动检查是否需要同步。8. 全程不要把"文件存在"说成"能力已验证可用",不要保存密钥、access token 或 OAuth 设备码。先给用户执行计划,等用户确认后再落地。摘要当 Codex skills 越装越多,真正麻烦的不是"有没有能力",而是"我到底有什么能力、这些能力从哪里来、什么时候会被触发、是否还有效、更新后有没有同步"。这篇文章记录我把本机 Codex skills 扫描成飞书多维表格,并通过全局 Stop hook 自动同步的完整过程。
正文最近我在整理自己的 Codex 能力栈时,遇到一个很现实的问题:
skills 已经越来越多了。
一开始,skills 少的时候,靠 AGENTS.md 里的几条索引规则就够用。比如告诉 Codex:遇到飞书文档就用哪个 skill,遇到图片生成就用哪个 skill,遇到产品包装就用哪个 skill。
但当 skills 数量越来越多,问题就不一样了。
我需要知道的不只是"有没有这个 skill",还包括:
• 这个 skill 是系统内置的,还是我自己创建的?
• 它来自 .codex\skills、.agents\skills,还是插件缓存?
• 它是独立 skill,还是某个 skill 包下面的子 skill?
• 它的主要目的是什么?
• 它是会被语义自动触发,还是必须用户主动点名?
• 它有没有被 AGENTS.md 索引?
• 它涉及本地写入、远端写入、OAuth、浏览器登录态,还是只读?
• 它还在本机可见吗?
• 它被更新了以后,我怎么知道目录已经同步?
这时候再把所有信息继续堆进 AGENTS.md,就不合适了。
AGENTS.md 应该是规则入口,不应该变成一张越来越大的清单。
所以我做了一个更适合长期维护的方案:
用飞书多维表格管理 Codex skills,把 AGENTS.md 只保留为索引入口和触发规则。
为什么不用一个 Markdown 表格继续管理?我一开始确实先做了一个本地 Markdown 目录。
路径类似:
C:\Users\\.codex\codex-skills-catalog.md这个目录里列出了本机可见的 SKILL.md,包括来源、路径、创建时间、修改时间、用途、触发方式、AGENTS 索引状态、能力域、权限风险和当前状态。
Markdown 的好处是简单、稳定、适合版本化。
但它也有明显缺点:
• 不方便筛选:比如我想只看"飞书/Lark"能力,Markdown 不如表格顺手。
• 不方便分组:比如按 skill 包、来源类型、触发方式分组。
• 不方便人工维护:我想手动调整字段、单选项、视图顺序,Markdown 不够直观。
• 不方便作为长期管理台账:尤其是后面要看新增、失效、最近同步时间、内容指纹。
所以 Markdown 可以作为本地索引,但真正适合日常查看和管理的,是多维表格。
第一步:确定我要管理哪些 skill我先定义了扫描范围。
这一步很重要,因为不能把"当前会话可见"和"本机缓存里存在"混为一谈。
我的默认扫描目录包括:
C:\Users\\.codex\skills C:\Users\\.agents\skills C:\Users\\.codex\plugins\cache\openai-bundled C:\Users\\.codex\plugins\cache\openai-curated C:\Users\\.codex\plugins\cache\openai-primary-runtime另外,我还有一个外部路径里的 skill,也纳入了额外扫描:
D:\code\优化codex\Claude-to-IM-skill\SKILL.md这里有一个边界需要说清楚:
扫描到 SKILL.md,只能说明这个文件在本机可见,不能说明这个 skill 的外部服务、OAuth、API、CLI 都已经验证可用。
所以我在同步备注里明确写了:
由 Codex skills catalog sync 自动维护;未逐个运行验证。这句话很关键。
做能力治理,最怕把"看见文件"说成"能力可用"。
第二步:设计多维表格字段我给多维表格设计了两类字段。
第一类是业务字段,用来描述 skill 本身:
•Skill名称:skill 的标准名称。
•Skill包:它属于哪个安装包、插件包或能力套件。
•来源类型:系统内置、用户自建、全局共享、插件内置、插件缓存可见。
•来源路径:SKILL.md 的本机路径。
•创建时间:本机文件创建时间。
•最后修改时间:本机文件最后修改时间。
•主要目的:从 description、标题或前 20 行说明中提炼。
•触发方式:语义被动触发、强制前置触发、用户主动点名触发等。
•AGENTS 索引状态:直接点名索引、通过 catalog 间接索引、未直接索引。
•能力域:飞书、Figma、HyperFrames、浏览器、文档、图像等。
•权限与风险:只读、本地写入、远端写入、OAuth、浏览器会话等。
•当前状态:当前会话可用、本机可见、缓存可见待确认、失效等。
第二类是同步字段,用来支撑自动化:
•唯一键:用规范化后的 SKILL.md 绝对路径生成稳定 key。
•内容指纹:用路径、修改时间、文件内容 hash 计算。
•本机可见:当前扫描是否还能看到这个文件。
•首次同步时间:第一次写入 Base 的时间。
•最近同步时间:最近一次同步时间。
•最后扫描批次:用时间戳表示一次扫描批次。
•失效时间:本机扫描不到时记录失效时间。
•同步备注:解释自动维护边界。
其中最重要的是 唯一键。
为什么不用 Skill名称 当唯一键?
因为会重名。
比如 Chrome 相关 skill 可能会有不同缓存版本。再比如一个 skill 包里可能有多个子 skill。只用名称,很容易误合并。
所以我选择用 SKILL.md 的绝对路径作为唯一键。
这比名称更稳定,也更符合本机能力目录的实际结构。
第三步:增加"Skill包"字段这一步是我后来补上的。
因为我发现有些 skill 不是独立安装的,而是一个大包下面带出来的一组子 skill。
最典型的例子是 Superpowers。
它下面有 14 个子 skill,例如:
• brainstorming
• executing-plans
• systematic-debugging
• test-driven-development
• writing-plans
• writing-skills
• using-superpowers
• verification-before-completion
如果只看 Skill名称,这些会像 14 个独立能力。
但从管理视角看,它们应该有共同归属:
Skill包 = Superpowers所以我新增了 Skill包 字段,并把它设计成单选。
目前我的归包规则大致是:
•Superpowers:Superpowers 套件里的 14 个子 skill。
•Lark CLI Skills:lark-*、feishu-bitable 等飞书 CLI skills。
•Figma:Figma 插件内置 skills。
•HyperFrames:HyperFrames、GSAP、Lottie、Three 等视频动效相关 skills。
•GitHub:GitHub 插件缓存 skills。
•Browser / Chrome:浏览器相关插件 skills。
•Documents / Presentations / Spreadsheets:primary runtime 提供的文档、演示、表格能力。
•Codex System Skills:.system 里的系统 skills。
•image-design-workflow:image-design-workflow 内部嵌套的辅助 skills。
•Claude-to-IM:Claude-to-IM 相关 skill。
•独立 skill:暂时没有归入大包的独立能力。
这个字段一加,多维表格的价值就明显提升了。
我可以按 Skill包 分组,一眼看出哪些能力是套件型的,哪些是真正独立安装的。
第四步:写同步器同步器放在:
C:\Users\\.codex\skills-catalog-sync\sync_skills_catalog.py同目录还有:
config.json state.json logs\sync.log tmp\配置文件记录扫描根目录、目标飞书 wiki URL、目标 table ID、view ID、需要维护的字段等。
状态文件记录最近一次扫描时间、最近一次同步时间、Base token、table ID、view ID、内容指纹和 schema 版本。
同步器的核心逻辑是:
1. 扫描本机所有可见 SKILL.md
2. 解析 frontmatter 里的 name 和 description
3. 没有 description 时读取一级标题和前 20 行说明
4. 读取本机 CreationTime 和 LastWriteTime
5. 计算内容指纹
6. 读取飞书 Base 现有字段和记录
7. 缺字段就自动补字段
8. 通过 唯一键 匹配远端记录
9. 新 skill 创建记录
10. 已存在但内容变化的 skill 更新记录
11. 本机扫描不到的旧 skill 不删除,只标记为 失效 / 未扫描到
这里我特别保留了"不删除"的策略。
原因很简单:
能力目录是治理台账,不是临时缓存。
一个 skill 今天扫描不到,不一定代表它永远没价值。可能是路径迁移、插件缓存变化、版本更新,或者暂时不可见。
所以我宁可标记失效,也不自动删除。
第五步:把飞书 Wiki 链接解析成 Base飞书多维表格经常出现在知识库 wiki 链接里。
用户看到的可能是:
https://xxx.feishu.cn/wiki/xxxx?table=tbl_xxx&view=vew_xxx这里的 /wiki/xxxx 不是 Base token。
正确做法是先用:
lark-cli wiki +node-get --as user --token ""解析出真实的 obj_token。
当返回的 obj_type 是 bitable 时,obj_token 才是后续 lark-cli base +... 要用的 Base token。
这一步如果搞错,就很容易遇到 baseToken is invalid 之类的问题。
第六步:字段自动补齐同步器每次运行时,会先读取字段结构:
lark-cli base +field-list \   --as user \   --base-token  \   --table-id  \   --offset 0 \   --limit 200如果缺字段,就自动创建。
例如 Skill包 是后来新增的字段。同步器发现远端缺这个字段后,会创建一个单选字段,并写入预设选项。
我后来还手动调整过多维表格结构:
• 第一列原来是空字段,我改成了 Skill名称
• 原来的 Skill 字段被删除
•来源类型、触发方式、AGENTS 索引状态、当前状态 改成了单选
• 新增 Skill包 字段
同步器也相应做了 schema 升级,避免下次运行时又把旧的 Skill 字段补回来。
这是一个很实际的经验:
自动同步器一定要允许人工调整表结构。
否则表格一旦被人手动优化,脚本下次运行又把旧结构补回来,就会变成"自动化污染"。
第七步:接入 Codex 全局 Stop hook只做同步脚本还不够。
如果每次都要手动运行,时间久了还是会忘。
所以我把它接到了 Codex 的全局 Stop hook。
全局 hook 文件路径:
C:\Users\\.codex\hooks.json大致结构是:
{   "hooks": {     "Stop": [       {         "hooks": [           {             "type": "command",             "command": "python \"C:\\Users\\\\.codex\\skills-catalog-sync\\sync_skills_catalog.py\" --mode hook",             "timeout": 120,             "statusMessage": "同步 Codex skills 管理目录"           }         ]       }     ]   } }这样以后任意 Codex 窗口结束一轮任务时,都会触发同步器。
但它不是每次都真的写远端。
hook 模式里做了几件事:
• 读取 Codex 传入的 JSON stdin
• 如果 stop_hook_active=true,直接静默退出,避免递归
• 如果环境变量 SKILLS_CATALOG_SYNC_DISABLE=1,直接静默退出
• 使用锁文件避免多个 Codex 窗口同时写飞书 Base
• 如果本机 skill 指纹没有变化,直接静默退出
• Stop hook stdout 返回合法 JSON:
{"continue": true, "suppressOutput": true}这个设计的目标是:
有变化时自动同步,无变化时不打扰。
第八步:用 dry-run 做验证同步器支持 dry-run。
命令类似:
python "C:\Users\\.codex\skills-catalog-sync\sync_skills_catalog.py" --dry-run我会看几个关键数字:
{   "scanned": 97,   "missing_fields": [],   "create_count": 0,   "update_count": 0,   "stale_count": 0 }这几个字段分别表示:
•scanned:当前本机扫描到多少个 SKILL.md
•missing_fields:飞书 Base 还缺哪些字段
•create_count:需要新增多少条记录
•update_count:需要更新多少条记录
•stale_count:有多少旧记录需要标记失效
当 create、update、stale 都是 0,说明本地和远端已经对齐。
我还做了 hook 模拟:
'{"stop_hook_active":false}' | python "C:\Users\\.codex\skills-catalog-sync\sync_skills_catalog.py" --mode hook预期输出:
{"continue": true, "suppressOutput": true}这说明 hook 模式不会破坏 Codex 的 Stop 事件协议。
最终效果现在这张多维表格变成了我的 Codex skills 管理台账。
它不是一个静态清单,而是一个会持续同步的能力目录。
我可以在表里按这些维度查看:
• 按 Skill包 看能力套件:Superpowers、Lark CLI Skills、Figma、HyperFrames
• 按 来源类型 看系统内置、自建、全局共享、插件内置、插件缓存
• 按 触发方式 看哪些是语义被动触发,哪些是强制前置触发
• 按 能力域 看飞书、浏览器、图像、音视频、文档、表格
• 按 权限与风险 看哪些能力会涉及 OAuth、远端写入、浏览器会话
• 按 当前状态 看当前会话可用、本机可见、缓存可见待确认、失效
• 按 内容指纹 和 最近同步时间 判断最近是否发生变化
更重要的是,我不用每次想起来才维护。
以后只要我新增或更新 skill,任意 Codex 窗口结束一轮任务时,hook 都会检查本机 SKILL.md 指纹。
有变化就同步。
没变化就静默退出。
这套方案真正解决了什么?表面上看,它只是把 skills 列到飞书多维表格里。
但真正解决的是 AI Agent 长期使用后的"能力治理"问题。
当能力越来越多,单靠记忆和自然语言是不够的。
你需要一张可以被人看、也可以被脚本维护的能力台账。
这张台账要回答几个问题:
1. 我现在有什么能力?
2. 这些能力从哪里来?
3. 它们属于哪个能力包?
4. 它们会在什么时候被触发?
5. 它们有没有权限风险?
6. 它们有没有被 AGENTS.md 索引?
7. 它们现在还可见吗?
8. 它们最近有没有变化?
这就是我为什么选择多维表格,而不是继续把信息塞进 AGENTS.md。
AGENTS.md 负责告诉 Agent 怎么行动。
多维表格负责管理能力资产。
同步器负责让两者持续对齐。
可以复用的实操清单如果你也想做一套类似的系统,可以按这个顺序来:
1. 先盘点本机所有 SKILL.md
2. 确定扫描根目录和额外路径
3. 设计多维表格字段
4. 用 唯一键 避免同名 skill 覆盖
5. 用 内容指纹 判断是否变化
6. 用 本机可见 和 当前状态 处理失效记录
7. 不要自动删除旧记录,先标记失效
8. 给套件型能力增加 Skill包
9. 把分类字段做成单选,方便分组和筛选
10. 写同步器,支持 dry-run
11. 接入 Codex Stop hook
12. hook 无变化时必须静默退出
13. 加锁,避免多个窗口并发写同一张表
14. 保留日志和 state 文件
15. 每次 schema 变化都记录版本
需要注意的边界这套方案也有边界。
第一,它不是实时文件监听。
如果你在 Codex 外部改了 SKILL.md,它不会立刻同步。要等下一次任意 Codex 窗口结束一轮任务,Stop hook 才会触发扫描。
第二,它不能证明每个 skill 都已经可用。
扫描到文件,只能说明文件存在。外部 API、OAuth、CLI、浏览器登录态、额度、权限,都需要单独验证。
第三,创建时间只代表本机文件创建时间。
对于系统 skill 或插件缓存 skill,这个时间更准确地说是"本机缓存创建时间",不是这个 skill 最早被开发出来的时间。
第四,插件缓存里的 skill 可能只是缓存可见。
它不一定代表当前会话已经声明可用,也不一定代表插件已启用。
第五,自动化脚本要尊重人工维护。
如果我在飞书表格里手动把字段改成单选、调整列顺序、改字段名,同步器不能粗暴地把旧结构又补回来。
所以 schema 版本和配置备注也很重要。
我的结论我以前更关注"给 Codex 增加能力"。
现在我越来越觉得,能力多了以后,更关键的是"治理能力"。
一个长期使用的 AI Agent,不应该只是一堆 skill、hook、MCP、plugin 和规则文件的堆叠。
它应该有一张自己的能力资产表。
这张表能告诉我:
哪些能力是系统给的。
哪些能力是我自己做的。
哪些能力来自插件。
哪些能力属于同一个能力包。
哪些会自动触发。
哪些有远端写入风险。
哪些已经失效。
哪些刚刚更新过。
当这些信息能够被结构化管理,AI Agent 才不只是"会做很多事",而是逐渐变成一个可维护、可审计、可扩展的工作系统。
这也是我这次用飞书多维表格管理 Codex skills 的真正原因。
发布前风险检查• 可发布:字段设计、同步逻辑、hook 机制、dry-run 验证方法、能力治理思路。
• 建议脱敏:真实 Base token、完整个人用户名路径、OAuth 设备码、任何 access token 或 app secret。
• 不能宣传:不能说已经逐个验证 97 个 skill 可用。
• 不能宣传:不能说这是 Codex 官方内置的完整能力管理系统。
• 不能宣传:不能说外部文件变化会实时同步。
• 可表达边界:这是基于本机可见 SKILL.md、飞书多维表格和 Codex Stop hook 组合出来的个人能力治理方案。

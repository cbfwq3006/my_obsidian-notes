---
author: 
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg3MjU3NzU1OA==&mid=2247523735&idx=1&sn=6b1cc76676ed1c858df8af69baf3961c&chksm=cfd1500259f54212443bad4964b3acb8c2382727517498197763facb19eb0d02cc5967300711&mpshare=1&scene=1&srcid=0614YGnsF7LpbTFH2YzhrRa6&sharer_shareinfo=95dc55b38b7a7a45849e328a5891c5b7&sharer_shareinfo_first=95dc55b38b7a7a45849e328a5891c5b7#rd
saved: 2026-06-14 17:57:12
tags:
  - 笔记同步助手
id: 00d6283c-b0b0-4ebe-9fc0-14fb4381a6c9
---

公众号名称：进击的Coder
发布时间：2026-06-14 17:41

![[attachments/笔记同步图片/9d3be2c0596c7a609ddb9c284506331c_MD5.png]]
![[attachments/笔记同步图片/0e9b5a1d162beec5068e238287c2db57_MD5.jpg]]

"📘 Overview:Claude Code MCP Overview →
Seedance 是字节跳动推出的 AI 视频生成模型,对中文描述理解非常准确,生成的视频动态自然。接到 Claude Code 后,你可以直接在终端里用自然语言生成视频——描述一个场景,几分钟就能拿到成片。
获取 API Token使用 Seedance MCP Server 之前,需要先准备一个 Ace Data Cloud API Token。获取方式和 Claude Code VS Code 配置教程保持一致:
打开 Ace Data Cloud 控制台 - 应用列表,或者识别下方二维码:然后获取您的 API Token,留作备用。 2. 如果你尚未登录或注册,会自动跳转到登录页面;登录注册之后会自动返回当前页面。 3. 首次申请时会有免费额度赠送,可以先免费体验 Claude Code MCP 服务。
一个 Token 可以使用 AceData Cloud 提供的全部 MCP Server,无需为 Seedance 单独申请。文档和截图里建议只展示脱敏形式,例如 3b78cc40dd3b43db806a4300....,不要把完整 Token 贴到公开仓库、Issue、截图或聊天记录里。
"用 claude.ai 网页版或 Claude Desktop?它们支持 OAuth 一键授权,无需手动填 Token,详见 Seedance MCP 的 Claude.ai / Desktop 教程。
配置 Claude Code下面三组选一种即可。-H 必须大写,小写 -h 是 --help;Authorization 后面的 Token 请替换成你在控制台复制到的真实值。
只给当前项目用:local适合先试用,配置只绑定你运行命令时所在的项目目录。Claude Code 会把记录写进本机 ~/.claude.json,并带上当前项目路径。
claude mcp add seedance --transport http https://seedance.mcp.acedata.cloud/mcp \
-H "Authorization: Bearer 3b78cc40dd3b43db806a4300...." \
-s local
所有项目都能用:user适合你经常在多个项目里使用 Seedance MCP。配置写进本机 ~/.claude.json 的用户级配置,之后任何项目打开 Claude Code 都能看到。
claude mcp add seedance --transport http https://seedance.mcp.acedata.cloud/mcp \
-H "Authorization: Bearer 3b78cc40dd3b43db806a4300...." \
-s user
随项目共享:project适合团队项目。配置写进当前项目根目录的 .mcp.json,可以提交到私有仓库让队友复用;公开仓库不要提交真实 Token,建议改成环境变量占位符或让每个人本地自行添加。
claude mcp add seedance --transport http https://seedance.mcp.acedata.cloud/mcp \
-H "Authorization: Bearer 3b78cc40dd3b43db806a4300...." \
-s project
项目级配置第一次被 Claude Code 读取时,可能会显示 Pending approval,需要在 Claude Code 会话里确认信任这个项目配置,这是正常的安全提示。
真实运行结果下面是在 Claude Code 2.1.158 中用隔离临时目录实际执行后的脱敏输出。命令使用真实 AceData Cloud Token,输出中的 Token 已替换成 3b78cc40dd3b43db806a4300....,临时配置已删除。
Added HTTP MCP server seedance with URL: https://seedance.mcp.acedata.cloud/mcp to local config
seedance: https://seedance.mcp.acedata.cloud/mcp (HTTP) - ✓ Connected
三种 scope 的行为也做过实测:
luma-local: https://luma.mcp.acedata.cloud/mcp (HTTP) - ✓ Connected
luma-user: https://luma.mcp.acedata.cloud/mcp (HTTP) - ✓ Connected
luma-project: https://luma.mcp.acedata.cloud/mcp (HTTP) - ⏸ Pending approval (run `claude` to approve)
确认本机配置时可以运行:
claude mcp list
看到 seedance: https://seedance.mcp.acedata.cloud/mcp (HTTP) - ✓ Connected 就说明 Seedance MCP 已经接入成功。
实际用法配置完成后,回到 Claude Code 会话直接用自然语言即可调用 Seedance:
产品演示视频
写文档、做演示时直接生成视频素材:
生成一段视频:一个运维监控大屏上的仪表盘在实时刷新,曲线在波动,数字在跳动,深色主题
让图片动起来
用这张产品图生成一段视频,让产品缓缓旋转展示
生成视频片头
生成的视频可以直接嵌入到 HTML / Markdown 文件中:
生成一段 3 秒的视频片头:一个发光的代码符号  从模糊变清晰,背景有粒子特效,科技蓝色调
工具列表工具说明seedance_generate_video文本生成视频seedance_generate_video_from_image图片生成视频相关链接Seedance MCP Server(GitHub)Claude + Seedance MCP 图文教程(claude.ai / Desktop)Claude Code MCP OverviewMCP 协议官网

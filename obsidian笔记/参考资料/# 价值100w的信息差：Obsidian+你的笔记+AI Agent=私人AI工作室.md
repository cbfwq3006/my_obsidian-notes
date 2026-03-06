

原创 廖磊AI编程 廖磊AI编程

![Obsidian](https://mmbiz.qpic.cn/mmbiz_png/zDicTibYTEOJr5HNAfsSkcI253g8TF68aX3ia0RQ64LEpjuAjB4folJhkD4iaVQ3M19ZwIRkCRy36UlSViajkdEq9CAxIIvTsXKAO1sgicCiccY95g/640?wx_fmt=png&from=appmsg)

Obsidian CEO 发布了自己的 Claude Code Skills , 9天暴涨6.6k Star 现在已经 9.9k Star。

Claude Code 作为一个程序员专属工具忽然变成了一个人人都可以使用的 AI Agent。

然而 Markdown 代码一样作为文本文件， Claude Code 能阅读、操控你电脑上的任何文件，再配合上大模型的能力，所以理论上它可以完成任何事情。

Obsidian 作为一个开源的 Markdown 编辑器，加上 Claude Code，就真的能成为你的第二大脑了。

Obsidian 提供数据，Claude Code 提供算力，两者结合就产生了质变。

**「这不再是「记笔记」，这是在本地建了一个「能读懂你过去所有人生」的数字工作室。」**

今天我们手摸手，教会你如何 30 分钟快速拥有自己的私人 AI 工作室

![9天暴涨6.6k Star！Obsidian CEO 开源三大专属Skills，Claude Code不再乱改笔记格式](https://mmbiz.qpic.cn/mmbiz_png/zDicTibYTEOJrczQQ8oyEekAvAKib8GZ7EYOhf2iaPfeKYjhkQ1jZCo41TyKQnZZCcTzaI5mohFrm7llqOPASkmvUEKfBIlaLVY85ibJSpFxYiavA/640?wx_fmt=png&from=appmsg)

---

## 什么是「私人 AI 工作室」

这套方案，由三个免费工具组成：

- **「Obsidian」**：本地笔记软件，数据完全归自己所有
    
- **「Git 插件」**：给 Obsidian 加上版本控制，告别丢失笔记的恐惧
    
- **「Claude Code CLI」**：Anthropic 推出的 AI Agents
    

### 安装 Obsidian Git 插件

1. 打开 Obsidian → 设置 → 第三方插件
    
2. 关闭「安全模式」
    
3. 浏览插件市场，搜索「obsidian-git」
    
4. 安装并启用
    

### 基础配置

插件设置里有几个关键选项：

- **「自动提交」**：设置时间间隔，比如每 30 分钟自动提交一次
    
- **「自动推送」**：提交后自动推送到远程仓库
    
- **「启动时拉取」**：每次打开 Obsidian 自动拉取最新版本
    

这样一来，写笔记的同时，Git 在后台默默同步到 GitHub 或 Gitee。

![](https://mmbiz.qpic.cn/mmbiz_png/zDicTibYTEOJqd61obVKs0PmET48jfWhT9sxISwr55NDpRKAHmibmohfsopq4YrjZHRwibK8cfV36aPTslKMnGSliaXUSHwIaG5JgGwKp51BEHjI/640?wx_fmt=png&from=appmsg)

### 远程仓库配置

#### 方式一：连接 GitHub

1. **「创建 GitHub 仓库」**
    

- 登录 https://github.com/
    
- 点击右上角「+」→「New repository」
    
- 填写仓库名（如 `my-obsidian-notes`）
    
- 选择 Public 或 Private
    
- 点击「Create repository」
    

3. **「在 Obsidian 中克隆仓库」**
    

- 打开 Obsidian 命令面板（`Ctrl + Shift + P` 或 `Cmd + Shift + P`）
    
- 输入「clone」
    
- 选择「Git: Clone an existing remote repo」
    
- 粘贴 GitHub 仓库地址（格式：`https://github.com/你的用户名/仓库名.git`）
    
- 选择本地存放位置
    

5. **「SSH 免密连接（推荐）」**
    

- 生成 SSH Key：`ssh-keygen -t ed25519 -C "your_email@example.com"`
    
- 复制公钥：`cat ~/.ssh/id_ed25519.pub`
    
- 在 GitHub → Settings → SSH and GPG keys → New SSH key 中粘贴
    

#### 方式二：连接 Gitee（国内访问更快）

1. **「创建 Gitee 仓库」**
    

- 登录 https://gitee.com/
    
- 点击右上角「+」→「新建仓库」
    
- 填写仓库名（如 `my-obsidian-notes`）
    
- 选择公开或私有
    
- 点击「创建」
    

3. **「在 Obsidian 中克隆仓库」**
    

- 同样打开命令面板
    
- 选择「Git: Clone an existing remote repo」
    
- 粘贴 Gitee 仓库地址（格式：`https://gitee.com/你的用户名/仓库名.git`）
    

#### 配置自动同步

安装好 Git 插件后，在设置中开启自动同步功能：

- 开启「自动提交」，设置时间间隔
    
- 开启「自动推送」
    
- 开启「启动时拉取」
    

具体选项名称在插件设置界面中可以找到。开启后，每次修改笔记，Git 会自动提交并推送到远程仓库，再也不怕笔记丢失了。

---

## 第二步：安装 Claude Code CLI

### 什么是 Claude Code

Claude Code 是 Anthropic 推出的 AI 编程工具，可以理解为「能直接操作文件的 ChatGPT」。它能读取代码库和文件、直接帮忙修改、运行终端命令。

在这里重点是文件，Markdown 也还是文件的一种，他在 AI 所以说 Markdown 被我称之为 21 世界 AI 时代最伟大的发明之一：[你可能不相信，我愿称Markdown是AI时代最伟大的发明之一](https://mp.weixin.qq.com/s?__biz=MjM5MzQyNDM1MQ==&mid=2247485389&idx=1&sn=1a4e86c59155c68fd1ab3500e44629cc&scene=21#wechat_redirect)

![Gemini CLI vs Claude Code vs Cursor - Which is the best option for coding?  - Bind AI](https://mmbiz.qpic.cn/mmbiz_png/zDicTibYTEOJpKBplVPrICtqhgVQnOkT3YJ3ViabHFalWcvatQgnsXzHMXicpzyAFZn2EuXrVj6g7qfKhFrZTs92Wce5ia9P8zHASbenQw7qoVrA/640?wx_fmt=png&from=appmsg)

### 安装方法

macOS/Linux 用户：

```
curl -fsSL https://claude.ai/install.sh | bash
```

Windows 用户（PowerShell）：

```
irm https://claude.ai/install.ps1 | iex
```

安装完成后，终端输入 `claude` 即可启动。首次登录请参考官方文档。

### 在 Obsidian 中直接使用：Claudian 插件

如果不想每次切换到终端，还可以在 Obsidian 里直接使用 Claude，那就是 Claudian 插件。

![Preview](https://mmbiz.qpic.cn/sz_mmbiz_png/zDicTibYTEOJoHcUToZp9FAicAzTQprYiazibwEsoic3BRPCcuj7327upxo8aic8MJdZj7yz9zLLbQa9zKkbTgQA1Bf4sPO0tExs8pv5TOzsVJjsYs/640?wx_fmt=png&from=appmsg)

**「注意」**：Claudian 暂时不在 Obsidian 官方插件市场，需要手动安装。有两种安装方式：

**「方式一：使用 BRAT 插件安装（推荐）」**

1. 先在插件市场搜索并安装「BRAT」插件
    
2. 启用 BRAT 后，打开设置
    
3. 在「Add beta plugin」中添加：`https://github.com/YishenTu/claudian`
    
4. 安装完成后启用 Claudian
    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zDicTibYTEOJoD6MEpOdRwUR1WN87le7ZNKjRuZtlnWIETBvQeapHEJ6CA2QHDcBL9DST2qwOOZYeUoicb65la9c1mLE0qmRWFIRpq2YsJQaMk/640?wx_fmt=png&from=appmsg)

**「方式二：手动安装」**

1. 访问 Claudian GitHub 仓库：https://github.com/YishenTu/claudian
    
2. 进入 Releases 页面，下载最新版本的 `main.js`、`manifest.json` 和 `styles.css`
    
3. 在 Obsidian 插件目录 `.obsidian/plugins/` 下创建 `claudian` 文件夹
    
4. 把下载的文件放进去
    
5. 重启 Obsidian，启用插件
    

---

## 第三步：配置多种大模型

### 为什么需要多模型

Claude Code 默认用 Anthropic 的 Claude 模型，但是国产大模型主打一个物美价廉，只需要 1/3 的费用享受相同的体验 Kimi、MiniMax、GLM 这些国产大模型。

Claude Code CLI 支持通过 API 配置模型，cc-switch 则可以快速切换，避免使用命令行 。

### cc-switch 安装

cc-switch 是一个模型切换工具，可以快速在不同模型之间切换。

![main-en.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zDicTibYTEOJphq4MeYsiaXqtydLGa7v6db0ADrC9kyPyf0icb6LnTmexibJfGPMicrOOH5WFMaunRxibHYgFtiaNbXMBVMvkQfn7Fp2jXiautCzO8Qc/640?wx_fmt=png&from=appmsg)

安装方法：

```
# macOS（Homebrew）
```

Windows / Linux 直接在 Releases 下载对应安装包：

https://github.com/farion1231/cc-switch/releases

### cc-switch 使用方法

安装好 cc-switch 后，打开桌面应用，你会看到一个模型列表界面。添加完配置后，选中模型，点击「Enable」启用，然后**「重启 Claude Code」** 使配置生效。

#### 添加 Kimi

1. 访问 https://platform.moonshot.cn/ 注册账号并获取 API Key
    
2. 在 cc-switch 中点击「Add Provider」：
    

- 名称：Kimi
    
- Provider：OpenAI Compatible
    
- Base URL：`https://api.moonshot.cn/v1`
    
- API Key：你的 Kimi API Key
    
- Model：`kimi-k2` 或 `kimi-k2.5`
    

#### 添加 MiniMax

1. 访问 https://platform.minimax.io/ 注册账号并获取 API Key
    
2. 在 cc-switch 中添加：
    

- 名称：MiniMax
    
- Provider：OpenAI Compatible
    
- Base URL：`https://api.minimax.io/v1`
    
- API Key：你的 MiniMax API Key
    
- Model：`minimax/MiniMax-M2.5`
    

#### 添加 GLM

1. 访问 https://open.bigmodel.cn/ 注册账号并获取 API Key
    
2. 在 cc-switch 中添加：
    

- 名称：GLM
    
- Provider：OpenAI Compatible
    
- Base URL：`https://open.bigmodel.cn/api/paas/v4`
    
- API Key：你的 GLM API Key
    
- Model：`glm-5`
    

#### 生效

添加完配置后：

1. 在 cc-switch 中选中模型
    
2. 点击「Enable」启用
    
3. **「重启 Claude Code」**（或在终端重新运行 `claude`）
    

切换完成后，Claude Code 会自动使用选中的大模型响应。

### 连通测试

配置完成后，可以在终端输入测试：

```
读取当前笔记，给我 3 条可以马上执行的改写建议。
```

能返回基于当前笔记内容的建议，就算打通。

---

## 第四步：Skills 系统让效率翻倍

### 什么是 Skills

Skills 是 Claude Code 的核心扩展机制，可以理解为「自定义指令包」。创建一个 Skill 后，可以用 `/skill-name` 直接调用，或者让 Claude 在合适的场景自动触发。

详情看这里：[我的股票跌了 72%，凶手居然是一个 127 行的 Skills Markdown 文件](https://mp.weixin.qq.com/s?__biz=MjM5MzQyNDM1MQ==&mid=2247485690&idx=1&sn=ca8493e3710fb2ae7ad90fff26268ef6&scene=21#wechat_redirect)

### Skills 推荐

obsidian 官网 Skills 安装：bunx skills add kepano/obsidian-skills

还推荐其他 Skills，安装命令：`bunx skills add davila7/claude-code-templates`

#### obsidian-markdown

Obsidian 专用，Markdown 笔记工作流，完美适配双向链接、标签管理。

#### obsidian-bases

把 Obsidian 变成轻量级数据库，用来做项目管理、阅读清单。

#### pdf-processing

处理 PDF，提取文本、表格，OCR 识别图片里的文字。

#### pdf-processing-pro

PDF 处理专业版，功能更全。

#### docx

Word 文档处理，读写 .docx 格式。

#### xlsx

Excel 表格处理。

#### pptx

PPT 制作。

#### spreadsheet

表格数据分析。

---

## 真实使用场景

### 场景一：跨时空的「年度回顾」

这简直是一面「照妖镜」。

年底了随口一问：「我今年都写了啥？」

Claude 穿透了几百篇零散的记录，给我拼出一份年度报告：原来这一年我写了 200 多篇笔记，最关心的话题不是「AI」也不是「效率」，而是「焦虑」。

原来我焦虑了整整一年。

没有这套组合，你根本不可能发现这件事。

### 场景二：跨笔记找关联

这个问题我想了三年，但一直想不明白。

终于有一次我问 Claude：「我有没有同时记过『睡眠』和『咖啡因』的内容？」

它从不同年份的笔记里翻出了我的自相矛盾：2019年我说喝咖啡提神，2021年我说睡不着是因为咖啡因，2023年我开始戒咖啡。

**「这不是 AI 在回答问题，是你自己在不同时间点的思考，在互相打脸。」**

### 场景三：让碎片自己长成文章

之前随手记了几十个碎片想法，关于某个话题的零散观点东一个西一个。

我对 Claude 说：「把这目录下所有关于 AI 的碎片整理成一篇完整的文章。」

它给我拼成了一篇结构清晰的初稿。我只需要补充几个数据、改改语气，一篇 3000 字的文章就出来了。

**「人类负责产生思考，AI 负责打扫卫生。这才是打开 AI 的正确方式。」**

### 场景四：做决定前问问过去的自己

面对一个选择纠结不定——要不要离开大城市？

突然想到或许之前的笔记里有点线索。问 Claude：「我有没有记过关于这件事的想法？」

它翻出了三年前一篇没写完的笔记，当时的纠结和现在一模一样。

**「原来这个问题我想了三年了。三年都没做出决定，说明什么？」**

### 场景五：让十年的笔记自己说话

突发奇想：如果让我十年的笔记自己说话会怎样？

问 Claude：「从我所有笔记里找出每年的今天我都在干什么。」

它读了几百个文件，给我拼出了一篇「2月16日的十年」。

2016年的我在写代码，2018年在西藏旅行，2020年在记疫情日记，2023年在纠结要不要离职。

**「你以为自己忘了，但它都帮你记着。」**

---

## 总结

私人 AI 工作室的作用不仅仅如此，你还可以通过 Skills 拥有自己的工作流 , 甚至你可以拥有自己 AI 员工：Agents Team ，开启自己的一人公司。

AI Agent 不再是程序员的专属，我断言 AI Agent 将会是 AI 发展的底座，他是一个通用架构，现在依托于 AI Agent 已经发展出很多新的架构和工具：比如 openClaw 、obsidian cli
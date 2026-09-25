# FAQ · 常见问题

> 按「现象 → 原因 → 怎么办」组织。看完还卡住，带上报错截图来 [Issues](https://github.com/looping-engineering/obsidian-cc/issues)。
>
> 📦 **装不上 / 看不懂命令行** → 先看 [INSTALL-HUMAN.md](INSTALL-HUMAN.md)（人类版傻瓜指南）。
> 🤖 **用 CodeBuddy 自动装** → 看 [INSTALL.md](INSTALL.md)（给 AI 读的执行手册）。

---

## 目录

- [一、安装类](#一安装类)
  - [我能直接把插件文件解压到 Vault 就用吗？](#我能直接把插件文件解压到-vault-就用吗)
  - [为什么这个插件不能像别的 Obsidian 插件那样一键装？](#为什么这个插件不能像别的-obsidian-插件那样一键装)
  - [我是小白，完全不会命令行，怎么装？](#我是小白完全不会命令行怎么装)
  - [`npm install` 卡住 / 超慢 / 下载失败](#npm-install-卡住--超慢--下载失败)
  - [`npm run package` 报一堆红色 TypeScript 错误](#npm-run-package-报一堆红色-typescript-错误)
  - [Obsidian 里看不到 Obsidian CC 这个插件](#obsidian-里看不到-obsidian-cc-这个插件)
  - [启用时报「找不到 claude / codex 二进制」](#启用时报找不到-claude--codex-二进制)
  - [能不能把 Mac 上装好的插件直接拷到 Windows 用？](#能不能把-mac-上装好的插件直接拷到-windows-用)
  - [Windows 上 `mklink` 报「拒绝访问」](#windows-上-mklink-报拒绝访问)
- [二、模型配置类](#二模型配置类)
  - [Codex 为什么不支持 DeepSeek、智谱 GLM？](#codex-为什么不支持-deepseek智谱-glm)
  - [DeepSeek / 智谱到底该怎么配？](#deepseek--智谱到底该怎么配)
  - [我用 Codex CLI 登录过了，插件里还要填 key 吗？](#我用-codex-cli-登录过了插件里还要填-key-吗)
  - [Claude 官方 / Claude Code plan 怎么配？](#claude-官方--claude-code-plan-怎么配)
  - [API Key 安全吗？会不会写进笔记？](#api-key-安全吗会不会写进笔记)
  - [用兼容网关时，点底部模型按钮跳到了设置页](#用兼容网关时点底部模型按钮跳到了设置页)
- [三、运行报错类](#三运行报错类)
  - [发消息没反应 / 报「无法连接 API」](#发消息没反应--报无法连接-api)
  - [Codex 引擎报 `Reconnecting…` 或 `UTF8 error`](#codex-引擎报-reconnecting-或-utf8-error)
  - [Codex 引擎报认证失败 / 401](#codex-引擎报认证失败--401)
  - [切了引擎之后，之前的对话怎么接不上了？](#切了引擎之后之前的对话怎么接不上了)
  - [启用后插件界面空白 / 没反应](#启用后插件界面空白--没反应)
- [四、使用类](#四使用类)
  - [「根目录展开」和「收拢进 obsidian-cc-workspace/」是什么区别？](#根目录展开和收拢进-obsidian-cc-workspace-是什么区别)
  - [Agent 会不会乱删我的笔记？](#agent-会不会乱删我的笔记)
  - [怎么更新插件？](#怎么更新插件)

---

## 一、安装类

### 我能直接把插件文件解压到 Vault 就用吗？

**不能。** 绝大多数 Obsidian 插件确实可以这样——下载 zip、解压到 `<Vault>/.obsidian/plugins/<插件名>/`、启用，就完事。

但 Obsidian CC 不行，因为它会在运行时**启动两个独立的程序**（内置的 `claude` 和 `codex` 二进制，合计约 200MB）。这两个二进制：

1. **不在源码里**，要靠 `npm install` 从 npm 下载（且按你的操作系统下载对应版本）；
2. **要靠 `npm run package` 把它们连同 `main.js` 一起打进分发包**。

所以直接解压源码会缺这两个二进制，插件一启用就报「找不到 claude/codex 二进制」。

→ 装法见 [INSTALL-HUMAN.md](INSTALL-HUMAN.md)（手动）或 [INSTALL.md](INSTALL.md)（让 CodeBuddy 自动装）。

### 为什么这个插件不能像别的 Obsidian 插件那样一键装？

因为它不是一个纯前端插件，本质上是**把一个本地 AI Agent 嵌进 Obsidian**——这个 Agent 跑在独立的子进程里（不是 Obsidian 的 JS 运行时），需要平台相关的原生二进制。这是它能驱动「多轮工具调用、读写文件、消化笔记」的前提，普通插件做不到这些。

代价就是安装多一步构建。我们用 CodeBuddy 自动化方案来抹平这个门槛（见下条）。

### 我是小白，完全不会命令行，怎么装？

**推荐用 [CodeBuddy Work](https://www.codebuddy.cn/work/) 自动装**，全程不用敲命令：

1. 下载安装并登录 [CodeBuddy Work](https://www.codebuddy.cn/work/)。
2. 在 Obsidian 里找到你的 Vault 路径（左下角点 Vault 名 →「打开文件夹路径」复制）。
3. 在 CodeBuddy 里打开本仓库源码，发一句：
   > 「按 INSTALL.md 帮我把插件装进 Vault，路径是 &lt;你上一步复制的路径&gt;」
4. 它会自动构建 + 装好。装完回 Obsidian 启用即可。

> 如果你想自己手动装（想学、或 CodeBuddy 不可用），看 [INSTALL-HUMAN.md](INSTALL-HUMAN.md)，每一步都带「卡点解释」。

### `npm install` 卡住 / 超慢 / 下载失败

**原因**：`npm install` 要下载约 200MB 的平台二进制（`claude` + `codex`），在国内网络下容易超时或中断。

**怎么办**：

1. **换淘宝镜像**（最常见有效）：
   ```bash
   npm config set registry https://registry.npmmirror.com
   ```
   装完想还原：`npm config set registry https://registry.npmjs.org`
2. **走代理**（你本机有梯子的话）：`npm install` 前设 `HTTPS_PROXY` 环境变量。
3. **只补装当前平台的二进制**（如果就差这两个包）：
   ```bash
   TAG=$(node -e "console.log(process.platform+'-'+process.arch)")
   npm install @anthropic-ai/claude-agent-sdk-$TAG @openai/codex-$TAG
   ```

### `npm run package` 报一堆红色 TypeScript 错误

**原因**：`npm run package` 会先跑 `tsc` 类型检查，源码里一些无害的类型告警会被当成错误拦下来，但其实不影响运行。

**怎么办**：跳过类型检查，直接用 esbuild 构建：

```bash
npm run dev          # esbuild watch，产出 main.js（跳过 tsc）
```

然后手动 staging（因为 dev 模式不自动产出 `dist/obsidian-cc/`）：

```bash
mkdir -p dist/obsidian-cc
cp main.js manifest.json styles.css dist/obsidian-cc/
cp -r skills helpers dist/obsidian-cc/
```

> 用 CodeBuddy 自动装的话，它遇到这个会自动走这条路，你不用管。

### Obsidian 里看不到 Obsidian CC 这个插件

按顺序排查：

1. **软链方向反了** —— 透过软链读不到 `manifest.json`。验证：
   ```bash
   ls "<Vault>/.obsidian/plugins/obsidian-cc/manifest.json"
   ```
   报「No such file」就是软链建错了，删掉重建（参考 [INSTALL-HUMAN.md](INSTALL-HUMAN.md) 的软链步骤）。
2. **Obsidian 没刷新** —— 按 `Cmd+R`（Mac）/ `Ctrl+R`（Win）重载，或完全退出 Obsidian 再打开。
3. **受限模式还开着** —— 设置 → 第三方插件 → 关闭「受限模式 / Safe mode」。
4. **装错位置了** —— 必须在 `<Vault>/.obsidian/plugins/obsidian-cc/` 下，注意是 `.obsidian` 这个隐藏文件夹里面。

### 启用时报「找不到 claude / codex 二进制」

**原因**：`npm install` 没把对应平台的二进制下载下来，或者你把别的平台装的拷过来了。

**怎么办**：

1. 回到源码目录，确认平台二进制存在：
   ```bash
   ls dist/obsidian-cc/node_modules/
   ```
   应能看到 `@anthropic-ai/claude-agent-sdk-<你的平台>` 和 `@openai/codex-<你的平台>`。
2. 缺了就补装（见上一条 `npm install` 失败的办法）。
3. **确认平台标签对得上**：在源码目录跑 `node -e "console.log(process.platform+'-'+process.arch)"`，输出的标签必须和 `node_modules` 里的包名后缀一致。

### 能不能把 Mac 上装好的插件直接拷到 Windows 用？

**不能。** 里面的 `claude` 和 `codex` 二进制是**平台专属**的：

| 你的系统 | 对应标签 |
|---|---|
| macOS Apple Silicon (M1/M2/M3) | `darwin-arm64` |
| macOS Intel | `darwin-x64` |
| Windows | `win32-x64` |
| Linux | `linux-x64` |

拷错了系统，二进制跑不起来，插件就报「找不到二进制」或直接无反应。**必须在你要用的那台机器上重新 `npm install`**，让 npm 自动下载对应平台的包。

### Windows 上 `mklink` 报「拒绝访问」

**原因**：误用了 `mklink /D`（符号链接），它需要管理员权限。

**怎么办**：改用 `mklink /J`（目录联接 / junction），**普通用户即可创建**，Obsidian 能正常识别：

```bat
cmd /c mklink /J "%VAULT%\.obsidian\plugins\obsidian-cc" "%SRC%\dist\obsidian-cc"
```

> 注意参数顺序和 Mac/Linux 相反：junction 是「**链接在前、源在后**」。

---

## 二、模型配置类

### Codex 为什么不支持 DeepSeek、智谱 GLM？

这是本项目被问得最多的问题，答案是**协议不兼容，不是我们故意限制**。

Obsidian CC 有两个引擎，它们调用的 API 协议完全不同：

| 引擎 | 走什么协议 | 谁的端点能用 |
|---|---|---|
| **Claude Code** | Anthropic Messages API | Anthropic 官方 **+ 任何 Anthropic 兼容网关**（DeepSeek、智谱 GLM、通义等都提供了这种端点） |
| **Codex** | OpenAI **Responses API** | 仅 OpenAI 官方端点（或 OpenAI 兼容的 Responses API 端点） |

关键点：

- DeepSeek 给的地址是 `https://api.deepseek.com/anthropic` —— **末尾的 `/anthropic` 就是「Anthropic 兼容」的意思**，它说的是「我可以假装自己是 Anthropic 的 API」。
- 智谱给的 `https://open.bigmodel.cn/api/anthropic` 同理。
- 而 Codex 引擎底层调的是 OpenAI 的 **Responses API**（`/v1/responses`），这跟 Chat Completions（`/v1/chat/completions`）是两套不同的接口。DeepSeek / 智谱目前都没提供 Responses API 兼容端点。

**所以**：DeepSeek / 智谱这类网关**只能配 Claude 引擎**，配到 Codex 引擎上一定连不通。

> 一句话记住：**端点带 `/anthropic` 的，只能配 Claude 引擎；要走 Codex 引擎，只能用 OpenAI 官方或完全兼容 Responses API 的端点。**

### DeepSeek / 智谱到底该怎么配？

两者都是 **Anthropic 兼容端点，只能配 Claude 引擎**。设置路径：Obsidian → 设置 → Obsidian CC。

**DeepSeek**：

| 字段 | 填什么 |
|---|---|
| Agent 引擎 | `Claude Code` |
| API Base URL | `https://api.deepseek.com/anthropic` |
| Model | `deepseek-v4-pro` |
| API Key | 在 https://platform.deepseek.com/api_keys 申请 |

**智谱 GLM**：

| 字段 | 填什么 |
|---|---|
| Agent 引擎 | `Claude Code` |
| API Base URL | `https://open.bigmodel.cn/api/anthropic` |
| Model | `glm-5.2` |
| API Key | 在 https://bigmodel.cn/coding-plan/personal/overview 申请 |

> 填完记得点底部对话栏的模型按钮确认当前引擎是 Claude Code，不是 Codex。

### 我用 Codex CLI 登录过了，插件里还要填 key 吗？

**不用填。** 如果你本机已经装了 [Codex CLI](https://developers.openai.com/codex) 并跑过 `codex login`：

1. 确认登录态在：终端跑 `codex login status`，或看 `~/.codex/auth.json` 是否存在。
2. 插件设置里：引擎选 `Codex`，**API Key / Base URL / Model 全部留空**。
3. 留空时插件自动回落到 `~/.codex` 的登录态和默认模型。

> 没装 Codex CLI 但想走这条路：先 `npm i -g @openai/codex` 再 `codex login`。

### Claude 官方 / Claude Code plan 怎么配？

**最省事**：拿到 Anthropic 的 API Key，引擎选 `Claude Code`，**只填 API Key**，Base URL 留默认（`https://api.anthropic.com`），Model 留默认即可。

如果你是 Claude Code 订阅用户、有专属 key，同样填到 API Key 字段就行，其他不用动。

### API Key 安全吗？会不会写进笔记？

**不会。** API Key 只存在 Obsidian 的插件配置区（`<Vault>/.obsidian/plugins/obsidian-cc/data.json`），**绝不会写进任何笔记文件**。所有 Agent 产物（报告、记忆、日志）都是不含 key 的普通 Markdown。

### 用兼容网关时，点底部模型按钮跳到了设置页

**这是正常的**。使用非官方端点（DeepSeek / 智谱 / 其他网关）时，模型名要填网关指定的（比如 `deepseek-v4-pro`、`glm-5.2`），无法在对话栏直接快切，所以点模型按钮会引导你去设置页填。

> 用官方 Anthropic 端点时，可以在对话栏底部直接快切模型，不会跳设置页。

---

## 三、运行报错类

### 发消息没反应 / 报「无法连接 API」

按这个顺序排查（覆盖 90% 情况）：

1. **引擎和端点匹配吗？** —— DeepSeek / 智谱只能配 Claude 引擎（见上面那条高频 FAQ）。这是最常见的连接失败原因。
2. **API Key 填对了吗？** —— 复制时别带前后空格；确认没把 Base URL 和 Key 填反了。
3. **Base URL 对吗？** —— DeepSeek 必须是 `https://api.deepseek.com/anthropic`（**别漏了 `/anthropic`**），智谱必须是 `https://open.bigmodel.cn/api/anthropic`。
4. **走代理了吗？** —— 如果你在国内用官方 Anthropic 端点，需要在「代理 URL」填代理地址；用 DeepSeek / 智谱通常不需要代理。

### Codex 引擎报 `Reconnecting…` 或 `UTF8 error`

**原因**：Codex 默认先用 WebSocket 打 Responses API，部分网络环境下会超时或断流。

**怎么办**：设置里开启「**强制 HTTPS 传输（禁用 WebSocket）**」（默认就是开的，如果你关过请打开）。它会强制走 HTTPS（SSE），更稳。

> 注意：这个选项只在**填了 API Key** 时生效；用 `codex login` 登录态时不生效（那种情况由 Codex 自己管传输）。

### Codex 引擎报认证失败 / 401

两种情况：

- **没填 key** → 必须先 `codex login`，否则没有登录态可用。
- **填了 key** → 确认是 OpenAI 官方的 key，不是 DeepSeek / 智谱的 key（后者不能用于 Codex 引擎）。

### 切了引擎之后，之前的对话怎么接不上了？

**这是设计如此，不是 bug。** Claude 和 Codex 两个引擎的上下文格式互不兼容，没法直接续接。切换引擎后，下一条消息会**开启新上下文**。历史记录仍然保留可回看；切回原引擎时，上下文会自动续接。

### 启用后插件界面空白 / 没反应

重载试试，按顺序：

1. `Cmd+R`（Mac）/ `Ctrl+R`（Win）重载 Obsidian。
2. 不行就完全退出 Obsidian（关窗口不够，要退出进程）再打开。
3. 还不行就在第三方插件列表里把 Obsidian CC **禁用 → 再启用**。

---

## 四、使用类

### Agent 会不会乱删我的笔记？

**不会**，有三重保护：

1. **写入确认门** —— 任何写文件或改文件系统的操作，默认都会先弹确认卡给你，你点同意才执行（除非你开 YOLO 模式）。
2. **`raw/` 永不可改** —— 原始材料目录由插件级写入拦截强制保护，Agent 只能读不能写删（连 YOLO 模式都拦）。
3. **自动快照 + 一键回滚** —— Agent 每轮写入前自动快照，对话里可以一键回滚（回滚也能撤销）。

可选还能开「每轮 Git 自动提交」，把 Vault 初始化成 Git 仓库，改动全程可追溯。

### 怎么更新插件？

如果你是用**软链方式**装的（CodeBuddy 自动装 / 按 INSTALL-HUMAN.md 手动软链），更新很简单：

```bash
cd <源码目录>
git pull
npm install          # 有新依赖时
npm run package      # 重新构建，软链自动指向新内容
```

然后在 Obsidian 里 `Cmd/Ctrl+R` 重载（或禁用→启用插件）即可生效。**不用重新拷贝、不用重新软链。**

> 如果你是直接拷贝 `dist/obsidian-cc/` 装的（没软链），更新后需要重新拷贝一次覆盖。推荐改用软链方式，省心。

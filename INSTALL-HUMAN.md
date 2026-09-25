# 手动安装指南（人类版）

> 给**完全不会命令行**的人看的傻瓜指南。每一步都告诉你：**做什么 → 敲什么 → 看到什么算成功 → 卡住了怎么办**。
>
> 🤖 **如果你更想省事**：用 [CodeBuddy Work](https://www.codebuddy.cn/work/) 自动装，全程不用敲命令，看 [INSTALL.md](INSTALL.md)（那份是给 CodeBuddy 读的）。
>
> ❓ **装的过程中遇到任何报错**：先查 [FAQ.md](FAQ.md)，高频问题都在那。

---

## 这个插件为什么装起来比别的麻烦？

先说清楚，免得你中途骂街。普通 Obsidian 插件 = 解压即用。但 Obsidian CC 在运行时会启动两个独立的程序（`claude` 和 `codex`，加起来约 200MB），这俩：

1. 不在源码里，要靠 `npm install` 下载（还会按你的系统下载对应版本）；
2. 要靠 `npm run build` 把源码编译成 Obsidian 能加载的 `main.js`。

所以你得先「构建」一下，不能解压源码直接用。**好消息是：整个过程在你解压源码的那个文件夹里完成，不用到处拷文件、不用搞软链接。装完一次，以后更新只需重新解压新包 + 两条命令。**

整个流程拢共 5 步，预计 15–30 分钟（主要是 `npm install` 下载时间）。

---

## 你需要先准备的东西

| 准备项 | 怎么搞 |
|---|---|
| **一台 Mac / Windows / Linux 电脑** | 必须桌面版，手机/平板不行 |
| **Obsidian 已装好，且建好了 Vault** | 没装去 https://obsidian.md 下；Vault 就是你放笔记的文件夹 |
| **插件源码 ZIP 包** | 群里 / GitHub 下载，下文教你放哪 |
| **一个能联网的网络** | 国内网络也行，下文会教你怎么加速 |

> 任何 AI 模型的 API Key 都可以**等装完再配**，安装阶段不需要。

---

## 第 1 步：找到你的 Vault 路径

Vault 就是你放 Obsidian 笔记的文件夹。**路径别猜，必须确认**，因为下一步要把源码放进去：

1. 打开 Obsidian。
2. 点**左下角你的 Vault 名字**（或者设置 → 关于）。
3. 点「**打开文件夹路径**」（Mac）或对应的「打开」按钮，会弹出文件管理器。
4. 文件管理器顶部的地址栏就是你的 Vault 路径，复制它。

典型长这样：

| 系统 | 路径样子 |
|---|---|
| Mac | `/Users/你的用户名/Documents/MyVault` |
| Windows | `C:\Users\你的用户名\Documents\MyVault` |

> 下文用 `$VAULT` 代指这个路径。

---

## 第 2 步：把源码解压到插件目录

这一步把源码放进 Obsidian 能找到的位置。

### 2.1 打开插件目录

在你的 Vault 下面找到（或新建）插件文件夹：

- **Mac / Linux**：`$VAULT/.obsidian/plugins/`
- **Windows**：`$VAULT\.obsidian\plugins\`

> 💡 `.obsidian` 是个隐藏文件夹。Mac 按 `Cmd+Shift+.` 显示隐藏文件；Windows 在资源管理器「查看」里勾选「隐藏的项目」。


### 2.2 解压源码

把拿到的 **源码 ZIP 包** 解压，把解压出来的文件夹重命名为 `obsidian-cc`，整个放进 `plugins` 目录。

解压后路径应该长这样：

```
$VAULT/.obsidian/plugins/obsidian-cc/
├── package.json
├── manifest.json
├── src/
├── ...
```

> ⚠️ **别多套一层文件夹！** 正确的是 `plugins/obsidian-cc/package.json`，不是 `plugins/obsidian-cc/obsidian-cc/package.json`。如果你解压出来多套了一层，把里面的文件挪上来。

### 2.3 如果之前装过，直接覆盖

检查 `plugins/` 下有没有旧的 `obsidian-cc` 文件夹：
- 有 → 直接覆盖即可


## 第 3 步：安装 Node.js（已经装过可跳过）

构建插件需要 Node.js（版本 ≥ 18）。先查一下你有没有——打开终端（Mac 在启动台搜 Terminal；Windows 开「命令提示符」或 PowerShell），**用 `cd` 进到刚才的插件目录**，然后敲：

```bash
node -v
```

> 💡 **怎么 cd 进去？** 在终端里打 `cd `（注意 cd 后面有个空格），然后把插件文件夹**从文件管理器拖进终端窗口**，路径会自动填上，回车即可。下文所有命令都在这个目录里敲。

- **显示 `v18` 或更高**（比如 `v20.11.0`）→ 已装好，跳到 [第 4 步](#第-4-步安装依赖并构建)。
- **显示「command not found」或「不是内部或外部命令」** → 没装，继续往下。

**装 Node 的方法**：

- **Mac / Windows**：去 https://nodejs.org ，下载 **LTS 版本**（左边那个按钮），双击安装包装到底。装完**关掉终端再重新打开**，重新 `cd` 进插件目录，再敲一次 `node -v` 确认能显示版本号。
- 或者用命令装（懂一点点的话）：
  - Mac（用 [nvm](https://github.com/nvm-sh/nvm)）：`nvm install --lts && nvm use --lts`
  - Windows：`winget install OpenJS.NodeJS.LTS`

> 💡 顺便确认 `npm -v` 也能显示版本（npm 跟着 Node 一起装）。看到版本号就 OK。

---

## 第 4 步：安装依赖并构建

> 确认你现在终端停在 `obsidian-cc` 目录里（就是有 `package.json` 的那个）。下文所有命令都在这里敲。

这一步最耗时（5–15 分钟，取决于网速），因为它要下载约 200MB 的二进制。

先换国内镜像（**国内用户强烈建议**，能快很多）：

```bash
npm config set registry https://registry.npmmirror.com
```

然后装依赖：

```bash
npm install
```

**看到什么算成功**：最后没有红色的 `ERR!`，出现一行类似 `added 240 packages in 3m`。

> 🔧 **卡住了？** 看 [FAQ · npm install 卡住/超慢](FAQ.md#npm-install-卡住-超慢-下载失败)。常见解法是挂代理或换镜像。

接着构建：

```bash
npm run build
```

**看到什么算成功**：终端输出构建完成，没有红色错误。这一步会在当前目录生成 `main.js`——这就是 Obsidian 要加载的插件主文件（`manifest.json` 和 `styles.css` 源码里本来就有）。

> 🔧 **报一堆红色 TypeScript 错误？** 多半是无害的类型告警。看 [FAQ · npm run package 报 TypeScript 错误](FAQ.md#npm-run-package-报一堆红色-typescript-错误)，改用 `npm run dev` 绕过。

---

## 第 5 步：在 Obsidian 中启用插件

文件就位了，但 Obsidian 默认不让第三方插件跑。这步**必须在 Obsidian 界面里点**：

1. 打开 Obsidian → **设置**（左下齿轮 ⚙️）→ **第三方插件**（Community plugins）。
2. 如果「**受限模式**」或「**Safe mode**」是开的 → **关掉**它。
3. 在「已安装插件」列表里找到 **Obsidian CC** → 把右边开关**打开**。
4. 左侧栏出现 ✨ 图标 = 启用成功 🎉

> 🔧 **列表里没有 Obsidian CC？**
> - 源码没放对位置 → 回 [第 2 步](#第-2-步把源码解压到插件目录)复查，确认 `manifest.json` 在 `plugins/obsidian-cc/` 下。
> - Obsidian 没刷新 → 按 `Cmd+R`（Mac）/ `Ctrl+R`（Win）重载，或完全退出再开。
>
> 🔧 **启用时报「找不到 claude/codex 二进制」？** 平台二进制没装好或系统不对。看 [FAQ · 找不到二进制](FAQ.md#启用时报找不到-claude-codex-二进制)。

---

## 第 6 步：配置模型（三选一）

启用后进 **设置 → Obsidian CC**。根据你手上的 key 选一条路：

### 🅰️ DeepSeek（最便宜，国内推荐）

| 字段 | 填什么 |
|---|---|
| Agent 引擎 | `Claude Code` |
| API Base URL | `https://api.deepseek.com/anthropic` |
| Model | `deepseek-v4-pro` |
| API Key | https://platform.deepseek.com/api_keys 申请 |

### 🅱️ 智谱 GLM（国内备选）

| 字段 | 填什么 |
|---|---|
| Agent 引擎 | `Claude Code` |
| API Base URL | `https://open.bigmodel.cn/api/anthropic` |
| Model | `glm-5.2` |
| API Key | https://bigmodel.cn/coding-plan/personal/overview 申请 |

注意，试用版本可能用不了 glm-5.2 的模型。

### 🅲️ Codex 内核（你已装过 Codex CLI 的话）

如果本机装了 [Codex CLI](https://developers.openai.com/codex) 并跑过 `codex login`：

1. 引擎选 `Codex`。
2. **API Key / Base URL / Model 全部留空**。
3. 插件自动复用 `~/.codex` 的登录态。

> ⚠️ **DeepSeek / 智谱不能配 Codex 引擎！** 它们只兼容 Anthropic 协议，Codex 只吃 OpenAI Responses API。详见 [FAQ · Codex 为什么不支持 DeepSeek/智谱](FAQ.md#codex-为什么不支持-deepseek智谱-glm)。

---

## ✅ 验证可用

1. 点左侧 ✨ 图标打开对话面板。
2. 发一句 `你好，介绍一下你自己`。
3. 收到正常回复 → 安装完成 🎉

> 🔧 **报「无法连接 API」？** 看 [FAQ · 发消息没反应](FAQ.md#发消息没反应-报无法连接-api)。九成是引擎和端点不匹配。

装完后建议点「开始 3 分钟基础设置」，让 Agent 帮你生成 `profile.md` 等配置。更多玩法见 [USAGE.md](USAGE.md)。

---

## 以后怎么更新？

拿到新版的源码 ZIP 包后，覆盖操作即可：

1. **删掉旧的插件文件夹**（`$VAULT/.obsidian/plugins/obsidian-cc/`）——你的笔记和配置不受影响，它们在别的地方。
2. **按 [第 2 步](#第-2-步把源码解压到插件目录)重新解压新版源码**到同一位置。
3. 在终端 `cd` 进去，敲：

```bash
npm install          # 装依赖
npm run build        # 重新构建，生成新的 main.js
```

4. 回 Obsidian 按 `Cmd/Ctrl+R` 重载（或禁用→启用插件）就生效了。

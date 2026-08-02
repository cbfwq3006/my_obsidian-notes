---
author: keen
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzA3MDQ0MDIxNg==&mid=2650008638&idx=1&sn=c5b3981a241d287ed9ef6011748e036a&chksm=86c8d12957139e4a23243417af0482a9e1f74de786f52444ffa34c904ce3d55c0890bd97cc54&mpshare=1&scene=1&srcid=0801VXoKkNjPMsFghyUnnZHI&sharer_shareinfo=e2bda4bdc9bbaf99675c40717f68324f&sharer_shareinfo_first=e2bda4bdc9bbaf99675c40717f68324f#rd
saved: 2026-08-01 23:20:43
tags:
  - 笔记同步助手
id: 3f82f3a8-9760-4ea5-8eef-c93ec9104e5b
---

公众号名称：KEEN的创享

作者名称：keen

发布时间：2026-08-01 10:38

**最近 DeepSeek 官方文档更新，正式放出了** **Codex 接入指南**。

这意味着，开发者现在可以直接在 OpenAI 的 Codex 体系里使用 DeepSeek 模型了。

目前支持的模型是 **deepseek-v4-flash**，`deepseek-v4-pro` 预计将在 2026 年 8 月初开放。

![[00 临时箱/images/b1ad23d328f950ea87e59e443e0c3629_MD5.png]]

---

### 为什么这件事值得关注？

Codex 并不是单一工具，而是一套完整的编程助手体系，包含：

-   Codex CLI
-   ChatGPT 桌面端
-   VS Code 的 Codex 插件

这三者共用同一套配置文件。只要配置一次，就能在命令行、桌面端和 IDE 里同步使用 DeepSeek 模型。

更关键的是，DeepSeek API **原生支持 Responses API**，这正是 Codex 与模型交互所使用的格式，因此接入门槛相对较低。

---

### 两种接入方式

#### 1\. 一键配置脚本（官方推荐）

DeepSeek 提供了自动化脚本，适合大多数用户。

**前提条件**：  
已经安装过 Codex CLI 或 ChatGPT 桌面端，并至少运行过一次（确保 `～/.codex` 目录存在）。

**macOS / Linux 用户** 在终端执行：

```
bash <(curl -fsSL https://cdn.deepseek.com/api-docs/codex-deepseek-setup.sh)
```

**Windows 用户** 在 PowerShell 中执行：

```
irm https://cdn.deepseek.com/api-docs/codex-deepseek-setup-en.ps1 | iex
```

脚本会自动完成以下几件事：

1.  备份现有配置文件
2.  写入模型目录（`models.json`）
3.  修改 `config.toml`，添加 DeepSeek 作为模型提供方
4.  进行语法校验，失败则不会改动任何文件

运行过程中会提示输入 API Key（以 `sk-` 开头），可在 DeepSeek 开放平台获取。

脚本支持重复运行，方便切换模型或恢复默认配置。

![[00 临时箱/images/9d7d5fdd40b9c6ce38005730732fb38c_MD5.png]]

  

#### 2\. 手动配置

如果更喜欢自己掌控细节，也可以手动操作。

首先创建或编辑 `～/.codex/models.json`，声明模型元数据。  
然后修改 `～/.codex/config.toml`，添加类似以下内容：

```
model = "deepseek-v4-flash"
model_provider = "deepseek"
preferred_auth_method = "apikey"
model_reasoning_effort = "high"
model_catalog_json = "～/.codex/models.json"

[model_providers.deepseek]
name = "deepseek"
base_url = "https://api.deepseek.com/"
wire_api = "responses"
experimental_bearer_token = "<你的 DeepSeek API Key>"
```

其中 `model_reasoning_effort` 控制推理强度，数值越高，模型思考越深入，回答质量通常更好，但耗时也会增加。

---

### 配置完成后如何验证？

-   **Codex CLI**：进入项目目录执行 `codex`，启动信息中显示对应模型名称即表示生效。
-   **ChatGPT 桌面端**：模型选择器中出现「自定义」选项。
-   **VS Code Codex 插件**：与 CLI 共用配置，安装后即可直接使用。

---

体验 DeepSeek V4 Flash 正式版显示用时花费，缓存命中率，按官方教程接入 Codex 使用量，如图

![[00 临时箱/images/1d3cb3fde15c09f679f4c9f55d776b41_MD5.png]]

### 写在最后

DeepSeek 这次把 Codex 的接入流程做得比较完整：既有一键脚本降低门槛，也保留了手动配置的灵活性，并且明确标注了当前支持的模型与后续计划。

对于已经在使用 Codex 生态的开发者来说，这相当于多了一个高性价比的模型选择；对于 DeepSeek 用户而言，则是把模型能力更顺畅地接入到了编程工作流中。

有兴趣的朋友可以直接去官方文档查看完整说明，或者先跑一遍一键脚本体验。

▼

**\-END-**

往期回顾：

[等了大半年的 V4-Flash-0731 来了，但实测后我心情有点复杂](https://mp.weixin.qq.com/s?__biz=MzA3MDQ0MDIxNg==&mid=2650008631&idx=1&sn=d488534626699677539fbc3e2f5289e8&scene=21#wechat_redirect)

[为什么越来越多人开始把 Claude 换成 Kimi K3？](https://mp.weixin.qq.com/s?__biz=MzA3MDQ0MDIxNg==&mid=2650008613&idx=1&sn=71bcd992d7e10c6212b2dfc310b7bae1&scene=21#wechat_redirect)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/fffde246_1785597641790?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA3MDQ0MDIxNg%3D%3D%26mid%3D2650008638%26idx%3D1%26sn%3Dc5b3981a241d287ed9ef6011748e036a%26chksm%3D86c8d12957139e4a23243417af0482a9e1f74de786f52444ffa34c904ce3d55c0890bd97cc54%26mpshare%3D1%26scene%3D1%26srcid%3D0801VXoKkNjPMsFghyUnnZHI%26sharer_shareinfo%3De2bda4bdc9bbaf99675c40717f68324f%26sharer_shareinfo_first%3De2bda4bdc9bbaf99675c40717f68324f%23rd&s=obsidian)
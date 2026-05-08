---
author: 路明修
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg2MjYyNTA4OA==&mid=2247484626&idx=1&sn=5879d97afc13450a079ade2e63c1903f&chksm=cf8efa13d045f76f05ba6ea92e305edac38f316a805d26f3a184bc4a941a2bb00dbdb2efa8c3&mpshare=1&scene=1&srcid=0508UtNmpoSk6lqBOQHR4YCc&sharer_shareinfo=290205ce88ea158670ef3160c954599d&sharer_shareinfo_first=290205ce88ea158670ef3160c954599d#rd
saved: 2026-05-08 09:35:08
tags:
  - 笔记同步助手
id: df35cbf7-bd0c-4f21-92e1-70133ad9c04f
---

公众号名称：路明修

作者名称：路明修

发布时间：2026-04-12 16:51

之前发了一篇利用ssh来控制CodeX的方案[为了在手机上操控 Codex，我把 WSL、Tailscale 和 tmux 全折腾了一遍](https://mp.weixin.qq.com/s?__biz=Mzg2MjYyNTA4OA==&mid=2247484483&idx=1&sn=aa8da1048a052da6954a5943727d1dfc&scene=21#wechat_redirect)

但是总是感觉太麻烦了点，评论区有人指出可以用cc-connect来连接，于是我就去了解了一下这个项目。发起他也和小龙虾一样可以连飞书和微信的，而且还不用自己配置通道，这不比我之前搞得简单多了吗？

于是就有了这篇文章

![[笔记同步助手/images/d18aac6743c4ec9edd95fc8880d6cd7c_MD5.png]]

## 🚀 快速开始

### 🤖 通过 AI Agent 安装配置（推荐）

> **最简单的方式** — 把这段话发给 Claude Code 或其他 AI 编码 Agent，它会帮你完成整个安装和配置过程：

```
请参考 https://raw.githubusercontent.com/chenhg5/cc-connect/refs/heads/main/INSTALL.md 帮我安装和配置 cc-connect
```

![[笔记同步助手/images/13e6e27f431986a128329bc50e726f52_MD5.png]]

### 📦 也可以手动安装

**通过 npm：**

```
# 稳定版
npm install -g cc-connect

# Beta 版（功能更新，可能不稳定）
npm install -g cc-connect@beta
```

> **微信个人号（Weixin ilink）：** 仅在 **Beta / 预发布** 中提供（`cc-connect@beta` 或 Releases 里带 `beta` / `prerelease` 的资源）。**稳定版**`npm install -g cc-connect`**暂时不包含**该通道，正式版上线前请以 Beta 说明为准。

## 飞书配置

## 第一步：创建飞书企业自建应用

### 1.1 进入飞书开放平台

访问 飞书开放平台 并登录你的飞书账号。

​

### 1.2 创建应用

1.  点击右上角「控制台」进入开发者后台
    
2.  点击「创建企业自建应用」
    

> 💡 **个人用户也可以创建**：飞书开放平台支持个人开发者创建应用，无需企业认证。

### 1.3 填写应用信息

| 字段 | 填写建议 |
| --- | --- |
| 应用名称 | `cc-connect`或你喜欢的名称 |
| 应用描述 | `CodeX连接手机` |
| 应用图标 | 上传一个喜欢的图标 |

## 第二步：获取凭证

### 2.1 进入凭据页面

在应用详情页，左侧导航栏点击 **「凭据与基础信息」**。

​

### 2.2 获取 App ID 和 App Secret

你会看到以下信息：

```
App ID:     cli_axxxxxxxxxxxx
App Secret: QhkMpxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ **重要**：请妥善保存这两个凭证，后续配置 cc-connect 时需要用到。App Secret 只会显示一次，如果忘记了需要重置。

![[笔记同步助手/images/3ea19b16749981a69809399c308a0d8b_MD5.png]]

### 2.3 配置到 cc-connect

直接发给CodeX帮你配置

![[笔记同步助手/images/806c382749545d6f8a81ed77bce386ba_MD5.png]]

也可在config.toml中配置

​

## 第三步：配置应用能力

### 3.1 启用机器人能力

左侧导航栏点击 **「应用能力」** → **「机器人」**

### 3.2 配置机器人信息

![[笔记同步助手/images/06ce16dbe1bb3307770df892868575bc_MD5.png]]

## 第四步：配置权限

### 4.1 进入权限管理

左侧导航栏点击 **「权限管理」**。

​

### 4.2 申请必要权限

在「权限配置」中搜索并添加以下权限（现在权限标识如果变化的话，可以直接看下面把我的配置复制导入）:

​

| 权限名称 | 权限标识 | 用途 |
| --- | --- | --- |
| 获取与更新用户基本信息 | `contact:user.base:readonly` | 获取用户信息 |
| 接收群聊消息 | `im:message.group:receive` | 接收群消息 |
| 接收单聊消息 | `im:message.p2p:receive` | 接收私聊消息 |
| 读取群消息 | `im:message.group_msg:readonly` | 读取群消息内容 |
| 读取单聊消息 | `im:message.p2p_msg:readonly` | 读取私聊内容 |
| 以应用身份发送群消息 | `im:message:send_as_bot` | 发送消息回复用户 |

也可以复制导入

```
{ "scopes": { "tenant": [ "contact:user.base:readonly", "im:message.group_at_msg:readonly", "im:message.group_msg", "im:message.p2p_msg:readonly", "im:message:send_as_bot" ], "user": [ "docx:document:readonly" ] } }
```

### 4.3 发布权限申请

配置完权限后，点击「申请发布」使权限生效。

![[笔记同步助手/images/48a8fe39b340b04805dbbe43af1fb3d9_MD5.png]]

到这里先把创建版本点了，然后配置发布。不然可能用不了长连接。

![[笔记同步助手/images/d5c7e137e7a01e6f41be71950ab5f2c1_MD5.png]]

然后把长连接的事件加上，加上这个再发布，飞书上的机器人就有对话框了

![[笔记同步助手/images/a8673d12adaa55420b95abc00caf2841_MD5.png]]

然后发布

​

## 第六步：启动 cc-connect

### 6.1 启动服务

```
cc-connect
# 或指定配置文件
cc-connect -config /path/to/config.toml
```

### 6.2 验证连接

启动后，cc-connect 会自动与飞书建立 WebSocket 长连接。你会在日志中看到：

```
level=INFO msg="platform started" project=my-project platform=feishu
level=INFO msg="cc-connect is running" projects=1
[Info] connected to wss://msg-frontier.feishu.cn/ws/v2?...
```

![[笔记同步助手/images/5f7d84abaeb5fa4012d22e75e9851138_MD5.jpg]]

这样就可以在自己飞书上面和CodeX对话了

顺便让CodeX可以常驻后台

![[笔记同步助手/images/06c010178d5fbacd7b6c46c1c6d06843_MD5.png]]

  

---

![[笔记同步助手/images/3d55d31a03b2fd79a1bcf5ac4c668c41_MD5.jpg|cover_image]]

原创 路明修 路明修

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/3ebf0d0c_1778204105608?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg2MjYyNTA4OA%3D%3D%26mid%3D2247484626%26idx%3D1%26sn%3D5879d97afc13450a079ade2e63c1903f%26chksm%3Dcf8efa13d045f76f05ba6ea92e305edac38f316a805d26f3a184bc4a941a2bb00dbdb2efa8c3%26mpshare%3D1%26scene%3D1%26srcid%3D0508UtNmpoSk6lqBOQHR4YCc%26sharer_shareinfo%3D290205ce88ea158670ef3160c954599d%26sharer_shareinfo_first%3D290205ce88ea158670ef3160c954599d%23rd&s=obsidian)
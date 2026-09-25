---
author: 丶平凡世界
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzA3MTg4NjY4Mw==&mid=2457349480&idx=1&sn=cf1502ff243814e72ccd49d22c21a6b5&chksm=89391dca19be05e9503011040f31b0dbcb86f7ba01e29fed77ab6c1a55d17188b021714b8fb9&mpshare=1&scene=1&srcid=0824n2fhVYt59d8HV8tM9PpE&sharer_shareinfo=4158b6939269195a598f88d764662475&sharer_shareinfo_first=4158b6939269195a598f88d764662475#rd
saved: 2026-08-24 17:05:13
tags:
  - 笔记同步助手
id: 51c1dcca-fb1a-4b06-91f7-bc99d2344071
---

公众号名称：李岳AI

作者名称：丶平凡世界

发布时间：2026-08-24 15:08

大家好，我是李岳。

最近知乎发布了Zhihu CLI，让搜索高赞帖子更加容易了，特别是一些做泛流量的用这个工具找帖子非常方便。

今天带你把 Zhihu CLI 装进 Codex。装好以后，你可以直接用命令搜索知乎内容、查看热榜、调用知乎直答，还能把搜索结果整理成标题、作者、链接、赞同数等结构化信息。

整个过程可以记成三步：

> 安装 → 授权 → 使用

## 一、Zhihu CLI 到底是什么？

CLI 是“命令行工具”的意思。你可以把 Zhihu CLI 理解成一个连接 Codex 和知乎开放平台的小助手：你负责提出问题，它负责把知乎的内容找出来。

它常用的能力包括：

-   搜索知乎内容，返回标题、作者、链接、评论数和赞同数；
    
-   查看知乎热榜；
    
-   搜索全网内容；
    
-   调用知乎直答；
    
-   查看自己的内容、收藏和关注内容。
    

![[00 临时箱/images/210ca60fd76fdd06c9f05396ce281ae7_MD5.jpg]]

## 二、准备工作

开始前准备好三样东西：

1.  已安装并能正常使用的 Codex；
    
2.  一个知乎账号；
    
3.  知乎开放平台的 Access Secret。
    

这里要特别提醒：Access Secret 是访问凭证，不是知乎登录密码。它和密码一样重要，不要发到群聊、文章、截图或 Git 仓库里。

## 三、在 Codex 中安装 Zhihu CLI

这一步很简单，只需要把这段提示词发送给Codex就可以安装成功了。

```
请下载安装 zhihu-cli skill 并完成初始化配置
https://developer-cdn.zhihu.com/zhihu-cli/releases/stable/skill/zhihu-cli-skill.zip
```

不一会儿就帮你把Skill和CLI都安装好了。

![[00 临时箱/images/2c299b4bf3ee29a64e6489a7cd01a0f1_MD5.png]]

## 四、获取 Access Secret

打开知乎开放平台的个人中心：

> https://developer.zhihu.com/profile

登录后找到 Access Secret，申请一个新的密钥并复制保存。

![[00 临时箱/images/126a5a86dc5ea0279d74d4b0b334aca4_MD5.png]]

## 五、完成授权配置

最简单的做法是使用 `auth set --secret-stdin`，让密钥通过标准输入传给 CLI，而不是放在命令参数里。

下面的代码只展示格式，尖括号里的内容要在你自己的电脑上替换：

```
"<你的 Access Secret>" | & $cli auth set --secret-stdin
```

如果你是在 Codex 里完成配置，可以直接告诉它：“请使用我的 Access Secret 初始化 Zhihu CLI”，然后只在私密输入区域提供密钥。

![[00 临时箱/images/28ae50cdb1565f5b10a71411421cffcf_MD5.png]]

## 六、第一次搜索知乎内容

### 1\. 搜索知乎站内内容

例如，在Codex里直接搜索“AI 工具”：

![[00 临时箱/images/011a56c8bfe2d59bff69fec6ab16d725_MD5.jpg]]

直接返回10条相关的帖子内容，包含对应的标题，类型，作者，赞同数和评论数等等。

也给出了终端PowerShell执行命令：

```
& "$HOME\AppData\Local\ZhihuCLI\current\zhihu-cli.exe" search zhihu --query "AI 工具" --count 10
```

用终端执行的话就不需要浪费Token了。

### 2\. 筛出超过 20000 赞同的内容

如果你要做“高赞帖清单”，可以让Code自动调用该CLI去执行 PowerShell 自动筛选：

![[00 临时箱/images/42e8db8c64d1a4e0f42b8117fe9ac69c_MD5.jpg]]

在执行过程中你会看到它使用的其实还是底层命令：

```
$$cli = 'C:\Users\liyue\AppData\Local\ZhihuCLI\current\zhihu-cli.exe'; & $cli search zhihu --query 'AI工具' --count 10
```

这段命令的意思很简单：把结果转成 JSON，留下赞同数大于 20000 的条目，只显示标题、作者、赞同数、评论数和链接。

注意，搜索结果是当前索引到的内容，赞同数可能会随着知乎页面变化；如果要发布文章或做正式统计，最好点击 `Url` 回到原文再核对一次。

![[00 临时箱/images/9a023743b3b50e9e4a95fd009f6c6957_MD5.jpg]]

## 七、用 Codex 批量整理高赞帖子

安装好之后，你不必每次都手动处理 JSON。可以直接把需求说清楚，例如：

> 请使用 Zhihu CLI，分别搜索“职场”“AI”“生活”“互联网”，每个领域返回 10 条赞同数超过 20000 的知乎帖子，整理为领域、标题、作者、赞同数、评论数和帖子链接。赞同数不足 20000 的不要返回，最后核对原文链接。

Codex 会把任务拆成搜索、筛选和整理三步。你也可以进一步要求它输出 Markdown 表格、CSV，或者按赞同数从高到低排序。

![[00 临时箱/images/dd7e53516c53b14c143a15a8aefc3f85_MD5.jpg]]

## 写到最后

Zhihu CLI 的核心并不复杂：先装 Skill，再配置 Access Secret，最后用自然语言或命令搜索内容。

从现在开始，找高赞帖不必靠手工翻页。

你负责提出问题，Codex 负责组织任务，Zhihu CLI 负责把知乎里的标题、链接和赞同数带到你面前，掌管高赞帖的神，算是正式上线了。

以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～

谢谢你看我的文章，我们，下次再见。

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/66acbc19_1787562311214?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA3MTg4NjY4Mw%3D%3D%26mid%3D2457349480%26idx%3D1%26sn%3Dcf1502ff243814e72ccd49d22c21a6b5%26chksm%3D89391dca19be05e9503011040f31b0dbcb86f7ba01e29fed77ab6c1a55d17188b021714b8fb9%26mpshare%3D1%26scene%3D1%26srcid%3D0824n2fhVYt59d8HV8tM9PpE%26sharer_shareinfo%3D4158b6939269195a598f88d764662475%26sharer_shareinfo_first%3D4158b6939269195a598f88d764662475%23rd&s=obsidian)
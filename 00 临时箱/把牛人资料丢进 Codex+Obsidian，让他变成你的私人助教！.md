---
author: 大瑜
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzk0ODcxNTI0OA==&mid=2247492169&idx=1&sn=1c1a5b51bb76b3c3a555f398252fc62a&chksm=c20c7217909f3e1efcd46923880b42a2d5f70eebc22e2ec344e71afcf47601e2be1ac791b600&mpshare=1&scene=1&srcid=080275NlwJaAqiAxMN25JLtH&sharer_shareinfo=098f1e5efbb67c21ed44f1a29c3a09e5&sharer_shareinfo_first=098f1e5efbb67c21ed44f1a29c3a09e5#rd
saved: 2026-08-02 21:18:22
tags:
  - 笔记同步助手
id: c0712b34-3d87-4f86-a68f-ac63053e9dbb
---

公众号名称：大瑜聊AI

作者名称：大瑜

发布时间：2026-07-21 19:40

在没有AI之前，大家收集资料都是保存到微信收藏夹中一丢！

看起来，是收藏了，其实是资料的浪费。

譬如说你在网上看到一个和牛逼的博主，但是能和博主对话的机会有限。

现在不一样了！

只需要将这个博主的公众号、视频号内容下载到raw中。通过在codex+obsidian重新盘活这些资料。

简单的来说就是让这个博主变为你的私人助教。

![[00 临时箱/images/19b1b30e34627f7c2c0910d7fda0842f_MD5.png]]

下面就给大家展示具体的步骤。

# 步骤1: 收集博主的资料

所谓巧妇难做无米之炊，第一步就要去各种数据来源收集这个博主的全部信息。

![[00 临时箱/images/e4cba15b6a38ba2ce9a82877f4a6216f_MD5.png]]

## 1、网页收藏可以用obsidian web cliper的插件

## 2、公众号文章写在可以用下面的skill

https://clawhub.ai/harven-droid/skills/wechat-article-archive

![[00 临时箱/images/1553dec76c52aa02c9117227f80e6957_MD5.png]]

3、PDF/word的转化可以用Markitdown File Converter这个插件，转换为md文件。

也可以让codex自己去写代码，给你的PDF转化为md文件。

![[00 临时箱/images/4801677d66deb3d527f9da175830ae93_MD5.png]]

4、视频下载可以用yt-dlp 的这个插件，将视频下载到本地， 然后借助Whisper再转化为逐字稿。

```
只需要这样说：将yt-dlp这个插件，下载我的视频地址，xXXXXXX
然后用Whisper转化为逐字稿，如果本机没有安装，请帮我安装。
最后整体进行错别字的修改，想成md文档，保存到raw/shipin目录中。
```

# 步骤2: 将内容转化到wiki中

只需要将下面的提示词发给codex。

```
按照卡帕西的思路，将raw里面没有进入wiki的内容，导入到wiki中。
严格按照当前 AGENTS.md 执行：
1、内容初级总结放到wiki/sources中
2、如果资料里有值得长期复用的概念、方法论或术语，
可以另存到 wiki/concepts/，但不是必做项。
3、提取值得长期维护的“实体—关系—实体”，更新所有的实体页，建立关联关系图谱。
4、提问的问题和回答，整理到wiki/questions 目录，便于知识库继续优化
```

最终形成这样的知识图谱。

![[00 临时箱/images/a35cd5254bead07ca80851accad5e54f_MD5.png]]

# 步骤3: 开始提问

当然，这个比网上的“乔布斯skill”、“张雪峰skill”要好很多。

举个例子：你知道你整理的资料来源自那些文章，还知道你你资料被哪些内容引用。

所以，你可以问：

```
如果一个产品，推广的时候，用户觉得贵怎么回复他
```

就会按照wiki的内容给你推荐。

![[00 临时箱/images/dec1dc2a7f07ce1d31c30ac6233a4dc3_MD5.png]]

更重要的是，借助 Obsidian 的双链和外链体系，你还能清楚看到回答背后的资料来源。

这才是知识库真正强大的地方。

![[00 临时箱/images/74452fccf57205c2569492e74d3040ee_MD5.png]]

# 写在后面的话

当然，这就是知识库的强大之处，你可以将之前的所有资料都入库，然后帮你：

1、根据之前的内容，清晰回答你的问题。

## 2、结合内容的整理，形成行业的报告

## 3、借助image2的功能，快速生成小红书内容

4、借助hyperperframe的插件，快速生成简单的口播视频。

现在是时候借助codex+obsidian开启你的AI知识库之旅了。

我是大瑜，关注大瑜，分享更多AI知识。

历史文章：

[人不在电脑前，如何用手机继续控制 Codex？两种方法讲清楚！](https://mp.weixin.qq.com/s?__biz=Mzk0ODcxNTI0OA==&mid=2247492131&idx=1&sn=348e1708956567760d4ae5ddd90c1d35&scene=21#wechat_redirect)

[这个skill可以下载公众号和小绿书！](https://mp.weixin.qq.com/s?__biz=Mzk0ODcxNTI0OA==&mid=2247492119&idx=1&sn=4b3b498875fe63a9ad7a34c48e6d4a56&scene=21#wechat_redirect)

[一本文字都选不中的 PDF，我用 Codex + Obsidian 做成了知识库！](https://mp.weixin.qq.com/s?__biz=Mzk0ODcxNTI0OA==&mid=2247492092&idx=1&sn=a7264cb8e4bed7ccb21982c3d0392692&scene=21#wechat_redirect)

  

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/81642e42_1785676699732?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzk0ODcxNTI0OA%3D%3D%26mid%3D2247492169%26idx%3D1%26sn%3D1c1a5b51bb76b3c3a555f398252fc62a%26chksm%3Dc20c7217909f3e1efcd46923880b42a2d5f70eebc22e2ec344e71afcf47601e2be1ac791b600%26mpshare%3D1%26scene%3D1%26srcid%3D080275NlwJaAqiAxMN25JLtH%26sharer_shareinfo%3D098f1e5efbb67c21ed44f1a29c3a09e5%26sharer_shareinfo_first%3D098f1e5efbb67c21ed44f1a29c3a09e5%23rd&s=obsidian)
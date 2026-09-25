---
author: 袋鼠帝
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA==&mid=2247518993&idx=1&sn=6a46f194133dd904aac1044c11260cb5&chksm=c1277f6d9b52b3db55d8d1960a5bfd928c1dc9428fdd55ecba6ebfb04763667de3a04ed5a0ad&mpshare=1&scene=1&srcid=0803kBWg53nVxJopLexrIjZn&sharer_shareinfo=d42ab53b3f82c1d8fc7ae01a8c5579fb&sharer_shareinfo_first=d42ab53b3f82c1d8fc7ae01a8c5579fb#rd
saved: 2026-08-03 13:03:23
tags:
  - 笔记同步助手
id: 2a87bd54-4d1a-4a13-9edf-66e2df68b249
---

公众号名称：袋鼠帝AI客栈

作者名称：袋鼠帝

发布时间：2026-08-03 08:30

大家好，我是袋鼠帝

昨天发布了DeepSeek V4 Flash正式版接入Codex的文章、视频。反响还不错。

![[00 临时箱/images/2154a59ae57b018e2bd1465b512b3c08_MD5.png]]

我实测下来，感觉DeepSeek V4 Flash，作为Flash模型，居然都快赶上国内第一梯队的旗舰模型了。

让我特别期待接下来的V4 Pro正式版，感觉会是个大招。

不过评论区有朋友好奇接入WorkBuddy的效果，我也挺想试试，于是我答应了。甚至这位朋友表示，WorkBuddy会比Codex更省Token。

![[00 临时箱/images/84d1180a0129c0ec756d1b94827e3704_MD5.png]]

所以这篇，它来了～

正好，前两天看到卡子哥讲了workbuddy的新功能，那这篇我们就来个新鲜组合（very fresh）：

![[00 临时箱/images/b8b02d0c0439953ffce15057248de0fe_MD5.png]]

结合WorkBuddy的新功能来看看DeepSeek最新的V4 Flash正式版+WorkBuddy到底怎么样？

还没了解DeepSeek V4 Flash正式版的朋友可以先看看我[上一篇文章](https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA==&mid=2247518938&idx=1&sn=4403836b501bf5d50119f4504c492b4b&scene=21#wechat_redirect)，这里就不赘述了。

总结就是，能力强，速度快，价格屠夫～

我们先一起看看WorkBuddy的新功能

简单来说，就是你和你的同事，你和你的AI，甚至你的AI和同事的AI，都能在同一份文档上同时干活了！

也是业内首次做到了人人、人机、机机（怎么有点别扭呢🤣）多端同步协同。

Word、Excel、PPT、MD等常见的本地文档都可以操作，还打通了云端的腾讯文档。

这对大家办公效率非常有帮助，早点干完活儿就可以悄悄摸鱼啦～

![[00 临时箱/images/18b822311a59980a77811f28f8f1bfc8_MD5.jpg]]

首先，人机协作很直观，就是WorkBuddy中生成的文件，你现在终于可以在右侧边栏中直接进行修改了，像下面这样。

![[00 临时箱/images/109a7fcfed54adebb9079ea29e1ee9fd_MD5.png]]

Codex目前能在右侧栏展示，但并不能直接修改。

它的修改按钮藏的巨隐蔽，我也是偶然才找到的。而且它只能修改，不能在文件里面直接跟AI协作。

![[00 临时箱/images/cd6e09b3a82c622ef6936e1d7ff52d63_MD5.png]]

说不如做，待会儿带你们实践一下，就懂了。

在这之前，我们先把DeepSeek最新的V4 Flash正式版接入WorkBuddy

其实WorkBuddy自带了DeepSeek V4 Flash模型，但是我不清楚它是不是最新的。

所以我决定走DeepSeek官方API

WorkBuddy这点就很好，它能自定义接入各家的API，甚至中转站的都行。非常灵活，这也是我喜欢用它的原因之一。

我们去DeepSeek API开放平台上新建一个apikey

![[00 临时箱/images/06e015e484f185d3ba1e4c90cd2ed88f_MD5.png]]

复制粘贴到workbuddy的自定义配置模型的apikey这里，提供商选DeepSeek。

模型选择DeepSeek-V4 Flash

![[00 临时箱/images/cd1768984bb71ac6eee0656eddda3a81_MD5.png]]

这样就搞定了。

使用的时候在自定义模型里面选择DeepSeek V4 Flash即可。

![[00 临时箱/images/d61d3baa25eda2c6ec1b66624cd59132_MD5.png]]

接下来我用入驻WorkBuddy的仓颉Skill蒸馏了《纳瓦尔宝典》这本书。

整个过程跑了35分钟，贼顺畅完全不卡，蒸馏出来17个Skill。

![[00 临时箱/images/46e9835b3ca05f9b167d26e9f6865c66_MD5.png]]

![[00 临时箱/images/4d48091351e69cd55d4c057eb1ab50a7_MD5.png]]

然后，我来完整的演示一次人机协作，确实很方便。

文件而且还能跟腾讯文档、腾讯Ima打通。还可以一键分享到朋友圈～

![[00 临时箱/images/15d79d72b09f9cef63d38055a691b331_MD5.jpg]]

> 📹 此处为视频内容（vid: wxv\_4631675574569156608）（上图为封面），未能直接提取，请前往原文查看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA==&mid=2247518993&idx=1&sn=6a46f194133dd904aac1044c11260cb5&chksm=c1277f6d9b52b3db55d8d1960a5bfd928c1dc9428fdd55ecba6ebfb04763667de3a04ed5a0ad&mpshare=1&scene=1&srcid=0803kBWg53nVxJopLexrIjZn&sharer_shareinfo=d42ab53b3f82c1d8fc7ae01a8c5579fb&sharer_shareinfo_first=d42ab53b3f82c1d8fc7ae01a8c5579fb#rd)

还有一个让我觉得非常实用的点是，PPT这块

比如我找到一个之前生成的简单的PPT（完全没有什么审美对吧）

![[00 临时箱/images/af9bb5ecaa31395eca3452e7f76c5a98_MD5.png]]

接着，又让DeepSeek V4 Flash帮我设计调整一套具有高级感的PPT，整体风格参考KFC品牌发布的视觉调性。

经过优化后是不是比之前好看多啦。

![[00 临时箱/images/40ca64c2710a34d760768972fbcbfc6a_MD5.png]]

毕竟DeepSeek V4 Flash的前端能力目前排世界第7了，审美还是不错的。

![[00 临时箱/images/8697b4510957f8042e6df033245154a2_MD5.jpg]]

接下来就是我觉得更舒服的操作了

WorkBuddy这里有个很好用的框选标注，框选这部分内容，提出修改要求。

![[00 临时箱/images/8ff9f447ae2d5dd2c370ded117074784_MD5.png]]

就能生成你想要的效果！而且修改后的效果是跟PPT完全适配的，不会乱改。

![[00 临时箱/images/2438e540b2ec265d9caf918d8b6c3ad8_MD5.png]]

感觉还差点东西，右边再加一个拿着早餐的袋鼠吧😄

嗯，这样就对了。

![[00 临时箱/images/fa9cf6ac923dce92fc05cf7a2752df63_MD5.png]]

是真心好用。

说实话，在所有的文件中，我最怕改PPT。

改过PPT的朋友应该知道，如果想加个图，或者加一段字，你可能要去调整布局。然后图应该怎么放，什么图加进去之后不违和，要考虑的东西挺多的。

而且经常会一不小心，就把版式搞乱了，贼烦。本来目的是为了去做汇报、讲解，但是光调整一个PPT版式可能就花了一半时间....

如果想改PPT的字，我们可以手动改：

就是说，简单的事情，我们可以手动完成，复杂的交给AI搞。因为改个字这种小事情，始终还是人来更快吧。如果用AI，你还得告诉它，然后它还要吭哧吭哧分析，绕弯路。

我们最终目标是省事儿、省时间。所以，人机协作这件事儿还是非常有必要。

WorkBuddy还可以和腾讯文档丝滑的打通，这就是大厂的生态。

在更多->腾讯文档这里，授权一下，就能看到最近访问过的一些文档，以及自己的文档。

![[00 临时箱/images/42f054ffab8f7d1f15dccc59d1ca1a98_MD5.png]]

仅仅是关联肯定不够，鼠标移动到某一个文档后面，会出现一个图标，点击可以直接把这个文档添加到workbuddy 对话框，纳入任务～

![[00 临时箱/images/95d5877a6b597ff9c83e01d089b0d1a6_MD5.png]]

cow-kg-desk是我前年用过的文档，长下面这样

![[00 临时箱/images/8c0ec71797488a0490abc17b836632fb_MD5.png]]

添加到任务后，可以直接在workbuddy里面让AI操作，甚至还能让把飞书那边的表格信息追加进去。

![[00 临时箱/images/978a7919e8f2a26d355deb089016fc4f_MD5.png]]

_说实话，这也是我最喜欢用workbuddy的一个点，就是它虽然用自家生态最丝滑，但是也不排斥别家的，很包容。_

_灵活度又高，包容度又高，这让workbuddy用起来就很方便。我想，这也是大多数人 选择它的重要原因之一吧。_

最终完成的很好，补充了优先级那块，然后也把飞书多维表格里面的信息追加过来了。

![[00 临时箱/images/2ec9def18e7f385e704ed0f2d1d00e50_MD5.png]]

基于腾讯文档，还可以丝滑的让你的workbuddy跟你的同事协同，一起修改同一份文件。

同样的，也可以让你的workbuddy和你同事的buddy协同

对于我自己来说，我最早联想到两个场景，给大家分享一下（希望有启发）：

1、人机协作：针对我们这种写公众号文章的，确实需要用 AI 来辅助。人机协作能让创作这一块更丝滑。

比如，我之前有几期视频的口播文案是请的一位兼职朋友帮忙的，他会把文案放在腾讯文档发给我，这其实用workbuddy来协作也会非常方便。

![[00 临时箱/images/84190384068a13a9ce6e1ae5727ad2dc_MD5.png]]

2、机机协作我觉得能解决开发者之前的一个痛点：

比如以前大家开多个 Claude Code 去开发功能时，很多时候不敢让多个 Agent 去改同一个功能或者同一个文件，因为可能会造成混乱、冲突。通常都是给它们分配毫不相关的两块任务。

而我感觉机机协作刚好就能解决这个问题。可能会极大地提高多agent开发同一个功能的效率。我接下来也准备尝试一下。

为什么我说WorkBuddy + DeepSeek是Agent时代的Office工作台呢？

这里+DeepSeek是因为，它确实是价格屠夫，而且就我这两天测试下来。即便是Flash模型也很强了，关键速度还快。

我只能说，DeepSeek 真是打破了模型的一个不可能三角，就是一个模型，几乎不可能做到既好用，又快，又便宜。。

但我觉得DeepSeek一定程度上做到了，我只能说respect🫡

咱们普通人办公，用一用AI，不就是图个便宜、好用、快捷嘛。

**「最后」  
**

给大家分享一个我的暴论，也是我认为未来一定会有的形态（不一定正确）：

我觉得未来App等一切用手操作的东西都会消失。

最终的入口就是AI入口，我们会先以打字的形式跟它交互，后续会完全通过语音，再到后来是通过脑机接口，通过意念。

所有的事情都可以交给AI帮我们完成。代码可能会成为非遗。

从这次workbuddy的新功能来看，Agent已经在开始慢慢吃掉Office场景了。

也就是说，以后这些原本需要在办公软件上操作的事情，慢慢会聚拢在Agent里面。

进而，我上面说的暴论已经初见端倪。

所以，我有时候在想，这些模型卷前端的Coding能力，从未来来看，是没有意义的（因为我觉得未来不存在操作界面了）。

最该卷的还是Agent能力，还有后端Coding的能力。还有感知现实世界的能力。

你怎么看，欢迎在评论区交流～

我是袋鼠帝，一个致力于帮你把AI变成生产力的博主。我们下期见。

能看到这里的都是凤毛麟角的存在！

如果觉得不错，随手点个赞、在看、转发三连吧～

如果想第一时间收到推送，也可以给我个星标⭐

谢谢你耐心看完我的文章～

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/ccabff90_1785733401519?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzkwMzE4NjU5NA%3D%3D%26mid%3D2247518993%26idx%3D1%26sn%3D6a46f194133dd904aac1044c11260cb5%26chksm%3Dc1277f6d9b52b3db55d8d1960a5bfd928c1dc9428fdd55ecba6ebfb04763667de3a04ed5a0ad%26mpshare%3D1%26scene%3D1%26srcid%3D0803kBWg53nVxJopLexrIjZn%26sharer_shareinfo%3Dd42ab53b3f82c1d8fc7ae01a8c5579fb%26sharer_shareinfo_first%3Dd42ab53b3f82c1d8fc7ae01a8c5579fb%23rd&s=obsidian)
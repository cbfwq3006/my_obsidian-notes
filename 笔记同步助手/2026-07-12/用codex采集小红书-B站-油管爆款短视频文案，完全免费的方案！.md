---
author: 菜哥
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247538009&idx=1&sn=349bd52182eaa2cd8acfdfb90b4bf5e1&chksm=96670bcb2c016482641523a157ee1ecc0652099477fc5cd658f5db28de152d90a643080ef806&mpshare=1&scene=1&srcid=0712ANRvnPTjgdF6kVCrPtEJ&sharer_shareinfo=bd6075f51ebb17596ce370640e3bd83b&sharer_shareinfo_first=bd6075f51ebb17596ce370640e3bd83b#rd
saved: 2026-07-12 11:51:38
tags:
  - 笔记同步助手
id: 34899307-3876-4ee1-8ef0-918e17ef8f30
---

公众号名称：菜鸟学Python

作者名称：菜哥

发布时间：2026-06-26 20:33

##### _👇我的小册 54章教程:**(**_**_[小白零基础用Python量化股票分析小册](http://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247526909&idx=1&sn=01c67f5745217ecd2647f30b6a96a4b7&chksm=978bfe32a0fc77244c63df78ec6395a7a05781293b81890dc7ca9e5e4bace32af4851b943009&scene=21#wechat_redirect)_****_)_** _,_**原价299，限时特价2杯咖啡，满100人涨10元。**__

  

大家好，我是菜哥！

今天又来解锁一个codex的新技能，经常刷短视频的同学肯定有这样的需求，比如我看到某一个短视频非常不错，它的文案，它的框架，我想进行模仿或在进行二创，但是需要采集它的短视频。这个怎么弄？

一般来说需要插件或在第三方的工具，但是都是需要付费的，今天我教大家用codex来搞定，完全免费。

## 1.需要一个语音转文字的API

  

我们要去扒这些爆款的视频，需要有一个东西，就是语言转文字，因为视频都是有声音有文案的，而这个文案都是音频，我们需要用一个api把这个音频转文字。

打开硅基流动 官网：

打开 https://www.siliconflow.cn，然后需要手机号注册一下，目前是需要实名（以前我用的时候不需要）

![[笔记同步助手/images/2683ccfe3c07eb76bcd374b7d4bc337e_MD5.png]]

实名好了之后，在左侧的菜单，找到这个API密钥， 点击新建API密钥，然后把这个描述写一下（否则你建了太多自己都弄不清楚）

![[笔记同步助手/images/f993a96ac7ee48b933ca1f8feddd98c6_MD5.png]]

建好之后就是这样的：

![[笔记同步助手/images/6623d672a1c4a61ac7436be4589a5ae8_MD5.png]]

然后我们需要去选择一个语音模型，这个后面有用！

## 2.打开codex

  

我们打开codex，然后新建一个项目，项目的名字叫"爬全网短视频爆款文案"（这个名字可以自己随便起），然后权限直接开完全访问

![[笔记同步助手/images/eb246e2f983dece47c386a9614ba791d_MD5.png]]

然后输入一段提示词：

![[笔记同步助手/images/b9a6d276cfc6e0f7c0b4fb64c385823d_MD5.png]]

大概10几分钟，codex会把要安装的依赖包全部搞定，然后最后会把运行的方式也告诉你。

![[笔记同步助手/images/3e5751aeed54b24ef917b78ffc315729_MD5.png]]

其实就是一个python工程文件，但是我们肯定不自己去运行，我们让codex 给我们运行，我们只需要喂给它视频链接即可。

## 3.爬取爆款视频文案

  

我们试一下这个工具效果如何，比如我在小红书上找一个视频：比如纳瓦尔的这个视频

![[笔记同步助手/images/73beed13c6edb3627a44779d1ab7b3ea_MD5.png]]

然后我们复制这个视频的链接，让codex解析看看：

![[笔记同步助手/images/6834899178066feb555c1fcc87ce6492_MD5.png]]

大概19秒就搞定了，我们再试一个中文的：

![[笔记同步助手/images/441bed75a4c826810eccaa9ecce88d98_MD5.png]]

然后让codex采集一下看看：

![[笔记同步助手/images/3bb54387ec25472a7a76a2ad9c9fc68c_MD5.png]]

是不是非常厉害，codex这个功能对做自媒体内容工厂的人来说，非常有用，商业价值非常大！

限于篇幅，没有展开讲。我会继续挖掘codex AI内容工厂的这方面的能力，有兴趣的可以加入我们下面的“AI编程与智能体实战”星球。

**![](https://relay-1.bijitongbu.site/p/b3c1762bbbdb715005e95fe18ebcd362.png)**

往期热文:

[刚开始用 Codex，一定要知道的 10 条技巧！](https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247537857&idx=1&sn=620b91917f2de9e934619a12266f6055&scene=21#wechat_redirect)

[太牛了，我把一份 30 页 PDF 丢给 Codex,只用一句提示词，十来分钟出了一份商业级 PPT!](https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247537909&idx=1&sn=81b820576597e70ba38608241235bfd3&scene=21#wechat_redirect)

[AI编程太香了：我用10分钟，做了一个简易版Trading view 看盘网站，省下了3000块！](https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247537811&idx=1&sn=9b49385e9a04dcfddbbef5f40953fa07&scene=21#wechat_redirect)

[没有团队，没有融资，他一个人靠开发网站一年赚千万！](https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247537128&idx=1&sn=e29ac2206475761a08dda52984681818&scene=21#wechat_redirect)

[AI编程开发小程序，有人已经日入1千，赚了10万块了！](https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247537122&idx=1&sn=b1448c7da5c09619b84c208d67171113&scene=21#wechat_redirect)

[30分钟！开发了“全能手电筒补光”小程序！](https://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247537081&idx=1&sn=ffe680f5d14d1aa1df5eac09bfcb71e6&scene=21#wechat_redirect)

目前我们星球是有AI智能体教程和AI编程零基础开发微信小程序的教程（可以学1整年，一整年才99，一天3毛都不到，非常划算，外边的智能体课程都是399起步），我们会教你全套的从零开始如何用AI编程开发小程序+副业变现 以及智能体的用法；

有兴趣的可以看看。我自己也在全力深耕这个赛道，欢迎志同道合的小伙伴加入我们！

![[笔记同步助手/images/455478f77f52b3e6b0b876d8b9f7402e_MD5.png]]

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/7870a36c_1783828296511?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIxNjM4NDE2MA%3D%3D%26mid%3D2247538009%26idx%3D1%26sn%3D349bd52182eaa2cd8acfdfb90b4bf5e1%26chksm%3D96670bcb2c016482641523a157ee1ecc0652099477fc5cd658f5db28de152d90a643080ef806%26mpshare%3D1%26scene%3D1%26srcid%3D0712ANRvnPTjgdF6kVCrPtEJ%26sharer_shareinfo%3Dbd6075f51ebb17596ce370640e3bd83b%26sharer_shareinfo_first%3Dbd6075f51ebb17596ce370640e3bd83b%23rd&s=obsidian)
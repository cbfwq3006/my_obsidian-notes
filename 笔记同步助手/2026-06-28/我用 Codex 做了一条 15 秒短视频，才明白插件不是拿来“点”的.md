---
author: 枫哥
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzA5MzY2NzM0OA==&mid=2650375192&idx=1&sn=0e5669603471ba250739b1ec77c230c4&chksm=8907b0fdcce9db8b461b1a316bd9dc60b131b7efdb7e1af7d97aec9ce7007b3c340d672fa16c&mpshare=1&scene=1&srcid=0626FDQvB8LIoqSOTJbZFAeO&sharer_shareinfo=d52fcabc65264f80b9a61922e8ca6d00&sharer_shareinfo_first=2f5de2cb50dca037c5bdf0c96d5f584e#rd
saved: 2026-06-28 09:05:06
tags:
  - 笔记同步助手
id: d8cd0a1e-a82d-41c6-9ec4-30dd3088d8ae
---

公众号名称：枫哥Prompter

作者名称：枫哥

发布时间：2026-06-26 17:26

  

这是枫哥的第 483 篇原创！

让更多人因 AI 而强大

![[笔记同步助手/images/9117b7025bafaa7848097100d45a6790_MD5.gif||108]]

你好！我是 70 后枫哥，

2 年写了 400+ 篇公众号原创文章。

帮 AI 小白、自媒体人，用 AI 提效、用 AI 赚钱。

![[笔记同步助手/images/fc6e5fb74e5b4e528a3db224395d45de_MD5.png]]

今天跑通了一件小事，不是大项目。就是用 Codex 里的 HyperFrames 插件，做了一条 15 秒竖屏短视频。

主题是：**我为什么建议普通人学习 ima 知识库。**

最后交付出来的东西很具体：

![[笔记同步助手/images/873c0dc9db1d2dfd032a44c50168cbc0_MD5.jpg]]

> 📹 此处为视频内容（vid: wxv\_4578029833250865153）（上图为封面），未能直接提取，请前往原文查看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzA5MzY2NzM0OA==&mid=2650375192&idx=1&sn=0e5669603471ba250739b1ec77c230c4&chksm=8907b0fdcce9db8b461b1a316bd9dc60b131b7efdb7e1af7d97aec9ce7007b3c340d672fa16c&mpshare=1&scene=1&srcid=0626FDQvB8LIoqSOTJbZFAeO&sharer_shareinfo=d52fcabc65264f80b9a61922e8ca6d00&sharer_shareinfo_first=2f5de2cb50dca037c5bdf0c96d5f584e#rd)

视频有画面。有转场。有文字动画。也有背景音乐。但真正让我有收获的，不是“做出了一条视频”。

虽然视频很不完美，而且中间还踩了三个坑。但我流程还是跑通了，可以使用codex 生成视频了。

第一个坑：插件装好了，不知道怎么用。

第二个坑：视频渲染失败，不是代码错，而是 FFmpeg 环境没配好。

第三个坑：音乐加上了，但一开始听不到；后来听到了，又像嗡嗡声。

这三个坑放在一起，其实就是普通人用 AI 工具最常见的问题：你缺的不是工具，是一套能跑起来、能检查、能返工的流程。

![[笔记同步助手/images/f0535513b4ddfc0751164944573ed824_MD5.png]]

## 先说结论

HyperFrames 不是一个“点开就用”的按钮。它更像是给 Codex 加了一只手。

你告诉 Codex 要做什么，它负责调用 HyperFrames，把 HTML、动画、音频、渲染串起来。

所以，我不是去找插件入口。而是直接对 Codex 说：

```
请用 HyperFrames 做一个 15 秒竖屏短视频：
主题：我为什么建议普通人学习 ima 知识库
风格：清爽、有力量、适合视频号
结构：开头金句 + 3 个要点 + 结尾行动号召
输出：本地预览地址和 MP4 文件
```

这段提示词里，有 5 个关键信息：

1.  用什么工具：HyperFrames。
    
2.  做多长：15 秒。
    
3.  什么画幅：竖屏。
    
4.  讲什么主题：ima 知识库。
    
5.  怎么验收：预览地址 + MP4 文件。
    

很多人用 AI 做东西，失败就失败在这里。一上来就说：

```
帮我做个视频。
```

这句话太虚。AI 会自己猜。一旦它开始猜，你后面就开始改。所以，提示词不是写得越长越好。

而是要把交付物说清楚。

![[笔记同步助手/images/9900317847fe23947b40627c0190924b_MD5.png]]

## 先定风格

Codex 开始做之前，先建了一个文件：

```
E:\Claude code\ima-knowledge-hyperframes-video\DESIGN.md
```

这个文件干什么？定风格。这一步很重要。如果不先定风格，AI 很容易给你来一套默认审美：蓝紫渐变。赛博霓虹。

一堆卡片飞来飞去。看起来很“AI”，但不适合公众号，也不适合视频号。

这次我给它的方向是：

-   浅色纸张背景。
    
-   深墨绿色文字。
    
-   绿色和暖黄色做强调。
    
-   字要大。
    
-   动效要克制。
    
-   不要装饰抢内容。
    

这就是我现在越来越重视的一点：**先定边界，再让 AI 发挥。没有边界，AI 会很努力地跑偏。**

![[笔记同步助手/images/b563f5bf036297a59d015497b3f3ba18_MD5.png]]

## 视频是 HTML

HyperFrames 最有意思的地方，是它把视频当成 HTML 来写。

核心文件是：

```
E:\Claude code\ima-knowledge-hyperframes-video\index.html
```

它不是普通网页。它是带时间轴的视频源文件。

比如一个场景是这样：

你不用懂太多前端，也能看懂几个关键点：

-   `data-start`：从第几秒开始。
    
-   `data-duration`：持续几秒。
    
-   `data-track-index`：在哪条轨道上。
    
-   `class="clip"`：这是一个按时间出现的片段。
    

这条 15 秒视频，我让它拆成 5 个场景：

1.  开头金句：普通人最该建的，不是收藏夹。
    
2.  第一个理由：资料越多，越容易忘。
    
3.  第二个理由：信息要变成可复用资产。
    
4.  第三个理由：问题越具体，答案越像助手。
    
5.  结尾行动：今天就建一个小知识库。
    

这就够了。短视频不怕短。怕的是短了还没重点。

![[笔记同步助手/images/4d1882229d715313e02c6c3f5f79cd43_MD5.png]]

## 必须检查

我现在用 AI 做东西，有一个习惯：**不只看它生成了什么，还要看它怎么通过检查。**

Codex 跑了三个命令：

```
npx hyperframes lint
npx hyperframes validate
npx hyperframes inspect --samples 15
```

它们分别检查三件事：

-   结构有没有错。
    
-   浏览器里有没有报错。
    
-   画面有没有溢出、重叠、跑出屏幕。
    

第一次检查，真查出了问题。

比如：

-   有些场景缺 `clip`。
    
-   转场动画和 CSS transform 冲突。
    
-   字体声明不够稳定。
    

这些问题肉眼不一定马上看出来。但一旦渲染，就可能变成画面错乱。

修完以后，结果变成：

```
lint：0 errors, 0 warnings
validate：No console errors · 90 text elements pass WCAG AA
inspect：0 layout issues
```

这一步，是我觉得最值得普通人学的。不要满足于“AI 说做好了”。要让它拿证据出来。

## 第一次失败

检查通过后，开始渲染：

```
npx hyperframes render --quality draft --output ima-knowledge-base-15s.mp4
```

结果失败了。报错很直接：

```
FFmpeg not found
FFprobe not found
```

这时候不要慌。这不是视频代码错了。

这是电脑里缺两个视频工具：

-   FFmpeg：负责编码。
    
-   FFprobe：负责检测媒体信息。
    

解决办法也很具体：

```
npm install ffmpeg-static ffprobe-static
```

然后渲染时临时把它们加入 PATH：

```
$env:Path = 'E:\Claude code\ima-knowledge-hyperframes-video\node_modules\ffmpeg-static;E:\Claude code\ima-knowledge-hyperframes-video\node_modules\ffprobe-static\bin\win32\x64;' + $env:Path
npx hyperframes render --quality draft --output ima-knowledge-base-15s.mp4
```

最后视频出来了。

再用 `ffprobe` 验证：

```
codec_name=h264
width=1080
height=1920
duration=15.000000
```

这就是一次完整闭环。不是报错就放弃。而是诊断问题，补上环境，再跑一次。

![[笔记同步助手/images/88b71ccc926964de0ca0b331098b7680_MD5.png]]

## 加音乐

视频有了，我又想加音乐。HyperFrames 加音乐，其实就是加一条独立音频轨：

```

```

看起来很简单。但真正的坑来了。第一次加完后，MP4 里确实有音频轨：

```
codec_name=aac
codec_type=audio
channels=2
```

可我一听，没声音。这时候不能靠感觉猜。

直接查音量：

```
ffmpeg -i ima-knowledge-base-15s-with-music.mp4 -af volumedetect -f null NUL
```

结果是：

```
mean_volume: -62.9 dB
max_volume: -54.3 dB
```

这基本等于听不见。所以问题不是“没音轨”。是音量太低。

后来调到：

```
mean_volume: -23.4 dB
max_volume: -14.5 dB
```

声音出来了。但又出现第二个问题。它像嗡嗡声。不是音乐。

这件事很有意思。因为从技术指标看，它已经合格了。有音轨，有音量，能播放。但它不合格，因为声音不是配乐，而是噪声。

所以我让 Codex 重新生成了一段真正有结构的底乐：

-   有和弦。
    
-   有短旋律。
    
-   有轻鼓点。
    
-   有淡入淡出。
    

最后用的是这个文件：

```
E:\Claude code\ima-knowledge-hyperframes-video\bgm-ima-melodic.mp3
```

最终视频是：

```
E:\Claude code\ima-knowledge-hyperframes-video\ima-knowledge-base-15s-melodic-music.mp4
```

最终音频检测：

```
音频轨：AAC，双声道
时长：15.04 秒
mean_volume: -22.5 dB
max_volume: -3.3 dB
```

这一次，才像一条能发出去的视频。

![[笔记同步助手/images/d3502ed605d5c5aea64e63e33b00c779_MD5.png]]

## 我的 SOP

这次跑完，我把流程整理成一套 SOP。以后再做同类视频，就不用从头摸了。

### 1\. 说清目标

```
请用 HyperFrames 做一个 15 秒竖屏短视频：
主题：____
风格：____
结构：开头金句 + 3 个要点 + 结尾行动号召
输出：本地预览地址和 MP4 文件
```

### 2\. 定视觉

先让 Codex 写 `DESIGN.md`。不要直接开做。先定颜色、字体、风格和禁忌。

### 3\. 做项目

核心文件是：

```
index.html
```

里面要有场景、时间轴、动画和音频轨。

### 4\. 跑检查

```
npx hyperframes lint
npx hyperframes validate
npx hyperframes inspect --samples 15
```

不通过就修。不要凭感觉。

### 5\. 渲染

```
npx hyperframes render --quality draft --output output.mp4
```

如果缺 FFmpeg，就补：

```
npm install ffmpeg-static ffprobe-static
```

### 6\. 验成品

看视频参数：

```
ffprobe output.mp4
```

查音量：

```
ffmpeg -i output.mp4 -af volumedetect -f null NUL
```

最后自己看一遍、听一遍。工具只能告诉你“有没有”。要判断“好不好”。

![[笔记同步助手/images/024763b19e65a4b867efbc13d29abe2b_MD5.png]]

## 最后说一句

这次我最大的感受是：**插件不是魔法，流程才是能力。**

以前我们做视频，要打开剪辑软件，找模板，写字幕，加音乐，调动画，导出。现在 Codex 可以把这些事串起来。但你不能把判断也交出去。

AI 可以帮你做。但你要会验收。AI 可以帮你跑。但你要知道跑到哪里算完成。

这也是我一直建议普通人学习 AI 工具的原因。不是为了多装几个插件，而是为了把自己的想法，变成一个能交付的结果。

收藏不是使用，围观不是上车。真正的进步，是你亲手跑通一次。

![[笔记同步助手/images/a38214e2c547de4c3168547ad2191712_MD5.png]]

![[笔记同步助手/images/e6d60fb7b2fd237dc58c9a8592d4f7be_MD5.png]]你好呀，我是 70 后枫哥，

终身学习、终身思考、终身行动的 70 后，

坚持日更，原创文章400+，总用户数 15000+

  

## 1\. 400+ 篇原创文章，1.5+ 万粉丝，我决定推倒重来

## 2\. 微信「小微」来了，超级 App 的 AI 入口争夺战正式打响

## 3\. AGENTS.md出圈：给你的AI写一份"入职说明书"

## 4\. 公众号新规：我踩坑后才明白，不能再这么写了

## 5\. ima 知识库小白入门教程：从 0 到 1 打造你的"第二大脑"

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/1a0d84a8_1782608704643?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA5MzY2NzM0OA%3D%3D%26mid%3D2650375192%26idx%3D1%26sn%3D0e5669603471ba250739b1ec77c230c4%26chksm%3D8907b0fdcce9db8b461b1a316bd9dc60b131b7efdb7e1af7d97aec9ce7007b3c340d672fa16c%26mpshare%3D1%26scene%3D1%26srcid%3D0626FDQvB8LIoqSOTJbZFAeO%26sharer_shareinfo%3Dd52fcabc65264f80b9a61922e8ca6d00%26sharer_shareinfo_first%3D2f5de2cb50dca037c5bdf0c96d5f584e%23rd&s=obsidian)
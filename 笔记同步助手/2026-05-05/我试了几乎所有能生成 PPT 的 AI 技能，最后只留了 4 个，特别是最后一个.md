---
author: 瞎捣鼓的老严
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzU0ODczNTMwNQ==&mid=2247485883&idx=1&sn=1e3d2d80100cb333f02be0e9ccb2ddd0&chksm=fa055b10306cdcb984f5fdeaad45fdb1b9564246358bcd75b8651014d4c721dc92eb8118bd4e&mpshare=1&scene=1&srcid=05052HKP8vf3sXEAcu18eLJp&sharer_shareinfo=24edc5eaa29986c99f981f92fadf558f&sharer_shareinfo_first=24edc5eaa29986c99f981f92fadf558f#rd
saved: 2026-05-05 23:47:20
tags:
  - 笔记同步助手
id: 4053ee4a-4711-450b-9185-44902a3093c1
---

公众号名称：AI Agentic共创

作者名称：瞎捣鼓的老严

发布时间：2026-04-30 08:18

上周我要做一个技术分享 PPT。

第一反应是找个 AI 工具帮我生成。打开 ClawHub 一搜，PPT 相关的 Skill 有几十个。

guizang-ppt-skill、huashu-design、Kami、ppt-master、slide-generator、deck-builder、MiniMax-skills……

我一个个试过来，熬了两个晚上，眼睛快瞎了。

**最后只留下了 4 个。** 不是因为其他的一无是处，是因为这 4 个各有一个"只有它能做到"的绝活。

​

---

![[笔记同步助手/images/be9ee7dfcabed7e16b624d7e73e338f0_MD5.png]]

---

## 第一个：guizang-ppt-skill

这个是我第一个试的。

生成的是一个单文件 HTML，横向翻页，完全独立运行。不需要装任何东西，浏览器打开就行。

**最让我"卧槽"的是它的 WebGL 流体背景。**

不是那种廉价的渐变动画，是真的有质感的流体效果，hero 页一打开，感觉像在看 Apple 发布会。配色是 5 套预设，不允许自定义——墨水经典、靛蓝瓷、森林墨、牛皮纸、沙丘。

一开始我觉得"不能自定义配色"是个缺点，后来发现，预设的审美比我这个纯理科、拍照被老婆鄙视的高出天际。

字体组合也很讲究：衬线标题 + 非衬线正文 + 等宽元数据。"电子杂志 + 电子墨水"的混血风格，放在大屏幕上确实好看。

**适合场景**：技术发布会、个人分享、私享会。就是那种"我要秀一下"的场合。

**缺点也很明显**：输出是 HTML，不能在 PowerPoint 里编辑。如果你需要把 PPT 发给别人修改，这个不行。

![[笔记同步助手/images/17fbd60953ae303ed93a00a6ab49983b_MD5.png]]

  

---

## 第二个：huashu-design（花叔）

这个最有意思。

它不是直接给你生成一个成品，而是像一个"Junior Designer"——先展示假设、推理过程、占位符，让你看他的设计思路，然后你再提意见。

**最让我觉得骚的操作是 Tweaks 系统。**

你可以实时切换颜色、字号、密度、暗黑模式。不用重新生成，直接切。这种感觉就像你在 Figma 里调参数，但它是 AI 自动帮你做的。

它还能把 HTML 动画导出成 MP4 或 GIF，25fps 基础加 60fps 插帧。如果你的 PPT 里需要动效演示，这个是唯一的选择。

设计方向顾问模式也很实用。它从 5 个流派 × 20 种设计哲学里推荐 3 个差异化方向，你不是一上来就定死风格，而是先看选项再选。

**适合场景**：交互原型、设计变体探索、需要动效的多媒体展示。

**缺点**：需要 React 环境，PPTX 需要转换，不是开箱即用。

![[笔记同步助手/images/e4cbfec14aafb699a40372ac98022595_MD5.png]]

  

---

## 第三个：Kami-design

这个是我试到第三个的时候觉得"嗯，这个稳了"的。

暖羊皮纸底色加墨水蓝点缀，衬线主导层级。一看就是专业文档的质感。

它覆盖 8 种文档类型：简历、一页纸、白皮书、信件、作品集、幻灯片、个股研报、更新日志。不只是 PPT。

**14 种图表原语让我眼前一亮。** 架构图、流程图、象限图、柱状图……你提供数据，它自动选图表类型。用 WeasyPrint 生成高质量 PDF，印刷级别。

**适合场景**：专业文档排版，尤其是需要印刷质量的中文文档。简历、白皮书、研报。

**缺点**：设计系统固定，不够灵活。依赖商业字体。

![[笔记同步助手/images/0fec15f558922efea8be6328bf4e81ad_MD5.png]]

​

---

## 第四个：ppt-master

这是最后一个试的，也是让我觉得"商务场景终于有解了"的那个。

它的核心设计是**AI 多角色协作流水线**：Strategist 定策略 → Image\_Generator 生成图片 → Executor 执行。三个角色串行工作，每页 SVG 生成前必须 re-read spec\_lock.md，防止风格漂移。

**8 步确认制（Blocking）一开始我觉得烦，后来觉得合理。** 画布格式、页数范围、目标受众、风格目标、配色方案、图标方案、字体方案、图片方案——每一步确认了再生成，出来的质量确实不一样。

**最让我觉得踏实的是：原生 PPTX 输出，完全可编辑。**

不是转换，不是导出，是真正的 PowerPoint 原生格式。生成后的 PPTX，你在 PowerPoint 里打开，文字能改、图片能换、布局能调。这对于商务场景来说，是刚需。

per-page layout rhythm 的设计也很用心：anchor（结构页）、dense（信息密集）、breathing（低密度冲击），长篇 PPT 不会一页一页长得一样。

特别是支持自定义模板，同时页提供了很多预置模板

![[笔记同步助手/images/efa4949954098263dc8f99c3f8973d38_MD5.png]]

**适合场景**：需要生成高质量、可编辑 PPTX 的商务和专业场景。长篇 PPT（20+ 页）。

**缺点**：流程最复杂，多步 Blocking 确认，不适合"快速出个东西"的场景。

​

---

![[笔记同步助手/images/00b17f1f9f955b6bf2335775e5bc5e44_MD5.png]]

---

## 我的判断

试完这四个，我有一个很明确的感受：

**没有万能的 PPT 工具，只有对的场景。**

guizang-ppt-skill做展示，huashu-design做原型，Kami 做文档，ppt-master 做商务。每个工具都在自己的赛道里做到了最好。

![[笔记同步助手/images/695e265fbcabb5fd9afbb9d3498028d5_MD5.png]]

---

成年人不做选择题，但要知道每个工具最适合什么。

我的建议是：根据场景搭配使用。商务 PPT 用 ppt-master，技术分享用guizang-ppt-skill，专业文档用 Kami，设计原型用huashu-design。

**少装一个没用的，多装一个对的。**

​

**PS：MiniMax的PPT-generator属于量大管饱型**

SKills：

huashu-skills:https://github.com/alchaincyf/huashu-skills

ppt-master:https://github.com/hugohe3/ppt-master/tree/main

guizang:https://github.com/op7418/guizang-ppt-skill

kami:https://github.com/tw93/Kami

​

一个喜欢瞎捣鼓的架构师，把团队转型过程中踩过的坑讲给你听。

#Agents#AIPPT#huashu#guizang

---

Original 瞎捣鼓的老严 AI Agentic共创
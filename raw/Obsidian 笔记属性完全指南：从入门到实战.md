Bug2048 *2026年3月26日 07:30*

![图片](https://mmbiz.qpic.cn/mmbiz_png/bxhz6OzhExachSQGF3BMic4MTPJBVgApKnkmEbVpNFQnuHEcvd6xzUHb1Gv2Joo1ytKXFkUGqhRZ0MphU1NXYfflia290RdwukhqCTBlo8EQo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

用 Obsidian 久了，你会发现一个问题：笔记越写越多，找起来越来越费劲。标签倒是打了，链接也建了，但真正想「按某个维度批量查看笔记」的时候，搜索框就显得力不从心。

笔记属性（Properties）就是 Obsidian 给出的答案。它让你能在每条笔记顶部挂上一段结构化元数据，然后像操作数据库一样去查询、筛选、排序你的笔记库。

这篇文章会从基础概念讲起，一路延伸到 Dataview 查询、Templater 自动化等进阶用法。

## 一、什么是笔记属性

笔记属性，在 Obsidian 的语境里也叫 Properties 或者 YAML Front Matter。说白了，就是在 Markdown 文件的最顶部加一段用 `---` 包裹的键值对数据。

```
---
title: 深度学习笔记
date: 2025-03-25
tags:
  - 机器学习
  - 深度学习
status: 进行中
---
```

这段数据不会出现在笔记正文中，但 Obsidian 和各种插件都可以读取它。你可以把它理解成每条笔记的「身份证」——标题、日期、分类、状态，全写在上面。

Obsidian 在 1.4 版本之后对属性做了大幅升级，新增了可视化属性面板。你现在打开一条带属性的笔记，会在编辑区上方看到一个结构化的属性表单，再也不用手动敲 YAML 了。

## 二、基础语法

### 2.1 格式规则

属性必须写在文件的最开头，用三个短横线 `---` 标记边界：

```
---
key: value
another_key: another value
---
```

几个需要注意的地方：

冒号后面必须加空格。 `title: Obsidian` 是对的， `title:Obsidian` 不会被识别。

字符串类型的值一般不需要引号，但如果值里包含特殊字符（比如冒号），就需要用引号包裹：

```
title: "Obsidian: 从入门到精通"
```

### 2.2 多值写法

一个字段对应多个值时，有两种写法：

用方括号，逗号分隔：

```
tags: [读书笔记, AI, 2025]
```

或者用短横线换行排列：

```
tags:
  - 读书笔记
  - AI
  - 2025
```

两种写法效果完全一样，后者在值多的时候更清晰。

### 2.3 常见数据类型

YAML 支持多种数据类型，Obsidian 都能正确识别：

| 类型 | 示例 | 说明 |
| --- | --- | --- |
| 字符串 | `title: 我的笔记` | 默认类型 |
| 数字 | `rating: 8` | 直接写数字 |
| 布尔值 | `completed: true` | 只能是 true 或 false |
| 日期 | `date: 2025-03-25` | 支持 ISO 8601 格式 |
| 列表 | `tags: [a, b]` | 用方括号或短横线 |
| 多行文本 | 用 \` | `或`  \>\` |

多行文本的写法比较特殊，举个例子：

```
summary: |
  这是一段摘要。
  第二行内容。
  每行换行都会被保留。
```

如果用 `>` 替代 `|` ，连续的换行会被折叠成一个空格。

## 三、Obsidian 原生支持的属性字段

Obsidian 核心功能直接识别的属性字段不多，但每个都很实用：

### tags — 标签

为笔记添加标签，支持单标签和多标签：

```
tags: 读书笔记
```
```
tags:
  - 读书笔记
  - AI
  - 笔记方法论
```

### aliases — 别名

给笔记设置别名后，用 `[[` 输入别名也能链接到这条笔记。对于文件名较长或有多重指代的笔记特别有用：

```
aliases:
  - Obsidian前置元数据
  - YAML属性
  - Front Matter
```

### cssclass — 样式类

指定 CSS 类名，配合自定义 CSS 代码片段使用。比如你写了一段 `wide-page` 的样式，就可以在特定笔记里这样用：

```
cssclass: wide-page
```

### publish — 发布控制

配合 Obsidian Publish 服务，控制笔记是否对外发布：

```
publish: true
```

这几个是 Obsidian 官方文档中明确列出的原生字段。但实际使用中，你可以自由定义任何字段名—— `status` 、 `priority` 、、 `source` ，随便你取。Obsidian 本身不会对自定义字段做特殊处理，但社区插件会利用它们做各种事情。

## 四、使用属性面板

Obsidian 1.4+ 版本引入了属性面板，让属性的编辑变得更加直观。

启用方式：设置 → 编辑器 → 显示属性。开启后，每条笔记的正文上方会出现一个表单式的属性编辑区域。

在属性面板里你可以：

- • 点击「添加属性」按钮，从下拉列表选择已有字段或创建新字段
- • 对于已有属性，直接在表单里修改值
- • 拖拽调整属性顺序
- • 删除不需要的属性

属性面板和 YAML Front Matter 是双向同步的。你在面板里改了值，YAML 源码会跟着变；直接编辑 YAML，面板也会实时更新。

如果你更喜欢手写 YAML（老用户多半如此），也可以在设置里关掉属性面板，回到纯文本编辑模式。

## 五、高阶用法：让属性真正发挥价值

前面说的是「怎么写属性」，接下来聊「怎么用属性」。

### 5.1 搭配 Dataview 插件做动态查询

Dataview 是 Obsidian 社区最受欢迎的插件之一。它能把你的笔记库当成一个数据库，用类 SQL 的语法查询属性数据。

安装 Dataview 后，在任意笔记里写一个代码块：

```
\`\`\`dataview
TABLE status, priority, due
FROM "项目笔记"
WHERE status = "进行中"
SORT due ASC
\`\`\`
```

这行代码会自动生成一个表格，列出「项目笔记」文件夹下所有状态为「进行中」的笔记，并按截止日期排序。

Dataview 支持四种展示格式：

- • `TABLE` — 表格
- • `LIST` — 列表
- • `TASK` — 任务视图
- • `CALENDAR` — 日历视图

几个实用的查询例子：

查询所有未完成的任务笔记：

```
\`\`\`dataview
LIST
FROM #任务
WHERE status != "已完成"
SORT priority DESC
\`\`\`
```

按创建日期显示最近一周的新笔记：

```
\`\`\`dataview
TABLE file.cday AS "创建日期", tags
WHERE file.cday >= date(today) - dur(7 days)
SORT file.cday DESC
\`\`\`
```

分组统计不同类别的笔记数量：

```
\`\`\`dataview
TABLE length(rows) AS "数量"
FROM ""
GROUP BY category
\`\`\`
```

Dataview 还能读取每个笔记自动携带的元数据，比如 `file.name` （文件名）、 `file.cday` （创建日期）、 `file.mday` （修改日期）、 `file.size` （文件大小），不需要你在 YAML 里额外定义。

### 5.2 搭配 Templater 插件实现自动化

如果你每新建一条笔记都要手动填属性，那属性的意义就打折了。Templater 插件可以在创建笔记时自动生成一段 Front Matter。

安装 Templater 后，创建一个模板文件：

```
---
title: "{{title}}"
date: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - <% tp.system.suggester(["读书笔记", "项目", "日记", "想法"], ["读书笔记", "项目", "日记", "想法"]) %>
status: 草稿
---

# {{title}}
```

这段模板里， `tp.date.now()` 会自动填入当前日期， `tp.system.suggester()` 会弹出一个选择列表让你选标签。每次新建笔记套用这个模板，属性就自动填好了。

Templater 还支持文件夹级别的自动模板规则。你可以设置「凡是新建在『读书笔记』文件夹下的文件，自动套用读书模板」，不需要每次手动选择。

更进一步，Templater 提供了 `tp.frontmatter` 模块，可以在模板中直接操作当前笔记的 Front Matter：

```
<%*
// 自动根据文件名设置标题
await tp.frontmatter.set("title", tp.file.title);
// 自动设置创建时间
await tp.frontmatter.set("created", tp.date.now("YYYY-MM-DD HH:mm"));
// 根据所在文件夹自动分类
await tp.frontmatter.set("category", tp.file.folder.split("/").pop());
%>
```

### 5.3 搭配 Tasks 插件管理待办

Tasks 插件能读取 YAML 属性中的日期字段，配合任务查询做项目管理：

```
---
due: 2025-04-01
priority: high
---
```
```
\`\`\`tasks
not done
due before tomorrow
priority is high
\`\`\`
```

这条查询会列出所有明天之前到期的高优先级未完成任务。

### 5.4 属性驱动的笔记分类体系

用属性建立一套自己的分类标准，比单纯靠文件夹和标签灵活得多。

举个例子，为读书笔记设计这样一套属性：

```
---
type: 读书笔记
book_title: 原子习惯
author: 詹姆斯·克利尔
rating: 8
date_read: 2025-03-20
status: 已读完
tags:
  - 个人成长
  - 习惯养成
---
```

然后用 Dataview 一条查询就能生成你的「已读书单」：

```
\`\`\`dataview
TABLE book_title AS "书名", author AS "作者", rating AS "评分", date_read AS "读完日期"
FROM ""
WHERE type = "读书笔记" AND status = "已读完"
SORT rating DESC
\`\`\`
```

再配合一个「评分排行」：

```
\`\`\`dataview
TABLE book_title AS "书名", rating AS "评分"
FROM ""
WHERE type = "读书笔记"
SORT rating DESC
LIMIT 10
\`\`\`
```

这样你的笔记库就不只是笔记的堆积，而是一个可查询、可统计的个人知识数据库。

## 六、容易踩的坑

写 YAML 属性时有几个常见错误，新手很容易中招。

冒号后忘记加空格。这是最多的错误来源。 `title:Obsidian` 不会被解析为键值对，整段 YAML 都可能失效。

缩进不一致。YAML 对缩进敏感，建议统一用两个空格缩进。

布尔值和字符串混淆。 `status: true` 会被解析为布尔值 true，而不是字符串 "true"。如果你确实想存字符串，需要加引号： `status: "true"` 。

日期格式不统一。Obsidian 对日期的识别比较宽容，但 Dataview 要求严格的格式。建议统一用 `YYYY-MM-DD` 或 ISO 8601 完整格式。

YAML 块内的 `---` 会截断属性。如果属性值中包含 `---` ，会导致 YAML 提前结束。

## 七、实用建议

最后分享几个用了一段时间属性之后总结出来的实践。

先想好你要查询什么，再决定怎么定义属性。属性是为了查询和统计服务的，不是越多越好。如果你从来没有按「心情」筛选笔记的需求，就没必要加一个 `mood` 字段。

同类笔记用统一的属性模板。读书笔记有一套属性，项目笔记有另一套。保持一致性才能让 Dataview 查询正常工作。

善用属性面板做批量编辑。需要给一批笔记统一添加某个字段时，属性面板比手改 YAML 高效得多。

定期清理无用属性。用久了你会发现有些字段从来没被查询过，果断删掉它们，减少每条笔记的信息噪音。

从简单开始。如果你刚开始用属性，先只加 `tags` 和 `date` 两个字段就够了。等用熟了再逐步扩展，别一上来就搞一长串属性把自己绕晕。

---

继续滑动看下一个

AI是那啥

向上滑动看下一个
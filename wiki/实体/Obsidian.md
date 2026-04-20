---
type: entity
tags: [工具, 知识管理, 笔记软件]
sources:
  - [[wiki/来源/2026-04-12 用Hermes+Obsidian搭建个人知识库.md]]
  - [[wiki/来源/2026-04-15 Smart Connections插件.md]]
  - [[wiki/来源/2026-04-18 Hermes+AutoCLI+Obsidian自动化知识系统.md]]
created: 2026-04-19
updated: 2026-04-19
---

# Obsidian

## 基本信息

**类型**：笔记软件 / 知识管理工具
**特点**：本地优先、Markdown 格式、双向链接

## 核心优势

### 1. 本地优先（Local-first）
- 所有笔记存在本地 Markdown 文件
- 数据永不丢失，完全掌控
- 隐私安全，不在云端

### 2. 双向链接
- 笔记之间可以互相链接
- 形成知识网络
- 支持 Wiki-link 语法

### 3. 图谱视图
- 可视化知识结构
- 发现隐藏联系
- 查看笔记关系网络

### 4. 完全可定制
- CSS 样式可自定义
- 丰富的插件生态
- 模板系统

### 5. 开放生态
- 支持第三方插件
- 可与其他工具集成
- 数据格式开放（Markdown）

## 推荐插件

### 核心插件
- **Templater**（⭐⭐⭐⭐⭐）：模板系统，自动化创建笔记
- **Dataview**（⭐⭐⭐⭐⭐）：查询笔记，像数据库一样
- **BRAT**（⭐⭐⭐⭐）：安装 Beta 插件
- **Metaedit**（⭐⭐⭐⭐）：可视化编辑 YAML

### 增强插件
- **Smart Connections**：语义搜索和智能推荐
- **Local REST API**：允许外部工具访问 Obsidian
- **Obsidian Web Clipper**：浏览器扩展，一键保存网页

## 与其他工具的集成

### Obsidian + Hermes
- Hermes 提供智能检索和自动整理
- 通过 Local REST API 插件连接
- 实现主动记忆和知识关联

### Obsidian + AutoCLI
- AutoCLI 负责信息抓取
- Obsidian 作为知识存储中心
- 形成自动化入库流程

## 推荐文件夹结构

```
~/obsidian-vault/
├── 0_Inbox/        # 收集箱
├── 1_Projects/     # 项目笔记
├── 2_Areas/        # 领域笔记
├── 3_Resources/    # 资源笔记
├── 4_People/       # 人物笔记
├── 5_Templates/    # 模板库
├── 6_Meta/         # 元笔记
└── z_Archive/      # 归档
```

## 在知识库中的角色

在多篇来源中，Obsidian 被定位为：
- **存储层**：负责持久化、结构化存储
- **可视化层**：通过图谱视图展示知识网络
- **中心枢纽**：连接各种自动化工具的核心

## 相关实体

- [[Hermes]]
- [[Smart Connections]]
- [[AutoCLI]]

## 相关概念

- [[第二大脑]]
- [[双向链接]]
- [[知识管理]]
- [[本地优先]]

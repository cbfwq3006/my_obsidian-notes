---
type: concept
tags: [飞书, CLI, 工具, API]
sources:
  - [[wiki/来源/2026-04-12 用Hermes+Obsidian搭建个人知识库]]
  - [[wiki/来源/2026-04-15 飞书CLI + Codex = 生产力]]
created: 2026-05-04
updated: 2026-05-04
---

# 飞书 CLI

## 概念定义

飞书 CLI（Command Line Interface）是飞书官方提供的命令行工具，允许开发者和 AI Agent 通过命令行访问和操作飞书的各种资源（文档、知识库、云空间、日历等）。

## 核心功能

### 1. 安装与配置

**安装**：
```bash
npm install -g @larksuite/cli
npx skills add https://github.com/larksuite/cli -y -g
```

**初始化**：
```bash
lark-cli config init --new
```
- 生成授权链接
- 在飞书开发者平台创建应用

**授权**：
```bash
lark-cli auth login                    # 交互式授权
lark-cli auth login --domain docs      # 精确授权特定域
lark-cli auth login --scope "..."      # 按 scope 授权
```

### 2. 与 AI Agent 集成

安装后会在以下应用的 skills 文件夹中添加飞书相关 skill：
- Trae
- Cursor
- Codex
- Claude Code

AI Agent 可以通过这些 skills 调用 lark-cli 访问飞书资源。

### 3. 主要能力

- **文档操作**：创建、读取、编辑飞书文档
- **知识库管理**：组织知识库结构
- **云空间访问**：上传下载文件
- **日历管理**：查看和创建日程
- **即时通讯**：发送消息

## 使用场景

### 场景 1：知识库自动化（来自第二篇文章）

**案例**：构建 GDPR 中英文对照知识库
- 使用 Codex + 飞书 CLI
- 在飞书知识库中创建树状结构
- 逐条插入中英文对照内容
- 添加超链接导航

### 场景 2：与 Obsidian 联动（来自第一篇文章）

**配置**：
```bash
hermes config set obsidian.vault_path ~/obsidian-vault
hermes config set obsidian.api_enabled true
hermes config set obsidian.api_port 27123
```

**工作流**：
- Hermes 读取 Obsidian 笔记
- 通过飞书 CLI 同步到飞书
- 或从飞书抓取内容到 Obsidian

## 身份类型

### User 身份
- 访问用户自己的资源
- 需要通过 `lark-cli auth login` 授权
- 适用场景：个人日历、云空间、邮箱

### Bot 身份
- 应用级操作
- 只需在开发者后台开通 scope
- 适用场景：发送消息、创建文档

切换身份：
```bash
lark-cli config default-as user
lark-cli config default-as bot
```

## 优势

1. **命令行友好**：适合自动化脚本
2. **AI Agent 原生支持**：无缝集成到 AI 工作流
3. **权限精细控制**：可按域或 scope 授权
4. **跨平台**：支持多种 AI 编程工具

## 与其他工具的对比

| 工具 | 定位 | 优势 |
|------|------|------|
| 飞书 CLI | 命令行工具 | 自动化、AI 集成 |
| 飞书 API | 编程接口 | 灵活性高 |
| 飞书网页版 | 图形界面 | 直观易用 |

## 实践经验

### 来自第二篇文章的经验

**谨慎策略**：
- 对于高准确率任务，采用逐条处理
- 每步验证，确保正确性
- AI 会主动寻求确认

**成本考虑**：
- 复杂任务会消耗大量 token
- 例如：99 条法条处理用了 4 个大对话

## 相关概念

- [[wiki/概念/知识管理系统]]
- [[wiki/概念/AI Agent 集成]]
- API 集成
- 命令行工具

## 相关实体

- [[wiki/实体/飞书]]
- [[wiki/实体/Codex]]
- Hermes

## 参考来源

1. [[wiki/来源/2026-04-12 用Hermes+Obsidian搭建个人知识库]] - 介绍了飞书 CLI 与 Obsidian 的集成
2. [[wiki/来源/2026-04-15 飞书CLI + Codex = 生产力]] - 展示了飞书 CLI 的实战案例

---

*这是一个从多篇来源中提炼出的概念页，符合 Karpathy 自下而上原则。*

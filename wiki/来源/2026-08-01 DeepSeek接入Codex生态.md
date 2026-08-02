---
type: source
tags: [DeepSeek, Codex, API接入, keen]
sources: [[00 临时箱/DeepSeek 正式打通 Codex，编程起飞]]
created: 2026-08-01
updated: 2026-08-01
---

# DeepSeek接入Codex生态

> 来源: KEEN的创享公众号  
> 发布时间: 2026-08-01  
> 同步时间: 2026-08-01

## 内容总结

DeepSeek官方文档更新,正式放出[[wiki/实体/Codex]]接入指南,开发者可在Codex CLI、ChatGPT桌面端和VS Code插件中使用DeepSeek模型。目前支持deepseek-v4-flash,deepseek-v4-pro预计2026年8月初开放。

Codex并非单一工具,而是完整编程助手体系(CLI+桌面端+IDE插件),共用同一套配置文件。DeepSeek API原生支持Responses API,因此接入门槛相对较低。

提供两种接入方式:
1. **一键配置脚本**(官方推荐):自动备份现有配置、写入模型目录、修改config.toml、进行语法校验
2. **手动配置**:创建`~/.codex/models.json`声明模型元数据,修改`~/.codex/config.toml`添加DeepSeek作为提供方

配置完成后可在CLI、桌面端和VS Code中验证。文章展示了V4 Flash正式版的用时花费和缓存命中率数据。

## 关键观点

1. **生态接入降低门槛**:一次配置,三个工具(CLI/桌面端/IDE)同步使用
2. **原生API兼容**:DeepSeek原生支持Responses API,与Codex交互格式天然匹配
3. **自动化脚本友好**:官方提供一键脚本,支持重复运行和配置切换
4. **推理强度可调**:model_reasoning_effort控制推理深度,数值越高质量越好但耗时增加

## 关键概念

- [[wiki/实体/Codex]]
- [[wiki/实体/DeepSeek]]
- Responses API
- 模型推理强度
- 编程工作流

## 可复用启发

1. 工具生态接入的标准化:提供一键脚本+手动配置两种方式覆盖不同用户需求
2. 配置文件共享机制:CLI/桌面端/IDE共用配置,避免重复设置
3. 安全设计:脚本运行前备份现有配置,语法校验失败则不改动任何文件
4. 文档完整性:明确当前支持模型、后续计划和验证方法
5. API兼容性的商业价值:原生支持标准格式可快速接入现有生态

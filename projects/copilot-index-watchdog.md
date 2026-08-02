# Copilot 索引自动巡检

## 目的

自动检查 Obsidian Copilot 本地索引是否落后于最新 Markdown 笔记。
如果索引明显滞后且持续存在，就自动触发 `Force Reindex Vault`。

## 已创建文件

- `scripts/copilot-index-watchdog.ps1`
- `scripts/copilot-index-watchdog.config.json`
- `scripts/register-copilot-index-watchdog.ps1`
- `scripts/unregister-copilot-index-watchdog.ps1`

## 运行逻辑

- 每次检查最新的 `.md` 修改时间和最新的 `copilot-index-*.json` 更新时间。
- 若最新笔记比索引更新更晚，并持续超过设定阈值，则判定索引异常。
- 触发重建前会做冷却控制，避免重复重建。

## 状态文件

- 日志：`%LOCALAPPDATA%\sl_obsidian\copilot-watchdog\watchdog.log`
- 状态：`%LOCALAPPDATA%\sl_obsidian\copilot-watchdog\state.json`

## 启用

运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/register-copilot-index-watchdog.ps1
```

## 停用

运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/unregister-copilot-index-watchdog.ps1
```

## 手动单次检查

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/copilot-index-watchdog.ps1
```


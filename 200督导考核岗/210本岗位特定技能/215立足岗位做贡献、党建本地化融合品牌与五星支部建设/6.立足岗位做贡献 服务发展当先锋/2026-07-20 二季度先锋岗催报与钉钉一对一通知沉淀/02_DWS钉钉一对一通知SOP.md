# DWS钉钉一对一通知SOP

## 一、适用场景

适用于需要根据本地 Excel 人员明细表，向党务人员、支部组织委员或专项工作联系人逐一发送钉钉单聊通知的场景。

本次使用场景：

- 人员表：`D:\work\2026\2026年专职党务人员信息统计表.xlsx`
- 表头字段：部门、姓名、联系电话
- 通知内容：二季度“立足岗位做贡献、服务发展当先锋”党员先锋岗申报及评选材料提交
- 发送方式：钉钉一对一单聊

## 二、基本流程

1. 读取人员表，确认姓名、部门、手机号。
2. 使用 DWS 登录钉钉。
3. 授权 DWS 的 `contact` 和 `chat` 行为权限。
4. 通过手机号匹配钉钉 `userId`。
5. 对匹配成功人员发送单聊消息。
6. 手机号未匹配人员，用姓名搜索补查。
7. 姓名搜索无结果或结果不唯一时，不发送。
8. 输出发送结果表，保留过程痕迹。

## 三、常用命令

### 1. 查看 DWS 登录状态

```powershell
dws.cmd auth status --format json
```

### 2. 登录 DWS

```powershell
dws.cmd auth login --device --format json
```

### 3. 授权通讯录和消息能力

```powershell
dws.cmd pat chmod --products contact,chat --grant-type permanent --yes --format json
```

说明：`contact` 用于按手机号或姓名查人，`chat` 用于发送钉钉单聊消息。

### 4. 按手机号查人

```powershell
dws.cmd contact user search-mobile --mobile 15639108350 --format json
```

### 5. 按姓名查人

```powershell
dws.cmd contact user search --query 杜跃敏 --format json
```

### 6. 发送单聊消息

```powershell
dws.cmd chat message send --user <userId> --title "通知标题" --text "通知正文" --uuid "<固定UUID>" --format json
```

## 四、关键注意事项

1. PowerShell 中优先使用 `dws.cmd`，不要直接使用 `dws`，避免执行策略拦截。
2. 所有命令都加 `--format json`，便于解析结果。
3. 批量发送前必须先检查人员表和通知正文。
4. 每条消息建议设置固定 `uuid`，避免24小时内重复发送。
5. 手机号匹配失败时，不要直接猜用户。
6. 姓名搜索出现多个结果时，必须人工确认后再发。
7. 发送结果表要保存，便于追踪哪些人已通知、哪些人未通知。

## 五、常见问题

| 问题 | 原因 | 处理 |
| --- | --- | --- |
| `未登录` | DWS 尚未授权登录 | 执行 `dws.cmd auth login --device --format json` |
| `PAT_MEDIUM_RISK_NO_PERMISSION` | 缺少行为授权 | 执行 `dws.cmd pat chmod --products contact,chat --grant-type permanent --yes --format json` |
| 手机号查询成功但没有 `userId` | 返回为空或手机号不在通讯录 | 改用姓名搜索 |
| 姓名搜索无结果 | 通讯录不可见或姓名不一致 | 不发送，人工核实 |
| 发送成功但需要追溯 | DWS 返回 `openTaskId` | 保存到发送结果表 |

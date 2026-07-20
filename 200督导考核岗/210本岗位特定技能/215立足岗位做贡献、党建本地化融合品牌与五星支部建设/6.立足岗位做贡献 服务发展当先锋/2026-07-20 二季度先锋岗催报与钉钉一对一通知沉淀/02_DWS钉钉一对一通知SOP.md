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
8. 普通文字通知默认只传 `--text`，不要同时传 `--title`，避免钉钉客户端只展示标题、不展示正文。
9. 对跨组织、上级公司、外部协作人员，人员表建议增加 `userId` 或 `openDingTalkId` 兜底列。手机号和姓名查不到时，脚本优先使用人工补充的标识发送。

## 五、跨组织人员为什么会查不到

钉钉客户端能打开某个人的单聊，不等于 DWS 通讯录接口一定能查到这个人。DWS 当前登录组织、通讯录可见范围、接口权限和钉钉客户端搜索范围可能不一致。

本次张德保的情况是：

- 钉钉客户端中可以打开单聊。
- `contact user search-mobile --mobile 15639102777` 返回空。
- `contact user search --query 张德保` 返回空。
- `aisearch person --keyword 张德保 --dimension name` 返回空。
- 截图显示其组织路径更接近省公司/河南机动通信局，不像焦作市分公司本级通讯录成员。

因此，脚本没有可用的 `userId` 或 `openDingTalkId`，为避免误发，正确处理是暂不发送并列入人工核实名单。

优化办法：

1. 在党务人员表中增加两列：`userId`、`openDingTalkId`。
2. 对张德保这类手机号/姓名均查不到但钉钉客户端可联系的人，人工补充其中一个标识。
3. 后续脚本先读人工标识；有标识直接发，没有标识再按手机号查。
4. 批量发送前先给本人发测试消息，只传 `--text`，确认正文展示正常后再批量。

## 六、常见问题

| 问题 | 原因 | 处理 |
| --- | --- | --- |
| `未登录` | DWS 尚未授权登录 | 执行 `dws.cmd auth login --device --format json` |
| `PAT_MEDIUM_RISK_NO_PERMISSION` | 缺少行为授权 | 执行 `dws.cmd pat chmod --products contact,chat --grant-type permanent --yes --format json` |
| 手机号查询成功但没有 `userId` | 返回为空或手机号不在通讯录 | 改用姓名搜索 |
| 姓名搜索无结果 | 通讯录不可见或姓名不一致 | 不发送，人工核实 |
| 发送成功但需要追溯 | DWS 返回 `openTaskId` | 保存到发送结果表 |
| 只发了标题没有正文 | 同时传了 `--title` 和 `--text`，客户端展示异常 | 普通通知只传 `--text`，标题写入正文第一行 |

---
author: Lydia
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=Mzg2NzA1MzA5MQ==&mid=2247484055&idx=1&sn=98569ad15fb6db2338264de6bddc9ce0&chksm=cf8d87820efdaf0187c09be7d41b9149261b2088829652b7a1794f251e7367c6735770506e2b&mpshare=1&scene=1&srcid=0504zE5oL4OGjNBnr5oyoWAE&sharer_shareinfo=457fe1d7652e966ad66b9e08498cc720&sharer_shareinfo_first=bbaebec03122c572857450fafd6b2d03#rd
saved: 2026-08-02 19:32:50
tags:
  - 笔记同步助手
id: 955e3c4f-743e-42a3-a525-a11206bbe336
---

公众号名称：左走右走

作者名称：Lydia

发布时间：2026-04-21 15:49

# 一、背景

如果你平时会用 Obsidian 做笔记、整理知识，可能已经不满足于“只记录”，而是开始希望它能帮你一起完成更多事情：比如直接在笔记里调用 AI、辅助写作、整理思路，甚至配合编程工具一起工作。

而Claudian 插件 + Codex，就是一个很适合折腾型用户的组合。前者让 Obsidian 拥有更强的 AI 交互能力，后者则更偏向代码生成与开发辅助。把这两者串起来之后，你就可以在自己熟悉的知识管理环境里，一边记录，一边调用 AI 协助思考和执行，整个流程会顺很多。

# 二、安装步骤

步骤1：先安装BRAT插件

![[00 临时箱/images/ed1c07dc6c5aa6b03ab07f3febfd0603_MD5.png]]

![[00 临时箱/images/daead60e660ced6c00a295bee8bbf982_MD5.png]]

步骤2：通过该插件安装claudian，填写仓库链接，并且选择最新版本

github地址：https://github.com/YishenTu/claudian

![[00 临时箱/images/75446168d88716cb3fbcca45a27e1cf8_MD5.png]]

![[00 临时箱/images/c21e6a258ca43a1e9a9db643c6d147e5_MD5.png]]

![[00 临时箱/images/72894ee2d3a19f9eab88743390722243_MD5.png]]

创建成功之后就可以查看到

![[00 临时箱/images/02ba0a058e6a78e41a8a2544f87b3b1d_MD5.png]]

步骤3：打开终端配置codex：安装codex cli

```
1、Codex CLI 依赖 Node.js 20 或更高版本。安装前先在终端确认版本：
node --version

2、确认 Node.js 版本没问题后，运行以下命令全局安装：
npm install -g @openai/codex

如果是Mac，提示没有权限，可使用sudo命令
sudo npm install -g @openai/codex

3、安装结束后，可查看版本号，确认是否安装成功
codex --version
```

步骤4：配置codex的API KEY

https://platform.openai.com/api-keys

![[00 临时箱/images/6632a4df2d12f05d51efa94ec6fa791c_MD5.png]]

步骤5：把上面生成的KEY配置到文件中

mac电脑中的命令如下：

在终端中依次运行以下两条命令即可，把sk-你的密钥替换成你刚才复制的真实 Key：

```
mkdir -p ～/.codex
```

```
cat > ～/.codex/auth.json << 'EOF'
{
"OPENAI_API_KEY": "sk-你的密钥"
}
EOF
```

完成后可以验证一下文件内容是否写入正确：

```
cat ～/.codex/auth.json
```

步骤6：回到obsidian里运行claudian里的codex

![[00 临时箱/images/4066f16c5dafeb89bf51e00fb88505b6_MD5.png]]

在终端输入which codex，得到地址

![[00 临时箱/images/5a26ec52523be42dfe1619729fd5cadb_MD5.png]]

步骤7：上述配置好后，点击图标即可使用

![[00 临时箱/images/006e0ec4bd5a3346d7e25efdab597bf9_MD5.png]]

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/eebeb764_1785670368997?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg2NzA1MzA5MQ%3D%3D%26mid%3D2247484055%26idx%3D1%26sn%3D98569ad15fb6db2338264de6bddc9ce0%26chksm%3Dcf8d87820efdaf0187c09be7d41b9149261b2088829652b7a1794f251e7367c6735770506e2b%26mpshare%3D1%26scene%3D1%26srcid%3D0504zE5oL4OGjNBnr5oyoWAE%26sharer_shareinfo%3D457fe1d7652e966ad66b9e08498cc720%26sharer_shareinfo_first%3Dbbaebec03122c572857450fafd6b2d03%23rd&s=obsidian)
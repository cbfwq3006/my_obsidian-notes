

原创 AI知行记 AI知行记

 _2026年2月3日 08:00_ _湖南_ 2人

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/FZlaAKiaPnTibyEma9oYphYPRZ2MBGKGlquK9Kf7224BMYrE0TL2JJ5ficYBlZkE9lBsniazoaZNv2zkPMD2LpG9cQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

万众瞩目的 OpenClaw， Github 上 Star 已经快 150k 了，名字也又从 Moltbot 改成了 OpenClaw。

这么一个开源免费的个人 AI 助手，不部署一套玩一下都会担心下次饭桌上吹牛跟不上节奏。考虑到大部分人个人电脑用的是 Windows 系统，所以周末花了半天多时间在自己的 Windows 台式机上部署了一下，并通过飞书机器人完成了对接，实测已经可以完美地做你的牛马替你干活了。

废话不多说，直接上“手把手”教程吧。

1. 安装配置 OpenClaw

1.1 使用管理员身份打开 powershell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhely7OwcFTcYV8pNQaRibYJNzSJgbnvPzsHD0Ok1pRgfsonibS2WibzouYQ/640?wx_fmt=png&from=appmsg)

1.2 安装 openclaw

在 powershell 中执行命令

```
iwr -useb https://openclaw.ai/install.ps1 | iex
```

在接下来的选项中，依次选 Yes、QuickStart，模型供应商国内可选 Qwen、Z.AI (智谱AI），我选择 Z.AI，如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhetCMd1K0akYcxgRMX0N0Oib2o5hqsAqYiblwDEk6Quqkee0vnGuCXialnA/640?wx_fmt=png&from=appmsg)

1.3 配置智谱 AI API KEY

通过如下链接登录智谱 AI，

```
https://www.bigmodel.cn/invite?icode=xe46nEMIgV8s2jDW8Da6vpmwcr074zMJTpgMb8zZZvg%3D
```

复制一个 API KEY，没有就创建一个（实名认证后，会送一些免费额度，别人通过你的邀请链接注册实名后，也可获取 Token 资源包），如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheGiaicbntePrOiaic8FMTT515geXDmhEYw8D9Tb6FMVhREztaUXM7w8UoMQ/640?wx_fmt=png&from=appmsg)

回到 powershell，将复制的 API KEY 粘贴进去，并设置模型为默认的 GLM-4.7, 如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhed2Y6jrNnf8e1dzlZg0glEooJ8IXENkegF2bj1Ricy9K1d9jsNrVqO6A/640?wx_fmt=png&from=appmsg)

1.4 完成其余配置

渠道配置这里先选择 Skip for now，后面我们再配置飞书渠道，如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheXtZkicUOtEfWObibNCaPKW4Ac9dWz7FyPW32ze0JB0FaybypAYuzQagA/640?wx_fmt=png&from=appmsg)

后面的 skills， hooks，都可以暂时先不添加，分别选择 No， Skip for now， 如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheIibybCgBwInQsJIdSPFgsA4GfZ6HfMzTicLSRMSqdMkXT6vAF7Z9nOrg/640?wx_fmt=png&from=appmsg)

到这里，网关服务就已经安装并启动了，可以通过下图红框中带 token 的链接在浏览器中打开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheIibjZdsc64OEcibAAmRwicb1KpCAE4wJAiaRDpJtiawNXCgfb0X4iboLoPeA/640?wx_fmt=png&from=appmsg)

最后，在如何创建机器人时选择 Open the Web UI, 是否安装 shell 自动补全脚本时，选 Yes、No都行（选 YES 应该是可以通过 Tab 键自动补全 openclaw 命令）， 如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhesiaG9ZfmBEZT6rhYO9laibC6pK2jJol2uZhIUtYrQMLVwSsnS8HD8mFQ/640?wx_fmt=png&from=appmsg)

1.5 验证

在浏览器上打开带有 token 的链接，在聊天窗口中输入内容，若正常回应，则表示 openclaw 已成功安装，并可通过云模型提供服务，如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhe0yic0ViaSGJVHL2pWc2AVXNPYLKgGK9TY7WUz9MSI9VyVP7qo5xP1tDg/640?wx_fmt=png&from=appmsg)

2. 配置飞书机器人

2.1 创建机器人应用 

登录飞书开放平台：https://open.feishu.cn/，进入“开发者后台”，点击“创建企业自建应用”，创建一个应用，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheza7pBtK2vLZMoeMPvDKQMJwKpMXcHm1aibmficiaexFAVVV5RSkgrHxwg/640?wx_fmt=png&from=appmsg)

创建完成后，添加机器人能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhelJj2ic4WfYLK1oricL9IPs2hDo5RYEnpCoicPXA0hwaf5oR1gnia9ybzOg/640?wx_fmt=png&from=appmsg)

配置机器人显示名称。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheOQj4n4HjkSh0d5j6RBPEgYq7lIeVjm5zibUhUaNZnyOfI0eLNOC3F9g/640?wx_fmt=png&from=appmsg)

2.2 配置权限

至少开通如下6个权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheHMa01Q59ia9ic6g56BeABcdVPvCWFGHhbtAl7DtL8o4yJ2n3mXdFwzWA/640?wx_fmt=png&from=appmsg)

2.3 “尝试”配置事件与回调

之所以用“尝试”，是因为这里直接配置不会成功，我一开始也是这么踩坑的。

飞书事件与回调的长连接配置需要客户端先与平台建立长连接才可配置，否则会提示下图所示错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhe7OHYxO4KU3f0dkGoX8icJxVBkfwbKcpvgtkibvM7mJIiaunjsNDewxhoQ/640?wx_fmt=png&from=appmsg)

因此我们需要先到2.4安装 openclaw 的飞书插件，并启用它建立连接后，才可进行事件与回调的配置。

2.4 安装飞书插件

使用如下命令安装飞书插件。

```
openclaw plugins install @m1heng-clawd/feishu
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheNvn2thX04oLl4cFD2iaxib02Vvvpcbdw5orcZyEQjhFO5hFfiaibEFFekg/640?wx_fmt=png&from=appmsg)

若出现如上图所示“spawn npm ENOENT”错误，则可改用下载安装包的方式安装，命令为，

```
 curl.exe -O https://registry.npmjs.org/@m1heng-clawd/feishu/-/feishu-0.1.3.tgz
```

执行结果如下图（若安装包本地安装的方式仍提示“spawn npm ENOENT”错误，可多试几下）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheuqaaaTx0htpIG8SIrE5rOh70icaC6yz8twdtFaZjg3quibziaUAiaPWjvg/640?wx_fmt=png&from=appmsg)

上面重试后，未报“spawn npm ENOENT”错误，但是提示找不到'@larksuiteoapi/node-sdk'的模块，可通过如下命令安装（若提示其它模块同样手动再安装一下），注意该命令需在“C:\Users\Administrator\.openclaw>”目录下执行，

```
npm install @larksuiteoapi/node-sdk --save
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheL9YmrmsxxibRfvTnHxCBzYibHCvQ88qqybkKoRsWzZx3BpUEibbuezpBw/640?wx_fmt=png&from=appmsg)

2.5 配置与启用飞书插件

通过如下命令配置飞书插件，

```
openclaw config set channels.feishu.appId "cli_xxxxx"
```

其中的appId, appSecret 为飞书机器人的应用凭证，如图。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheUs4ldnoeTTmf4ibjMpZMO8P5b3GibBhKjqFG81Zh6VFWBmrzIoSznJtg/640?wx_fmt=jpeg)

命令执行结果如图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhelG8IMPewuSdKEf57wibXmOLb4ozGV37Cm6DCEsO3XrGoqtK9zMXs7og/640?wx_fmt=png&from=appmsg)

配置完成后， 重启网关服务，使其生效。

```
openclaw gateway restart
```

重启后，命令行窗口显示已与飞书平台建立长连接，此时即可到飞书平台配置事件与回调了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheeaT8GqRULmibhSb1Ya65hnBkdjhoC48WJzsbQL35UEJfF86FHibK5yvg/640?wx_fmt=png&from=appmsg)

2.6 配置事件与回调

回到飞书“开发者后台”，将事件配置为“使用 **长连接** 接收事件”， 并添加如下4个事件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhe6l2ZibSzQAw7mgd4edEZs0BQCUL2aiaEvriaq16p78rib1WciaxlIic60CxA/640?wx_fmt=png&from=appmsg)

将回调也配置为“使用 长连接 接收回调”，并添加“卡片回传交互”的回调，如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheib4Pibqfe5cHKMysvpRjMRiadsDmYAWweRmm8fHOHzK8Vm2Fu9q3VicpIQ/640?wx_fmt=png&from=appmsg)

2.7 发布版本

最后，创建版本，填写信息后确定发布。至此，机器人应用就已配置发布完成了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnhexGUaRgdDOFRh3YhBcuw2IEItQpqt8pnSdQ0OPyicib7KHuNa5icibfNH1Q/640?wx_fmt=png&from=appmsg)

3. 实测验证

打开飞书APP，点击搜索按钮，通过机器人名称搜索到机器人。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheCfMwSEIG43fDxtKdPa8icy3R02YtzVMV5AewGRb5LN7ax1swFN6ENFQ/640?wx_fmt=png&from=appmsg)

  

这里我以一个整理相册的场景来实测一下，整个对话内容如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheo9LgtegA999cp4FuaMjicX28LOibe0X16yKkZ2l8flfoia6xZ4Pf97tWw/640?wx_fmt=jpeg&from=appmsg)

从明确任务到告知已整理完成，差不多花了2分钟的样子，回到电脑上查看，确实已将指定文件夹下的所有照片按年份进行了规整，完美完成验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FZlaAKiaPnTiblbqNSYmCB19UCSpf1dnheYn7x2PFicjFbByiaibQLFsxVn2uQ4afBsUWmWjh946THLqbibWb6MDcqDQ/640?wx_fmt=png&from=appmsg)
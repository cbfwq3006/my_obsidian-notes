kimopig *2026年4月15日 23:45*

前段时间同学@年轻人啊撸起袖子加油干 大肆赞美飞书CLI，勾起了我的好奇心，因为我绝大部分知识文档也在飞书。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/4AqhHF5EicR1muuNFmicFChObqymj3g5TpC7qJ10lqoTf9ibxk22FU5zFYPyOp8HgtGVB8nciaNU3ibzxle1icICMqVkkjlzLIAmsYWmySva2R3As/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

碰巧最近我有一个学习GDPR法规的需求（涉及到欧盟地区数据出入境），

GDPR正文一共56页，11个章节，99条法条，全英文看的头疼。虽然网上可以找到全文翻译，但是中英文在两个pdf里，阅读、理解、做笔记非常不方便，看着看着就迷失了。。。。。。

因此我想着，拿飞书CLI来试试水，基于原文和翻译版的pdf，做一个中英文逐条对照的GDPR知识库。

---

开干！

首先，安装飞书cli

这个很简单，按照飞书提供的文档一步一步走就行（可以点击阅读原文）：

```
npm install -g @larksuite/clinpx skills add https://github.com/larksuite/cli -y -g
```

安装完后，会发现Trae、Cursor、Codex、Claude code这些应用的skills文件夹里会新增飞书相关的skill。

我们以Trae为例：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

或者是Codex：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后做初始化。执行下面代码后，终端里会出现一个链接。打开链接，按提示完成初始化流程后，飞书开发者平台里就会创建出一个新的应用，AI Agent 就可以通过安装到本地的飞书 skills 调用 lark-cli 来访问飞书里的资源：

```
lark-cli config init --new
```
![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

接着完成授权：

```
lark-cli auth login
```

执行后会进入一个交互式界面，你可以按自己的需要勾选要授权的业务域，比如文档、知识库、云空间这些。授权完成后，这个应用就可以在你允许的范围内访问对应的飞书资源了。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

如果已经明确只需要某一类能力，也可以用 --domain 或 --scope 的方式做更精确的授权。

```
lark-cli auth login --domain docs
```

准备工作做好后，我们进入主题：

首先，不得不说，markitdown真的太香了。借用markitdown，两个pdf在一分钟内完成了markdown格式文件的转换。

接着，我让Codex帮我把法条逐一做成树状结构，放进GDPR知识库里：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后，让它给每个文档增加超链接：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后，就是最重要、最需要保证正确率的环节，将中文精准地插入到每段英文下方：

这里我没有让它一次性整篇导入，而是按法条一条一条地插入中文翻译。每插入一条，都要回读核对，确认没问题之后，才能继续下一条。整个过程里，Codex 也非常谨慎，时不时就会停下来找我确认。最后前前后后一共用了 4 个大对话，才算全部搞定，真的非常非常费 token！！！！

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

最后展示一下成果：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

后面我阅读GDPR就方便多啦！！！！

最后感谢一下优秀青年 @年轻人啊撸起袖子加油干

就这么多，发射🚀！！

MyAIExploration · 目录

阅读原文

继续滑动看下一个

睡不醒的DBP

向上滑动看下一个
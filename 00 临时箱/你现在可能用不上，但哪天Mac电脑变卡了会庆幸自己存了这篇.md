---
author: arthinking
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzA3NDM5Nzg3OA==&mid=2452767834&idx=1&sn=ad58d32c7a6b2c5ec16ecf41e73b865a&chksm=898f680777d5504d3374fbf5bfd238a6db959d3916cc04d18ab2e4e6de3b6c049c1742d7b009&mpshare=1&scene=1&srcid=0803GJynAxraQzTkNt0ReyuJ&sharer_shareinfo=4eb4ac1313b35127d768939c2abc1563&sharer_shareinfo_first=4eb4ac1313b35127d768939c2abc1563#rd
saved: 2026-08-03 10:04:25
tags:
  - 笔记同步助手
id: dd3196e5-6f4c-4bb1-8620-5264e83972cf
---

公众号名称：AppGuide

作者名称：arthinking

发布时间：2026-07-31 08:22

当你的Mac系统用了好几年了，随着不断的升级系统，可能会发现越来越卡。这个时候，你也许有这个疑惑：如果我把它装回刚买回来的那个时候的系统，它还会卡吗？而且现在Mac都涨价这么多了，旧设备能接着用就用着先，不是更划算吗？

刚好手头有一台2019年的MacBook Pro，由于使用越来越卡，后边升级到了其他设备区做主力工作了。之前也有提到，macOS 26 Tahoe出来时候，第一时间用它升级体验了最新系统，结果系统就开始变更响应更迟钝了。今天我们就用它来做一个实际测试。

![[00 临时箱/images/c5070d3643408e2cd7f1d62643f2794b_MD5.jpg]]

MacBook Pro 2019

## 恢复到出厂系统

当然，恢复到出厂系统，也就意味着里面的任何数据都没了，所以，你需要先备份好资料，再操作。我这台机器所有有用的东西已经都已经同步到了云端或者其他主力机。所以可以直接开干。

我们先关机，然后开机，立刻同时按住 `Shift + Option + Command + R`，一直按着，直到你看到 Apple 标志、旋转地球后再松手。因为这个组合属于 **Internet Recovery**，所以它会通过网络进入恢复环境。

![[00 临时箱/images/f017d8310cb2e0dc06ca9d58e5a87cc2_MD5.jpg]]

恢复到出厂系统

之后会让你连接WIFI：

![[00 临时箱/images/b79b957ecd00f18e9a922b4c6f61446d_MD5.jpg]]

连接WIFI

如果系统要求，输入你的Mac登录密码。

接着会进入会界面，如下图：

![[00 临时箱/images/b1a5fad977b317870f974be797f02992_MD5.jpg]]

macOS Utilities

打开磁盘工具：

选中启动盘，比如Macintosh HD，点击抹除（我这里目录有点问题，后面会说到）：

![[00 临时箱/images/cdebdee983bbbe5fba89e3d40663d3e1_MD5.jpg]]

磁盘工具

抹掉完成后，退出磁盘工具。回到恢复界面，点 **重新安装 macOS**：

![[00 临时箱/images/f41fad629eb7979bd7cb541f63993c63_MD5.jpg]]

重新安装 macOS

按提示完成安装即可。更多说明，可以参考官方文档：

![[00 临时箱/images/8f3752ae746ce7a15211516c8e76e33c_MD5.png]]

最终，恢复到了出厂系统。不过旧系统流畅是流畅，回忆一下子拉回了刚买这台设备开机的那时候，操作起来非常丝滑，跟当时新机器没太大区别。也很怀旧，但是用起来竟然有点不习惯了。忘记截图就匆匆升级到了15系统。

### 关于格式化磁盘的问题

在格式化磁盘时候，发现我这里点了之后没反应：

![[00 临时箱/images/b1ad0ee65b6e0f11e0c2520c712dd39f_MD5.jpg]]

格式化磁盘

先把磁盘结构展开来：（在“磁盘工具”里点： **显示 → 显示所有设备（View > Show All Devices）**）

看磁盘结构，似乎是有点问题。于是只能通过终端区抹除： 先在恢复模式里打开 **终端**，然后执行命令：`diskutil list`，先确认你的内置物理盘是不是 `/dev/disk0`。确认后再执行：

```
diskutil unmountDisk force /dev/disk0
diskutil eraseDisk APFS "Macintosh HD" GPT /dev/disk0
```

这两个命令的意思是：

-   强制卸载整块盘
    
-   直接把整块物理盘抹成 **APFS**
    
-   分区方案用 **GUID Partition Map**
    

## 恢复之后如何升级到指定版本

在重置到出厂系统的时候，如果你在系统设置里面升级系统，一般是直接让你升级到最新的系统的：

![[00 临时箱/images/838c85a152e6311fb5a64281070eeeeb_MD5.jpg]]

升级到指定版本

如果你想升级到特定版本的系统，可以根据这里的指引进行下载升级：

![[00 临时箱/images/1fe1d2c217c893a7b525ef89a07bf481_MD5.png]]

最终，为了升级已经用习惯了的新系统的风格，同时为了能够安装新软件，避免太老系统的系统漏洞问题，这台机器升级到了比较新的跑起来还算流畅的系统 macOS Sequoia 15.7.5。

## 关于M芯片的Mac

关于其他的启动快捷键，如果大家使用的不熟练，这里也给大家说明下，避免大家按错（以下是针对Intel机型的快捷键）：

-   `Command + R`：重装你当前这台 Mac 上的`当前版本` macOS；
    
-   `Option + Command + R`：安装这台 Mac `兼容的最新版本` macOS；
    
-   `Shift + Option + Command + R`：安装这台 Mac `出厂自带的版本，或最接近仍可用的版本`。
    

而如果你是使用的M芯片的Mac，操作方式有点不同：需要在关机后，长按电源键直到看到“正在载入启动选项”或出现“选项”，然后点 **选项 → 继续** 进入恢复环境。M芯片的Mac在恢复环境下可以重装 macOS，但默认安装的并不是出厂系统版本，而是最近安装过的 macOS 当前版本。

如果 M 芯片 Mac 想安装某个指定版本的 macOS，可以先在终端执行 `softwareupdate --list-full-installers`，查看当前这台机器还能下载哪些完整安装器：

![[00 临时箱/images/1cd6373c37b91b676d1cde7c187e5cde_MD5.png]]

安装器

然后再下载指定版本：`softwareupdate --fetch-full-installer --full-installer-version 版本号`

需要注意，这种方式只能下载这台 Mac 兼容且 Apple 当前仍提供的版本，并不等于一定能恢复到最初出厂版本。下载完成后，还需要运行安装器，或者制作启动盘后再安装。

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/9eae4dbe_1785722663344?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA3NDM5Nzg3OA%3D%3D%26mid%3D2452767834%26idx%3D1%26sn%3Dad58d32c7a6b2c5ec16ecf41e73b865a%26chksm%3D898f680777d5504d3374fbf5bfd238a6db959d3916cc04d18ab2e4e6de3b6c049c1742d7b009%26mpshare%3D1%26scene%3D1%26srcid%3D0803GJynAxraQzTkNt0ReyuJ%26sharer_shareinfo%3D4eb4ac1313b35127d768939c2abc1563%26sharer_shareinfo_first%3D4eb4ac1313b35127d768939c2abc1563%23rd&s=obsidian)
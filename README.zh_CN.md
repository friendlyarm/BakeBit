## **BakeBit**

[English](https://github.com/friendlyarm/BakeBit)
[汉语](https://github.com/friendlyarm/BakeBit/blob/master/README.zh_CN.md)


BakeBit 是一个基于 GrovePi 的开源平台, 它连接 NanoPi 上的 BakeBit 传感器.

当前支持的主板: NanoPi NEO, NanoPi NEO2, NanoPi NEO Air.

## 说明

它能够在FriendlyCore、Armbian或Ubuntu Core 系统的 Python3.x 环境工作.

基于尽量充分利用 Debian/Ubuntu 发行版的 APT 包管理器进而达到稳定及更新的目的,
本代码分支在安装过程中放弃使用 Python3 包管理器 (PIP) 并移除老旧依赖库.
由于APT源中依赖库的缺失, 兼容模式的安装脚本未移除PIP.
将依赖库 WiringNP 直接连接于 https://github.com/friendlyarm/WiringNP 并在安装时自动下载更新.

原始实现基于Python2，感谢[CuitGGyy](https://github.com/CuitGGyy/BakeBit)将其移植到Python3.x环境.

## 安装

#### FriendlyCore Xenial / Armbian Stretch / Ubuntu Core Xenial

```
# git clone --depth=1 https://github.com/friendlyarm/BakeBit.git
# cd BakeBit
# sudo -H ./install.sh
```

#### FriendlyCore Focal / Armbian Buster / Ubuntu Core Bionic

```
# git clone --depth=1 https://github.com/friendlyarm/BakeBit.git
# cd BakeBit
# sudo -H ./install-compat.sh
```

演示代码将在系统重新启动后自动运行.

## 协议

The MIT License (MIT)

BakeBit: an open source platform for connecting BakeBit Sensors to the NanoPi NEO.
Copyright (C) 2016 FriendlyARM


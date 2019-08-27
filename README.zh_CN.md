## **BakeBit**

[English](https://github.com/CuitGGyy/BakeBit)
[汉语](https://github.com/CuitGGyy/BakeBit/blob/master/README.zh_CN.md)


BakeBit 是一个基于 GrovePi 的开源平台, 它连接 NanoPi 上的 BakeBit 传感器.

当前支持的主板: NanoPi NEO, NanoPi NEO2, NanoPi NEO Air.

## 说明

本代码分支基于 https://github.com/friendlyarm/BakeBit

它能够在 armbian buster 或 ubuntu-core bionic 系统的 Python3.x 环境工作.

基于尽量充分利用 Debian/Ubuntu 发行版的 APT 包管理器进而达到稳定及更新的目的,
本代码分支在安装过程中放弃使用 Python3 包管理器 (PIP) 并移除老旧依赖库.
将依赖库 WiringNP 直接连接于 https://github.com/friendlyarm/WiringNP 并在安装时自动下载更新.


## 安装

```
# git clone https://github.com/CuitGGyy/BakeBit.git
# cd BakeBit
# sudo -H ./install.sh
```

演示代码将在系统重新启动后自动运行.

## 协议

The MIT License (MIT)

BakeBit: an open source platform for connecting BakeBit Sensors to the NanoPi NEO.
Copyright (C) 2016 FriendlyARM


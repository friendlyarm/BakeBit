## **BakeBit**

[English](https://github.com/friendlyarm/BakeBit)
[汉语](https://github.com/friendlyarm/BakeBit/blob/master/README.zh_CN.md)


BakeBit is an open source platform for connecting BakeBit Sensors to the NanoPi NEO/NEO2. It is based on the GrovePi.

Currently supported boards: NanoPi NEO, NanoPi NEO2, NanoPi NEO Air.

## Introduction

The code work well on armbian or friendlycore (ubuntu-core) with Python 3.x

I abandon using PIP(Python Package Installer) when installing in install.sh, but not in install-compatible.sh, and take full advantage of APT with the latest release packages of distribution.

The original implementation was based on Python2, thanks to [CuitGGyy](https://github.com/CuitGGyy/BakeBit) for porting it to Python 3.x environment.

## Installtion

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

The demo will automatically start at the next reboot.


## License

The MIT License (MIT)

BakeBit: an open source platform for connecting BakeBit Sensors to the NanoPi NEO.
Copyright (C) 2016 FriendlyARM

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

#!/usr/bin/env python
#
# BakeBit example for the basic functions of BakeBit 128x64 OLED
#
# The BakeBit connects the NanoPi NEO and BakeBit sensors.
# You can learn more about BakeBit here:  http://wiki.friendlyarm.com/BakeBit
#
# Have a question about this example?  Ask on the forums here:  http://www.friendlyarm.com/Forum/
#
'''
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
'''

import time
import bakebit
import os
import psutil
from math import log
import multiprocessing
import platform
import socket
import bakebit_128_64_oled as oled

oled.init()                  #initialze SEEED OLED display
oled.clearDisplay()          #clear the screen and set start position to top left corner
oled.setNormalDisplay()      #Set display to normal mode (i.e non-inverse mode)
oled.setPageMode()           #Set addressing mode to Page Mode

byteunits = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
def filesizeformat(value):
    exponent = int(log(value, 1024))
    return "%.1f %s" % (float(value) / pow(1024, exponent), byteunits[exponent])

memUsage = psutil.phymem_usage()
diskUsage = psutil.disk_usage('/')

oled.setTextXY(0,0)
oled.putString("%s" % socket.gethostbyname(socket.gethostname()))

oled.setTextXY(0,1)
oled.putString("Mem:%s" % filesizeformat(memUsage.total))
import time
import bakebit
import os
import psutil
from math import log
import multiprocessing
import platform
import socket
import bakebit_128_64_oled as oled

oled.init()                  #initialze SEEED OLED display
oled.clearDisplay()          #clear the screen and set start position to top left corner
oled.setNormalDisplay()      #Set display to normal mode (i.e non-inverse mode)
oled.setPageMode()           #Set addressing mode to Page Mode

byteunits = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
def filesizeformat(value):
    exponent = int(log(value, 1024))
    return "%.1f %s" % (float(value) / pow(1024, exponent), byteunits[exponent])

memUsage = psutil.phymem_usage()
diskUsage = psutil.disk_usage('/')

oled.setTextXY(0,0)
oled.putString("%s" % socket.gethostbyname(socket.gethostname()))

oled.setTextXY(0,1)
oled.putString("Mem:%s" % filesizeformat(memUsage.total))

oled.setTextXY(0,2)
oled.putString("Usage:%d%%" % memUsage.percent)

oled.setTextXY(0,3)
oled.putString("Disk:%s" % filesizeformat(diskUsage.total))

oled.setTextXY(0,4)
oled.putString("Usage:%d%%" % diskUsage.percent)

oled.setTextXY(0,5)
oled.putString("CPU:%s" % platform.processor())

oled.setTextXY(0,6)
oled.putString("Cores:%d" % multiprocessing.cpu_count())

with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq") as f:
	freq = int(f.readlines()[0])/1000
	freqStr = "%d MHz" % freq
	if freq > 1000:
		freqStr = "%.1f GHz" % (float(freq)/1000.0)
	oled.setTextXY(0,7)
	oled.putString("Freq:%s" % freqStr)
oled.setTextXY(0,2)
oled.putString("Usage:%d%%" % memUsage.percent)

oled.setTextXY(0,3)
oled.putString("Disk:%s" % filesizeformat(diskUsage.total))

oled.setTextXY(0,4)
oled.putString("Usage:%d%%" % diskUsage.percent)

oled.setTextXY(0,5)
oled.putString("CPU:%s" % platform.processor())

oled.setTextXY(0,6)
oled.putString("Cores:%d" % multiprocessing.cpu_count())

with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq") as f:
	freq = int(f.readlines()[0])/1000
	freqStr = "%d MHz" % freq
	if freq > 1000:
		freqStr = "%.1f GHz" % (float(freq)/1000.0)
	oled.setTextXY(0,7)
	oled.putString("Freq:%s" % freqStr)



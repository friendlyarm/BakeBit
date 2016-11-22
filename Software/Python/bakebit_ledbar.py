#!/usr/bin/env python
#
# BakeBit Example for using the BakeBit LED Bar (http://wiki.friendlyarm.com/wiki/index.php/BakeBit_-_LED_Bar)
#
# The BakeBit connects the NanoPi NEO and BakeBit sensors.
# You can learn more about BakeBit here:  http://wiki.friendlyarm.com/BakeBit
#
# Have a question about this example?  Ask on the forums here:  http://www.friendlyarm.com/Forum/
#
'''
## License

The MIT License (MIT)

BakeBit for the NanoPi NEO: an open source platform for connecting BakeBit Sensors to the NanoPi NEO.
Copyright (C) 2016  FriendlyARM

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
import random

# Connect the BakeBit LED Bar to digital port D3
# DI,DCKI,VCC,GND
ledbar = 3

bakebit.pinMode(ledbar,"OUTPUT")
time.sleep(.2)
i = 0
old_color = 0

bakebit.bakeBitLedBar_Init(ledbar, 0, 5)
time.sleep(.5)

while True:
    try:
        for i in range(0,5):
            color16bit = bakebit.Green
            if i >= 1:
                color16bit = color16bit | (bakebit.Green << 3)
            if i >= 2:
                color16bit = color16bit | (bakebit.Green << 6)
            if i >= 3:
                color16bit = color16bit | (bakebit.Yellow << 9)
            if i >= 4:
                color16bit = 0
                color16bit = color16bit | bakebit.Red
                color16bit = color16bit | (bakebit.Red << 3)
                color16bit = color16bit | (bakebit.Red << 6)
                color16bit = color16bit | (bakebit.Red << 9)
                color16bit = color16bit | (bakebit.Red << 12)
            if color16bit != old_color:
                old_color = color16bit
                lowBits = color16bit & 255
                highBits = (color16bit & (255 << 8)) >> 8
                bakebit.bakeBitLedBar_Show(ledbar, highBits, lowBits)
            time.sleep(1)
    except KeyboardInterrupt:
        bakebit.bakeBitLedBar_Release(ledbar)
        time.sleep(.5)
        break
    except IOError:
        print ("Error")

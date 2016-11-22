#!/usr/bin/env python
#
# BakeBit example for the basic functions of BakeBit 128x64 OLED and Joystick
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

import bakebit_128_64_oled as oled
import bakebit
import time


oled.init()                  #initialze SEEED OLED display
oled.clearDisplay()          #clear the screen and set start position to top left corner
oled.setNormalDisplay()      #Set display to normal mode (i.e non-inverse mode)
oled.setPageMode()           #Set addressing mode to Page Mode

# Uses two pins - one for the X axis and one for the Y axis
# This configuration means you are using port A0
xPin = 0
yPin = 1
bakebit.pinMode(xPin,"INPUT")
bakebit.pinMode(yPin,"INPUT")

texts = ["Wi-Fi"
    , "Bluetooth"
    , "Media Vol"
    , "Alarm Vol"
    , "FontSize"
    , "Brightness"
    , "Dim" ]

values = [True
    , False
    , 50
    , 50
    , 9
    , 80
    , 30 ]

opIndex = 0
m = int(1024.0/5)
while True:
    try:
        # Get X/Y coordinates
        x = bakebit.analogRead(xPin)
        y = bakebit.analogRead(yPin)

        oled.setTextXY(0,0)
        oled.putString("[Settings]")

        if x<m:
            # left
            print("left")
            if type(values[opIndex]) is int:
                values[opIndex]=values[opIndex]-1
                if values[opIndex]<0:
                    values[opIndex] = 0
            elif type(values[opIndex]) is bool:
                values[opIndex] = not values[opIndex]

        elif x>(1024-m):
            # right
            print("right")
            if type(values[opIndex]) is int:
                values[opIndex]=values[opIndex]+1
                if values[opIndex]>999:
                    values[opIndex] = 999
            elif type(values[opIndex]) is bool:
                values[opIndex] = not values[opIndex]
        elif y<m:
			opIndex = opIndex - 1
        elif y>(1024-m):
			opIndex = opIndex + 1
        elif opIndex<0:
			opIndex=6
        elif opIndex>6:
			opIndex=0

        for i in range(7):
            oled.setTextXY(0,i+1)
            valueStr = ""
            if type(values[i]) is int:
                valueStr = str(values[i])
            elif type(values[i]) is bool:
                if values[i]:
                    valueStr = "On"
                else:
                    valueStr = "Off"
            for j in range(3-len(valueStr)):
                valueStr = " " + valueStr

            title = texts[i]
            if len(title) > 10:
                title = title[:10]

            for j in range(10-len(title)):
                title = title + " "

            if opIndex == i:
                oled.putString("> " + title + " " + valueStr)
            else:
                oled.putString("  " + title + " " + valueStr)
    	print("x =", x, " y =", y, " opIndex=", opIndex)	

    except IOError:
        print ("Error")


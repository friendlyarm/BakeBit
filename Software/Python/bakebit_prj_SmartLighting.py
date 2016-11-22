#!/usr/bin/env python
#
# BakeBit Example for using the BakeBit Light Sensor and the LED Bar together to turn the LED Bar On and OFF.
# Modules:
# 	http://wiki.friendlyarm.com/wiki/index.php/BakeBit_-_Light_Sensor
# 	http://wiki.friendlyarm.com/wiki/index.php/BakeBit_-_Red_LED
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

# Connect the BakeBit Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the BakeBit LED Bar to digital port D3
# DI,DCKI,VCC,GND
ledbar = 3


lowThreshold = 500
highTreshold = 600

bakebit.pinMode(light_sensor,"INPUT")
bakebit.pinMode(ledbar,"OUTPUT")
time.sleep(.2)
bakebit.bakeBitLedBar_Init(ledbar, 0, 5)
time.sleep(.5)
old_color = 0

while True:
    try:
        light_count = 0

        # Get sensor value
        sensor_value = bakebit.analogRead(light_sensor)
        if sensor_value > highTreshold:
            f=(1023-highTreshold)/4
            light_count =  (sensor_value-highTreshold)/f+1

            # turn on ledbar
            color16bit = bakebit.Green
            if light_count > 1:
                color16bit = color16bit | (bakebit.Green << 3)
            if light_count > 2:
                color16bit = color16bit | (bakebit.Green << 6)
            if light_count > 3:
                color16bit = color16bit | (bakebit.Green << 9)
            if light_count > 4:
                color16bit = 0
                color16bit = color16bit | bakebit.Blue
                color16bit = color16bit | (bakebit.Blue << 3)
                color16bit = color16bit | (bakebit.Blue << 6)
                color16bit = color16bit | (bakebit.Blue << 9)
                color16bit = color16bit | (bakebit.Blue << 12)

            if color16bit != old_color:
                old_color = color16bit
                lowBits = color16bit & 255
                highBits = (color16bit & (255 << 8)) >> 8
                bakebit.bakeBitLedBar_Show(ledbar, highBits, lowBits)

        elif sensor_value < lowThreshold:
            # turn off ledbar
            bakebit.bakeBitLedBar_Show(ledbar, 0, 0)

        print("sensor_value = %d light_count =%d" %(sensor_value,  light_count))
        time.sleep(.5)

    except KeyboardInterrupt:
        bakebit.bakeBitLedBar_Release(ledbar)
        time.sleep(.2)
        break
    except IOError:
        print ("Error")

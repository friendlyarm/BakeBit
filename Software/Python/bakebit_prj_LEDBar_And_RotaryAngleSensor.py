#!/usr/bin/env python
#
# BakeBit Example for using the BakeBit LED Bar (http://wiki.friendlyarm.com/wiki/index.php/BakeBit_-_LED_Bar)
#
# The BakeBit connects the NanoPi NEO and BakeBit sensors.  You can learn more about BakeBit here:  http://wiki.friendlyarm.com/bakebit
#
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
import random

# Connect the BakeBit LED Bar to digital port D3
# DI,DCKI,VCC,GND
ledbar = 3

# Connect the BakeBit Rotary Angle Sensor to analog port A0
# SIG,NC,VCC,GND
potentiometer = 0

# Reference voltage of ADC is 5v
adc_ref = 5

# Vcc of the bakebit interface is normally 5v
bakebit_vcc = 5

# Full value of the rotary angle is 360 degrees, as per it's specs (0 to 360)
full_angle = 360

bakebit.pinMode(potentiometer,"INPUT")
bakebit.pinMode(ledbar,"OUTPUT")
time.sleep(1)

# LED Bar methods
# bakebit.bakeBitLedBar_Init(pin, chipset, numOfLED)
# bakebit.bakeBitLedBar_Release(pin)
# bakebit.bakeBitLedBar_Show(pin,colorHigh,colorLow)

bakebit.bakeBitLedBar_Init(ledbar, 0, 5)
time.sleep(.5)

old_color = 0
while True:
    try:
        # Read sensor value from potentiometer
        sensor_value = bakebit.analogRead(potentiometer)

        # Calculate voltage
        voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

        # Calculate rotation in degrees (0 to 360)
        degrees = round((voltage * full_angle) / bakebit_vcc, 2)
        print("sensor_value = %d voltage = %.2f degrees = %.1f" % (sensor_value, voltage, degrees))

        color16bit = 0
        if degrees > 0:
            color16bit = color16bit | bakebit.Green
        if degrees > 72:
            color16bit = color16bit | (bakebit.Green<<3)
        if degrees > 144:
            color16bit = color16bit | (bakebit.Green << 6)
        if degrees > 216:
            color16bit = color16bit | (bakebit.Yellow << 9)
        if degrees > 288:
            color16bit = color16bit | (bakebit.Red << 12)
        if degrees == 360:
            color16bit = 0
            color16bit = color16bit | bakebit.Red
            color16bit = color16bit | (bakebit.Red << 3)
            color16bit = color16bit | (bakebit.Red << 6)
            color16bit = color16bit | (bakebit.Red << 9)
            color16bit = color16bit | (bakebit.Red << 12)

        if color16bit == old_color:
            continue
        old_color = color16bit

        lowBits = color16bit & 255
        highBits = (color16bit & (255<<8))>>8
        print("%s %s" % ('{0:08b}'.format(highBits), '{0:08b}'.format(lowBits)))
        bakebit.bakeBitLedBar_Show(ledbar, highBits, lowBits)
        time.sleep(.2)

    except KeyboardInterrupt:
        bakebit.bakeBitLedBar_Release(ledbar)
        time.sleep(.2)
        break
    except IOError:
        print ("Error")



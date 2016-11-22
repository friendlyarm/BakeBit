#!/usr/bin/env python
#
# BakeBit Example for using the BakeBit Servo (http://wiki.friendlyarm.com/wiki/index.php/BakeBit_-_LED_Bar)
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

# Connect the servo to digital port D5
# SIG,NC,VCC,GND
servo = 5

# Connect the BakeBit Rotary Angle Sensor to analog port A0
# SIG,NC,VCC,GND
potentiometer = 0

# Reference voltage of ADC is 5v
adc_ref = 5

# Vcc of the bakebit interface is normally 5v
bakebit_vcc = 5

# Full value of the rotary angle is 180 degrees, as per it's specs (0 to 180)
full_angle = 180
old_degrees = -1

bakebit.pinMode(potentiometer,"INPUT")
bakebit.bakeBitServo_Attach(servo)


while True:
    try:
        # Read sensor value from potentiometer
        sensor_value = bakebit.analogRead(potentiometer)

        # Calculate voltage
        voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

        # Calculate rotation in degrees (0 to 180)
        degrees = int((voltage * full_angle) / bakebit_vcc)

        if degrees != old_degrees:
            print("sensor_value = %d voltage = %.2f degrees = %d" % (sensor_value, voltage, degrees))
            bakebit.bakeBitServo_Write(servo, degrees)

        old_degrees = degrees

    except KeyboardInterrupt:
        bakebit.bakeBitServo_Detach(servo)
        break
    except IOError:
        print ("Error")



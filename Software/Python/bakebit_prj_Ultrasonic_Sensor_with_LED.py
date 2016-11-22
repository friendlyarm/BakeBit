#!/usr/bin/env python
#
# BakeBit Example for using the BakeBit Ultrasonic Ranger (http://wiki.friendlyarm.com/wiki/index.php/BakeBit_-_Ultrasonic)
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

import bakebit
import time

# Connect the BakeBit Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4

# Connect the BakeBit LED to digital port D3
led = 3                                                                      

bakebit.pinMode(led,"OUTPUT")
light = 0

while True:
    try:
        # Read distance value from Ultrasonic
	distance = bakebit.ultrasonicRead(ultrasonic_ranger)
        print(distance)
	if distance > 0:
		if distance<10: 
			if light == 0:
				print("\ton")
				bakebit.digitalWrite(led,1)
				light = 1
		else:
			if light == 1:
				print("\toff")
				bakebit.digitalWrite(led,0)
				light = 0
	time.sleep(.2)

    except KeyboardInterrupt:
	bakebit.digitalWrite(led,0)
        break

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")

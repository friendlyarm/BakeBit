# button_buzzer.py
#
# This is an project using the BakeBit Button, Buzzer from the BakeBit starter kit
# 
# In this project, the buzzer starts making a sound when the the button is hold

'''
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
from bakebit import *
import math

buzzer_pin = 3		#Port for buzzer
button = 4		#Port for Button

pinMode(buzzer_pin,"OUTPUT")	# Assign mode for buzzer as output
pinMode(button,"INPUT")		# Assign mode for Button as input
while True:
	try:
		button_status= digitalRead(button)	#Read the Button status
		if button_status:	#If the Button is in HIGH position, run the program
			analogWrite(buzzer_pin,0)						
			print "\tOff"			
		else:		#If Button is in Off position, print "Off" on the screen
			analogWrite(buzzer_pin,127)
			print "Buzzing"			
	except KeyboardInterrupt:	# Stop the buzzer before stopping
		digitalWrite(buzzer_pin,0)
		break
	except (IOError,TypeError) as e:
		print("Error")
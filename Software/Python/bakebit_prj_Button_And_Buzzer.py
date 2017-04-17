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
old_button_status = -1
pinMode(buzzer_pin,"OUTPUT")	# Assign mode for buzzer as output
pinMode(button,"INPUT")		# Assign mode for Button as input

buzzer_on = False
old_buzzer_on = not buzzer_on
button_pressed = False

while True:
	try:
		while True:
			button_status = digitalRead(button)	#Read the Button status
			# print button_status
			if old_button_status < 0: 
				break

			if button_status != old_button_status:
				break

		time.sleep(0.2)
		old_button_status = button_status

		if button_status == 0:
			button_pressed = True
		else:
			if button_pressed:
				buzzer_on = not buzzer_on
			button_pressed = False 

		if old_buzzer_on != buzzer_on:
			old_buzzer_on = buzzer_on
			if buzzer_on:
				analogWrite(buzzer_pin,127)
				print "Buzzing"
			else:
				analogWrite(buzzer_pin,0)
				print "\tOff"			
			
		time.sleep(0.2)			
	except KeyboardInterrupt:	# Stop the buzzer before stopping
		digitalWrite(buzzer_pin,0)
		break
	except (IOError,TypeError) as e:
		print("Error")

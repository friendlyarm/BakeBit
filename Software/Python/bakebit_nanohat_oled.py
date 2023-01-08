#!/usr/bin/env python
#
# BakeBit example for the basic functions of BakeBit 128x64 OLED (http://wiki.friendlyarm.com/wiki/index.php/BakeBit_-_OLED_128x64)
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

from __future__ import print_function
import bakebit_128_64_oled as oled
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import sys
import subprocess
import threading
import signal
import os
import socket

global width
width = 128
global height
height = 64

global pageCount
pageCount = 2
global pageIndex
pageIndex = 0
global showPageIndicator
showPageIndicator = False

global last_index
last_index = 0
global options
options = "Options"
global optionA
optionA = "Shutdown?"
global optionB
optionB = "Reboot?"
global statue
statue = "not available"

oled.init()  # initialze SEEED OLED display
oled.setNormalDisplay()  # Set display to normal mode (i.e non-inverse mode)
oled.setHorizontalMode()

global drawing
drawing = False

global image
image = Image.new('1', (width, height))
global draw
draw = ImageDraw.Draw(image)
global fontb24
fontb24 = ImageFont.truetype('DejaVuSansMono-Bold.ttf', 24)
global font14
font14 = ImageFont.truetype('DejaVuSansMono.ttf', 14)
global smartFont
smartFont = ImageFont.truetype('DejaVuSansMono-Bold.ttf', 10)
global fontb14
fontb14 = ImageFont.truetype('DejaVuSansMono-Bold.ttf', 14)
global font11
font11 = ImageFont.truetype('DejaVuSansMono.ttf', 11)

global lock
lock = threading.Lock()


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def draw_page():
    global drawing
    global image
    global draw
    global oled
    global font
    global font14
    global smartFont
    global width
    global height
    global pageCount
    global pageIndex
    global showPageIndicator
    global width
    global height
    global lock
    global options
    global optionA
    global optionB
    global drawing
    global statue

    lock.acquire()
    is_drawing = drawing
    page_index = pageIndex
    lock.release()

    if is_drawing:
        return

    lock.acquire()
    drawing = True
    lock.release()

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    # Draw current page indicator
    if showPageIndicator:
        dotWidth = 4
        dotPadding = 2
        dotX = width-dotWidth-1
        dotTop = (height-pageCount*dotWidth-(pageCount-1)*dotPadding)/2
        for i in range(pageCount):
            if i == page_index:
                draw.rectangle((dotX, dotTop, dotX+dotWidth,
                               dotTop+dotWidth), outline=255, fill=255)
            else:
                draw.rectangle((dotX, dotTop, dotX+dotWidth,
                               dotTop+dotWidth), outline=255, fill=0)
            dotTop = dotTop+dotWidth+dotPadding

    x = 0
    y = 0
    # Move left to right keeping track of the current x position for drawing shapes.
    if int(time.strftime("%M")) % 6 < 0:  # oled shifts every 3 minutes
        x = 2
        y = 2

    if page_index == 0:
        text = time.strftime("%A")
        draw.text((28+x, 0+y), text, font=font14, fill=255)
        text = time.strftime("%e %b %Y")
        draw.text((13+x, 18+y), text, font=font14, fill=255)
        text = time.strftime("%X")
        draw.text((6+x, 33+y), text, font=fontb24, fill=255)

    elif page_index == 1:
        IPAddress = get_ip()
        if (int(time.strftime("%S"))/2) < 10:
            cmd_1min = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
            CPU_1min = subprocess.check_output(
                cmd_1min, shell=True).decode('utf-8')
            CPU = "CPU: %s" % str(int(float(CPU_1min)*100/4)) + "% / 1min"
        elif (int(time.strftime("%S"))/2) < 20:
            cmd_5min = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-1)}'"
            CPU_5min = subprocess.check_output(
                cmd_5min, shell=True).decode('utf-8')
            CPU = "CPU: %s" % str(int(float(CPU_5min)*100/4)) + "% / 5min"
        else:
            cmd_15min = "top -bn1 | grep load | awk '{printf \"%s\", $(NF-0)}'"
            CPU_15min = subprocess.check_output(
                cmd_15min, shell=True).decode('utf-8')
            CPU = "CPU: %s" % str(int(float(CPU_15min)*100/4)) + "% / 15min"
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %d%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True).decode('utf-8')
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell=True).decode('utf-8')
        tempI = int(open('/sys/class/thermal/thermal_zone0/temp').read())
        if tempI > 1000:
            tempI = tempI/1000
        tempStr = "Core Temp: %.1fC" % float(tempI)

        draw.text((x, y+1),       "IP: " +
                  str(IPAddress),  font=smartFont, fill=255)
        draw.text((x, y+1+12),    str(CPU), font=smartFont, fill=255)
        draw.text((x, y+1+24),    str(MemUsage),  font=smartFont, fill=255)
        draw.text((x, y+1+36),    str(Disk),  font=smartFont, fill=255)
        draw.text((x, y+1+48),    tempStr,  font=smartFont, fill=255)

    elif page_index == 3:  # optionA
        draw.text((2, 2),  options,  font=fontb14, fill=255)
        draw.rectangle((2, 20, width-4, 20+16), outline=0, fill=255)
        draw.text((4, 22),  optionA,  font=font11, fill=0)
        draw.rectangle((2, 38, width-4, 38+16), outline=0, fill=0)
        draw.text((4, 40),  optionB,  font=font11, fill=255)

    elif page_index == 4:  # optionB
        draw.text((2, 2),  options,  font=fontb14, fill=255)
        draw.rectangle((2, 20, width-4, 20+16), outline=0, fill=0)
        draw.text((4, 22),  optionA,  font=font11, fill=255)
        draw.rectangle((2, 38, width-4, 38+16), outline=0, fill=255)
        draw.text((4, 40),  optionB,  font=font11, fill=0)

    elif page_index == 5:
        draw.text((2, 10),  statue,  font=fontb14, fill=255)
        draw.text((2, 30),  'Please wait...',  font=font11, fill=255)

    oled.drawImage(image)

    lock.acquire()
    drawing = False
    lock.release()


def is_showing_power_msgbox():
    global pageIndex
    lock.acquire()
    page_index = pageIndex
    lock.release()
    if (page_index == 3) or (page_index == 4):
        return True
    return False


def option_status(st):
    global options, optionA, optionB, statue
    if st == "shutdown":
        options = "Shutdown?"
        optionA = "Yes"
        optionB = "No"
        statue = "shutting down"
    elif st == "reboot":
        options = "Reboot?"
        optionA = "Yes"
        optionB = "No"
        statue = "rebooting"
    else:
        options = "Options"
        optionA = "Shutdown"
        optionB = "Reboot"
        statue = "not available"


def update_page_index(pi):
    global pageIndex
    lock.acquire()
    pageIndex = pi
    lock.release()


def receive_signal(signum, stack):
    global pageIndex
    global options
    global optionA
    global optionB
    global drawing
    global statue
    global last_index

    lock.acquire()
    page_index = pageIndex
    lock.release()

    if page_index == 5:
        time.sleep(1)
        return

    if signum == signal.SIGUSR1:
        print('K1 pressed')
        if is_showing_power_msgbox():
            if page_index == 3:
                update_page_index(4)
            else:
                update_page_index(3)
            draw_page()
        else:
            pageIndex = 0
            draw_page()
        print('K1 released')

    if signum == signal.SIGUSR2:
        print('K2 pressed')
        if is_showing_power_msgbox():
            if page_index == 3:
                if options == "Options":
                    option_status("shutdown")
                    update_page_index(4)
                elif options == "Shutdown?":
                    update_page_index(5)
                elif options == "Reboot?":
                    update_page_index(5)
            else:
                if options == "Options":
                    option_status("reboot")
                    update_page_index(4)
                elif options == "Shutdown?" or options == "Reboot?":
                    option_status("default")
                    pageIndex = last_index
            draw_page()
        else:
            option_status("default")
            update_page_index(1)
            draw_page()
        print('K2 released')

    if signum == signal.SIGALRM:
        print('K3 pressed')
        if is_showing_power_msgbox():
            option_status("default")
            update_page_index(last_index)
            draw_page()
        else:
            last_index = page_index
            update_page_index(3)
            draw_page()
        print('K3 released')


image0 = Image.open('friendllyelec.png').convert('1')
oled.drawImage(image0)
time.sleep(2)

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)
signal.signal(signal.SIGALRM, receive_signal)

while True:
    try:
        draw_page()

        lock.acquire()
        page_index = pageIndex
        lock.release()

        if page_index == 5:
            time.sleep(2)
            while True:
                lock.acquire()
                is_drawing = drawing
                lock.release()
                if not is_drawing:
                    lock.acquire()
                    drawing = True
                    lock.release()
                    oled.clearDisplay()
                    break
                else:
                    time.sleep(.1)
                    continue
            time.sleep(1)
            if options == "Shutdown?":
                os.system('systemctl poweroff')
            else:
                os.system('systemctl reboot')
            break
        elif page_index == 1:
            time.sleep(1)
        else:
            time.sleep(0.2)
    except KeyboardInterrupt:
        break
    except IOError:
        print("Error")

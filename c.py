#c is short for common
#also if you run c.py it refreshes the screen
from PIL import Image,ImageDraw,ImageFont
import os
from waveshare_epd import epd2in13_V3
from gpiozero import Button
from time import sleep
from threading import Thread

#Screen common functions/recources
pic = 'pic'
font24 = ImageFont.truetype(os.path.join('pic', 'Font.ttc'), 24)
font18 = ImageFont.truetype(os.path.join('pic', 'Font.ttc'), 18)
font16 = ImageFont.truetype(os.path.join('pic', 'Font.ttc'), 16)
epd = epd2in13_V3.EPD()

def epd():
    return epd2in13_V3.EPD()

def newImage():
    image  = Image.new(mode='1', size=(250,122), color=255)
    return image

def refresh():
    epd = epd2in13_V3.EPD()
    epd.init()
    epd.Clear(255)

#Button common functions/recources
up = Button(16)
down = Button(20)
select = Button(21)

def rel(pin):
    while pin.is_pressed:
        sleep(0.01)

def getButton():
    if up.is_pressed:
        rel(up)
        return 1
    elif down.is_pressed:
        rel(down)
        return 2
    elif select.is_pressed:
        rel(select)
        return 3
    else:
        return 4
    
def detectPress():
    try:
        while True:
            if up.is_pressed:
                raise NotImplementedError
            if down.is_pressed:
                raise NotImplementedError
            if select.is_pressed:
                raise NotImplementedError
            sleep(0.025)
    except NotImplementedError:
        print("should work")

def threadDetect():
    Thread(target = detectPress).start()

#code to make it refresh
refresh()
#c is short for common
from PIL import Image,ImageDraw,ImageFont
import os
from waveshare_epd import epd2in13_V3

pic = 'pic'
font24 = ImageFont.truetype(os.path.join('pic', 'Font.ttc'), 24)
epd = epd2in13_V3.EPD()

def epd():
    return epd2in13_V3.EPD()

def newImage():
    image  = Image.new(mode=1, size=(250,122), color=255)
    return image
import time
from PIL import Image,ImageDraw,ImageFontimport 
from waveshare_epd import epd2in13_V3

try:
    time_image = Image.new('1', (epd.height, epd.width), 255)
    time_draw = ImageDraw.Draw(time_image)
    
    epd.displayPartBaseImage(epd.getbuffer(time_image))
    num = 0
    while (True):
        time_draw.rectangle((120, 80, 220, 105), fill = 255)
        time_draw.text((120, 80), time.strftime('%H:%M:%S'), font = font24, fill = 0)
        epd.displayPartial(epd.getbuffer(time_image))
        num = num + 1
        if(num == 30):
            break
    
    epd.init()
    epd.Clear(0xFF)
    
    epd.sleep()
except:
    print("Error")
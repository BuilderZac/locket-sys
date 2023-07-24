import time
from PIL import Image,ImageDraw,ImageFont
import c

#try:
epd = c.epd()
epd.init()
epd.Clear(255)
image = c.newImage()
draw = ImageDraw.Draw(image)

epd.displayPartBaseImage(epd.getbuffer(image))

num = 0
while (True):
    #draw.rectangle((120, 80, 220, 105), fill = 255)
    draw.text((120, 80), time.strftime('%H:%M:%S'), font = c.font24, fill = 0)
    epd.displayPartial(epd.getbuffer(image))
    num = num + 1
    if(num == 5):
        break

epd.init()
epd.Clear(0xFF)
epd.sleep()
#except:
#    print("Error")
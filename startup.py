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
    draw.text((5, 5), time.strftime('%H:%M:%S'), font=c.font24, fill=0, align='center')
    epd.displayPartial(epd.getbuffer(image))
    num = num + 1
    if(num == 30):
        break

epd.init()
epd.Clear(0xFF)
epd.sleep()
#except:
#    print("Error")
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

draw.text((35, 40), "Mon Tue Wen Thu Fri Sat Sun", font = c.font24, fill = 0)

num = 0
while (True):
    draw.rectangle((75, 10, 175, 35), fill = 255)
    draw.text((75, 10), time.strftime('%H:%M:%S'), font = c.font24, fill = 0)
    epd.displayPartial(epd.getbuffer(image))
    num = num + 1
    if(num == 60):
        break

epd.init()
epd.Clear(0xFF)
epd.sleep()
#except:
#    print("Error")
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

draw.text((15, 40), "Mon Tue Wen Thu Fri Sat Sun", font = c.font18, fill = 0)
draw.text((15, 40), time.localtime(1)+"/"+time.localtime(2)+"/"+time.localtime(0), font = c.font18, fill = 0)

num = 0
while (True):
    draw.rectangle((75, 5, 175, 30), fill = 255)
    draw.text((75, 5), time.strftime('%H:%M:%S'), font = c.font24, fill = 0)
    epd.displayPartial(epd.getbuffer(image))
    num = num + 1
    if(num == 60):
        break

epd.init()
epd.Clear(0xFF)
epd.sleep()
#except:
#    print("Error")
import time
import datetime
from PIL import Image,ImageDraw,ImageFont
import c

#try:
epd = c.epd()
epd.init()
image = c.newImage()
draw = ImageDraw.Draw(image)
epd.displayPartBaseImage(epd.getbuffer(image))

x = datetime.date.today()
draw.text((5, 40), "Mon Tue Wen Thu Fri Sat Sun", font = c.font18, fill = 0)
draw.text((125, 5), x.strftime('%b/%d/%Y'), font = c.font24, fill = 0)

num = 0
while (True):
    draw.rectangle((15, 5, 115, 30), fill = 255)
    draw.text((15, 5), time.strftime('%H:%M:%S'), font = c.font24, fill = 0)
    epd.displayPartial(epd.getbuffer(image))
    num = num + 1
    if(num == 60):
        break

epd.Clear(255)
epd.sleep()
#except:
#    print("Error")
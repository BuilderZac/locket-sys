import time
import datetime
from PIL import Image,ImageDraw,ImageFont
import c

epd = c.epd()
epd.init()
image = c.newImage()
draw = ImageDraw.Draw(image)

def date():
    x = datetime.date.today()
    draw.text((117, 5), x.strftime('%b/%d/%Y'), font = c.font24, fill = 0)
    day = time.localtime()[6]
    days = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]
    for i in range(7):
        if i == day:
            days[i] = ">" + days[i] + "<"
        draw.text((5 + (i * 40), 40), days[i], font = c.font18, fill = 0)

def homePrint():
    epd.displayPartBaseImage(epd.getbuffer(image))

    currentDay = time.localtime()[7]

    date()

    while (True):
        draw.rectangle((12, 5, 112, 30), fill = 255)
        draw.text((12, 5), time.strftime('%H:%M:%S'), font = c.font24, fill = 0)
        epd.displayPartial(epd.getbuffer(image))

        if currentDay != time.localtime()[7]:
            c.refresh()
            date()

        if c.Button() == 3:
            raise NotImplementedError
        

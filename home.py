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
    draw.text((111, 5), x.strftime('%b/%d/%Y'), font = c.font24, fill = 0)
    day = time.localtime()[6]
    days = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]
    dayString = ""
    for i in range(7):
        if i == day:
            days[i] = ">" + days[i] + "< "
        else:
            days[i] = days[i] + " "
        dayString = dayString + days[i]
    draw.text((10, 40), dayString, font = c.font16, fill = 0)

def homePrint():
    epd.displayPartBaseImage(epd.getbuffer(image))

    currentDay = time.localtime()[7]

    date()

    while (True):
        if c.getButton() == 3:
            print("should raise")
            raise NotImplementedError
        
        draw.rectangle((8, 5, 108, 30), fill = 255)
        draw.text((8, 5), time.strftime('%H:%M:%S'), font = c.font24, fill = 0)
        epd.displayPartial(epd.getbuffer(image))

        if currentDay != time.localtime()[7]:
            c.refresh()
            date()
            print("this triggers")

        print(c.getButton())
        
import time
import datetime
from PIL import Image, ImageDraw, ImageFont
import c
from threading import Thread

epd = c.epd()
epd.init()
image = c.newImage()
draw = ImageDraw.Draw(image)


# Function to print the date
def date():
    x = datetime.date.today()
    draw.text((111, 5), x.strftime('%m/%d/%Y'), font = c.font24, fill = 0)
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


# Updates the clock to show the time
def clock():
    currentDay = time.localtime()[7]
    while True:
        draw.rectangle((8, 5, 108, 30), fill = 255)
        draw.text((8, 5), time.strftime('%H:%M:%S'), font = c.font24, fill = 0)
        epd.displayPartial(epd.getbuffer(image))

        if currentDay != time.localtime()[7]:
            c.refresh()
            time.sleep(1)
            date()
            print("this triggers")  # for debuging remove later
            currentDay = time.localtime()[7]


# Function to print home for threading
def homePrint():
    global termSignal
    epd.displayPartBaseImage(epd.getbuffer(image))

    date()
    clockThread = Thread(target=clock, daemon=True)
    clockThread.start()
    c.detectPress()
    print("Thread should join")
    clockThread.join(0)
    clockThread._stop()

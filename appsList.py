import c
from PIL import Image, ImageDraw, ImageFont


def appList():
    print("Triggered appList()")


epd = c.epd()
epd.init()
image = c.newImage()
draw = ImageDraw.Draw(image)


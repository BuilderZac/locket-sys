import c
from PIL import Image, ImageDraw, ImageFont


epd = c.epd()
epd.init()
image = c.newImage()
draw = ImageDraw.Draw(image)


appList = {"", "Home", "Pull Github", "Shutdown", ""}


def drawList(index):
    draw.text((80, 5), appList[index - 1], font = c.font24, fill = 0)
    draw.text((100, 5), appList[index], font = c.font24, fill = 0)
    draw.text((120, 5), appList[index + 1], font = c.font24, fill = 0)

def appList():
    index = 1
    drawList(index)
    c.detectPress()
    button = c.getButton()
    match button:
        case 1:
            index+1
        case 2:
            index-1
        case 3:
            print("selected")
    print("Triggered appList()")

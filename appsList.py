import c
from PIL import Image, ImageDraw, ImageFont
import git
import os


epd = c.epd()
epd.init()
image = c.newImage()
draw = ImageDraw.Draw(image)


# List of apps
appListArray = ["", "Home", "Pull Github", "Shutdown", ""]


# Draws the list of items
def drawList(index):
    draw.text((80, 5), (appListArray[index - 1]), font=c.font24, fill=0)
    draw.text((100, 5), ">" + (appListArray[index]) + "<", font=c.font24, fill=0)
    draw.text((120, 5), (appListArray[index + 1]), font=c.font24, fill=0)


# Executes the desired app
def appDeploy(selection):
    if selection == 1:
        pass
    elif selection == 2:
        g = git.cmd.Git(os.getcwd())
        g.pull()
    elif selection == 3:
        os.system("shutdown")
        # might not work due to root


# appLists main function
def appList():
    index = 1
    while True:
        drawList(index)
        c.detectPress()
        button = c.getButton()
        if button == 1:
            index+1
        elif button == 2:
            index-1
        elif button == 3:
            print("Selected")
            appDeploy(index)
            break
    print("Triggered appList()")

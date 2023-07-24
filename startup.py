import time
from PIL import Image,ImageDraw,ImageFont
import c

#try:
epd = c.epd()
epd.init()
epd.Clear(255)
image = c.newImage()
draw = ImageDraw.Draw(image)

draw.text((5,5), 'Happy Testing', font=c.font24, fill=0, align='left')
epd.display(epd.getbuffer(image))

time.sleep(5)

epd.init()
epd.Clear(0xFF)
epd.sleep()
#except:
#    print("Error")
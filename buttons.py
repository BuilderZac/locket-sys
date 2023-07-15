from gpiozero import Button
from time import sleep

def rel(pin):
    while pin.is_pressed:
        sleep(0.01)

up = Button(17)
down = Button(27)
select = Button(22)

def getButton():
    if up.is_pressed:
        rel(up)
        return 1
    if down.is_pressed:
        rel(down)
        print("test down")
        return 2
    if select.is_pressed:
        rel(select)
        print("test down")
        return 3
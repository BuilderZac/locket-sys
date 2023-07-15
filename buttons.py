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
    elif down.is_pressed:
        rel(down)
        return 2
    elif select.is_pressed:
        rel(select)
        return 3
    else:
        return 4
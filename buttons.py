from gpiozero import Button
from time import sleep

def rel(pin):
    while pin.is_pressed:
        sleep(0.01)

up = Button(16)
down = Button(20)
select = Button(21)

def getButton():
    if up.is_pressed:
        rel(up)
        return 1
    if down.is_pressed:
        rel(down)
        return 2
    if select.is_pressed:
        rel(select)
        return 3
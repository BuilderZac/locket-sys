from gpiozero import Button
from time import sleep

up = Button(17)
down = Button(27)
select = Button(22)

def rel(pin):
    while pin.is_pressed:
        sleep(0.05)

while True:
    if up.is_pressed:
        print("up")
        rel(up)
    if down.is_pressed:
        print("down")
        rel(down)
    if select.is_pressed:
        print("select")
        rel(select)


    sleep(0.05)
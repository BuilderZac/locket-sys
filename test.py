from gpiozero import Button
from time import sleep

up = Button(17)
down = Button(27)
select = Button(22)

while True:
    if up.is_pressed:
        print("up")
    if down.is_pressed:
        print("down")
    if select.is_pressed:
        print("select")


    sleep(0.05)
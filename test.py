from buttons import getButton as get
from time import sleep

while True:
    if get() == 1:
        print("it works up")
    if get() == 2:
        print("it works down")
    if get() == 3:
        print("it works select")
    sleep(0.05)
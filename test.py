from buttons import getButton as get
from time import sleep

while True:
    but = get()
    if but == 1:
        print("it works up")
    if but == 2:
        print("it works down")
    if but == 3:
        print("it works select")
    sleep(0.05)
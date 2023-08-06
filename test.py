import time
day = time.localtime()[6]
days = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]
dayString = ""
for i in range(7):
    if i == day:
        days[i] = ">" + days[i] + "< "
    else:
        days[i] = days[i] + " "
    dayString = dayString + days[i]
print(dayString)
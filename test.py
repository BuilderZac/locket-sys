import time
day = time.localtime()[6]
days = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]
for i in range(7):
    if i == day:
        days[i] = ">" + days[i] + "<"
    print(days[i])

#Time bilan ishlash

import time as t

timeNow = t.localtime()

#Hozirgi vaqtni ko'rish dasturi

print(f"Ayni paytdagi soat {timeNow.tm_hour} : {timeNow.tm_min} ga teng")
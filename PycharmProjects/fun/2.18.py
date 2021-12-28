
timeOffset = eval(input("enter time offset:"))



import time

currentTime = time.time ()

totalSeconds = int(currentTime)

currentSecond = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinute = totalMinutes % 60

totalHours = totalMinutes // 60

currentHour = totalHours % 24



print ("The current time is", currentHour + timeOffset, ":", currentMinute, ":", currentSecond,)
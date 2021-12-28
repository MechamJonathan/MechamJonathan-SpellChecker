currentTime = time.time ()

totalSeconds = int(currentTime)

currentSeconds = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinutes = totalMinutes % 60

totalHours = totalMinutes // 6

currentHours = totalHours % 24

print ("the current time is", currentHours, ":" , currentMinutes, ":", currentSeconds, "GMT")
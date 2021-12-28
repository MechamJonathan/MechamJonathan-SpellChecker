import sys
import time

print (sys.argv)

i = 0
for arg in sys.argv:
    print(str(i) + " " + arg)
    i += 1

c = int(sys.argv[1]) + int(sys.argv[2])
print(c)

print(chr(ord("a") + ord("b")))
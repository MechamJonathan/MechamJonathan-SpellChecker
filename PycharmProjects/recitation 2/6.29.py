

def getDigits (number):
    total = 0
    while number != 0:
        total +=(number % 10)
        number = number //10
        print (number)
getDigits(12345)
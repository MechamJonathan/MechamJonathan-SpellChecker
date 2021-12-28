

import time
import random

def main():
    numList = []
    for i in range(1000):
        numList.append(random.randint(0,1000))

    start = time.time()
    selectionSort(numList)
    for num in numList:
        print(num)
    print(time.time() - start)


def selectionSort(inputList):
    for i in range(len(inputList) -1):
        currMinIndex = i

        for j in range(i + 1, len(inputList)):
            if inputList[currMinIndex] > inputList[j]:
                currMinIndex = j

        if currMinIndex != i:
            inputList[i], inputList[currMinIndex] = inputList[currMinIndex], inputList[i]


main()




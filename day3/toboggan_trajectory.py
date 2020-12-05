import sys
import re

def loadInput():    
    with open("input.txt") as f:
        content = f.read().splitlines()
    f.close()
    return content

def partOne(pisteIn):
    tobPointer = 0
    treeCount = 0
    pisteWidth = len(pisteIn[0])

    pisteIn.pop(0)
    for row in pisteIn:
        tobPointer = tobPointer + 3
        if tobPointer >= pisteWidth: tobPointer = tobPointer - pisteWidth
        if row[tobPointer] == "#":
            treeCount = treeCount + 1
    return treeCount

#============================================
# Main Program
#============================================

try:
    piste = loadInput()

    print(f"Part 1 answer = {partOne(piste)}")


except Exception as e:
    print("Aborting..../n", e)

import sys
import re

def loadInput():    
    with open("input.txt") as f:
        content = f.read().splitlines()
    f.close()
    return content

def traversePiste(pisteIn, rightIn, downIn):
    tobPointer = 0
    treeCount = 0
    pisteWidth = len(pisteIn[0])

    for i in range(downIn, len(pisteIn), downIn):
        tobPointer = tobPointer + rightIn
        if tobPointer >= pisteWidth: tobPointer = tobPointer - pisteWidth
        if pisteIn[i][tobPointer] == "#":
            treeCount = treeCount + 1
    return treeCount

#============================================
# Main Program
#============================================

try:
    piste = loadInput()
    print(f"Part 1 = {traversePiste(piste, 3, 1)}")
    print(f"Part 2 = {traversePiste(piste, 1, 1) * traversePiste(piste, 3, 1) * traversePiste(piste, 5, 1) * traversePiste(piste, 7, 1) * traversePiste(piste, 1, 2)}")

except Exception as e:
    print("Aborting..../n", e)

import sys
import re

def loadInput():    
    with open("input.txt") as f:
        content = f.read().splitlines()
    f.close()
    return content

def scanBoardingPasses(bpIn):

    highestSeat = 0
    for bp in bpIn:
        #print(f"BP is {bp}")
        row = getRowOrCol(bp[0:7], 0, 127)
        #print(f"row is {row}")
        col = getRowOrCol(bp[7:], 0, 7)
        #print(f"col is {col}")
        seatId = (row * 8) + col
        #print(f"seatId = {seatId}")
        if seatId > highestSeat: highestSeat = seatId
    return highestSeat 

def getRowOrCol(inCode, inStart, inEnd):
    midPoint = inStart + (((inEnd - inStart) + 1) / 2)
    #print(f"incode = {inCode}  inStart = {inStart} inEnd = {inEnd}  midPoint = {midPoint}")
    if len(inCode) == 1:
        if inCode == 'F' or inCode == 'L': return int(inStart)
        return int(inEnd)
    else:
        if inCode[0] == 'F'  or inCode[0] == 'L': 
            return getRowOrCol(inCode[1:], inStart, midPoint - 1)
        return getRowOrCol(inCode[1:], midPoint, inEnd)

#============================================
# Main Program
#============================================

try:
    boardingPasses = loadInput()

    print(f"Part 1 is {scanBoardingPasses(boardingPasses)}")


except Exception as e:
    print("Aborting..../n", e)

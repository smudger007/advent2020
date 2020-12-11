import sys
import re

def loadInput():    
    with open("input.txt") as f:
        content = f.read().splitlines()
    f.close()
    return content

def getSeatFromBP(bpIn):
    return (getRowOrCol(bpIn[0:7], 0, 127) * 8) + getRowOrCol(bpIn[7:], 0, 7)

def scanBoardingPasses(bpsIn):
    highestSeat = 0
    for bp in bpsIn:
        seatId = getSeatFromBP(bp)
        if seatId > highestSeat: highestSeat = seatId
    return highestSeat 

def getRowOrCol(inCode, inStart, inEnd):
    midPoint = inStart + (((inEnd - inStart) + 1) / 2)
    if len(inCode) == 1:
        if inCode == 'F' or inCode == 'L': return int(inStart)
        return int(inEnd)
    else:
        if inCode[0] == 'F'  or inCode[0] == 'L': 
            return getRowOrCol(inCode[1:], inStart, midPoint - 1)
        return getRowOrCol(inCode[1:], midPoint, inEnd)

def getSeatsOnRowWithEmptySeat(bpIn):
    rowSeats = [[] for i in range(128)]
    for bp in bpIn:
        rowId = getRowOrCol(bp[0:7], 0, 127)
        rowSeats[rowId].append(getSeatFromBP(bp))
    return [x for x in rowSeats if len(x) == 7 ]

#============================================
# Main Program
#============================================

try:
    boardingPasses = loadInput()

    print(f"Part 1 is {scanBoardingPasses(boardingPasses)}")
    print(f"Part 2 is on this row - {getSeatsOnRowWithEmptySeat(boardingPasses)}")

except Exception as e:
    print("Aborting..../n", e)

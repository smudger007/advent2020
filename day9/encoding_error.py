import sys
import re


def loadInput():    
    with open("input.txt") as f:
         allRules = f.read().splitlines()
    f.close()
    return allRules

def initSumPool(poolIn):
    outPool = []
    
    for i in range(len(poolIn) - 1):
        interimPool = []
        for j in range(i + 1, len(poolIn)):
            interimPool.append(int(poolIn[i]) + int(poolIn[j]))
        outPool.append(interimPool)
    return outPool

def valIn2DPool(inPool, val):
    for a in inPool:
        if val in a: return 1
    return 0

def updateSumPool(inSumPool, inPairPool, inSize):
    # Remove values for number removed from pair pool.
    del inSumPool[0]

    # Need to update each sum row; add on new number added to pair pool.
    for i in range(inSize - 2):
        inSumPool[i].append((int(inPairPool[i]) + int(inPairPool[inSize - 1])))
    
    # Don't forget the sum of last two numbers in the pair pool.
    inSumPool.append([int(inPairPool[inSize - 2]) + int(inPairPool[inSize - 1])])


def getFirstBadNum(inputIn, preambleSizeIn):

    pointer = preambleSizeIn    
    sumPool = initSumPool(inputIn[:preambleSizeIn])

    while pointer < len(inputIn):
        
        if valIn2DPool(sumPool, int(inputIn[pointer])):
            # Update the sum pool and continue...
            updateSumPool(sumPool, inputIn[(pointer - (preambleSizeIn - 1)):pointer + 1], preambleSizeIn)
            pointer = pointer + 1
        else:
            # No match, so we have found the issue. Let's return it...
            break
        
    return inputIn[pointer]

#============================================
# Main Program
#============================================

try:
    input = loadInput()
    #print(f"input = {input}\n")
    print(f"Part 1 = {getFirstBadNum(input, 25)}")
    

except Exception as e:
    print("Aborting..../n", e)

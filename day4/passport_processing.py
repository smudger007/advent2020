import sys
import re

def loadInput():    
    with open("input.txt") as f:
        content = f.read().splitlines()
    f.close()
    return content

def processPassportList(listIn):
   
    count = 0
    pairCount = 0
    cidCount = 0
    for entry in listIn:
        
        if entry == "":
            if pairCount == 8 or (pairCount == 7 and cidCount == 0): count = count + 1
            pairCount = 0
            cidCount = 0
        else: 
            pairCount = pairCount + entry.count(':')
            if "cid" in entry: cidCount = 1

    if pairCount == 8 or (pairCount == 7 and cidCount == 0): count = count + 1
            
    
    return count

#============================================
# Main Program
#============================================

try:
    input = loadInput()
    print(f"Part 1 = {processPassportList(input)}")
    
except Exception as e:
    print("Aborting..../n", e)

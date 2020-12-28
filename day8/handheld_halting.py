import sys
import re

def loadInput():    
    with open("input.txt") as f:
         allRules = f.read().splitlines()
    f.close()
    return allRules

def interpreter(inCode):

    codePattern = re.compile("(.*) ([-+])(.*)")
    pointer = 0
    lineCounter = [0] * len(inCode)
    running = 1
    accumulator = 0

    while running:
        if lineCounter[pointer] == 1:
            running = 0
        else:
            lineCounter[pointer] = lineCounter[pointer] + 1
            interpret = codePattern.search(inCode[pointer])            
            if interpret.group(1) == "nop":
                pointer = pointer + 1
            elif interpret.group(1) == "acc":
                if interpret.group(2) == "+":
                    accumulator = accumulator + int(interpret.group(3))
                else:
                    accumulator = accumulator - int(interpret.group(3))
                pointer = pointer + 1
            else:
                # Command must be a JMP
                if interpret.group(2) == "+":
                    pointer = pointer + int(interpret.group(3))
                else:
                    pointer = pointer - int(interpret.group(3))
                
    return accumulator

#============================================
# Main Program
#============================================

try:
    code = loadInput()

    print(f"input = {code}")

    print(f"Part 1 = {interpreter(code)}")

except Exception as e:
    print("Aborting..../n", e)

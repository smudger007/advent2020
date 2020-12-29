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

        if pointer >= len(inCode):
            # Success - we fixed it....
            return (1, accumulator)

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

    # We've hit an infinite loop - let's report back...   
    return (0, accumulator)

def fixCode(inCode):
    accumulator = 0
    codePattern = re.compile("(.*) ([-+])(.*)")

    # Loop through code, changing jmp to nop and vice versa and trying code again. Continue until we fix....
    
    for linePointer, line in enumerate(inCode):
        interpret = codePattern.search(line)
        if interpret.group(1) == "jmp" or interpret.group(1) == "nop":
            if interpret.group(1) == "jmp":
                inCode[linePointer] = "nop " + interpret.group(2) + interpret.group(3)
            else:
                inCode[linePointer] = "jmp " + interpret.group(2) + interpret.group(3)
            
            retry = interpreter(inCode)
            # Did we fix??
            if retry[0] == 1:
                # YES :-)
                accumulator = retry[1]
                break

            inCode[linePointer] = line

    return accumulator

#============================================
# Main Program
#============================================

try:
    code = loadInput()
    #print(f"input = {code}\n")
    print(f"Part 1 = {interpreter(code)[1]}")
    print(f"Part 2 = {fixCode(code)}")

except Exception as e:
    print("Aborting..../n", e)

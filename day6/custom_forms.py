import sys
import re

def loadInput():    
    with open("input.txt") as f:
        content = f.read().split("\n\n")
    f.close()
    return content

def scanForms(formsIn):
    count = 0
    for group in formsIn:
        holdSet = set()
        for char in group.replace("\n", ""): holdSet.add(char)
        count = count + len(holdSet)
    return(count)

def scanFormsPartTwo(formsIn):
    count = 0
    for group in formsIn:
        holdSet = set()
        for form in group.split("\n"):
            toRemove = []
            if len(holdSet) == 0:
                [holdSet.add(char) for char in form]
            else:
                for char in holdSet:
                    if char not in form: toRemove.append(char)
                for char in toRemove: holdSet.remove(char)
                if len(holdSet) == 0: break
        count = count + len(holdSet)
    return(count)

#============================================
# Main Program
#============================================

try:
    customForms = loadInput()
    print(f"Part 1 is {scanForms(customForms)}")
    print(f"Part 2 is {scanFormsPartTwo(customForms)}")

except Exception as e:
    print("Aborting..../n", e)

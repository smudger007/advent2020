import sys
import re

def loadInput():    
    with open("input.txt") as f:
        content = f.read().split("\n\n")
    f.close()
    return content

def scanForms(formIn):
    count = 0
    for form in formIn:
        holdSet = set()
        for char in form.replace("\n", ""): holdSet.add(char)
        count = count + len(holdSet)
    return(count)

#============================================
# Main Program
#============================================

try:
    customForms = loadInput()
    print(f"Part 1 is {scanForms(customForms)}")

except Exception as e:
    print("Aborting..../n", e)

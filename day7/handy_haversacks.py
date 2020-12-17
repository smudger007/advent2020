import sys
import re

def loadInput():    
    with open("input.txt") as f:
         allRules = f.read().splitlines()
    f.close()
    return allRules

def getExternalBagCount(inRules, inBagColour):

    #Turn the rules into a dictionary that shows which external bags a bag type can reside in

    pattern = re.compile("\d+ (.*)bag")
    externalBagDict = {}
    for rule in inRules:
        if "no other bag" in rule: continue
        parts = rule.split(" bags contain ")
        for bag in parts[1].split(","):
            colourSearch = pattern.search(bag)
            colour = colourSearch.group(1).strip()
            if colour in externalBagDict:                
                externalBagDict[colour].append(parts[0])
            else:
                externalBagDict[colour] = [parts[0]]

    # Now search through the rules identifying how many external bags the input bag can reside in.

    currentSearchBag = set([inBagColour])
    nextSearchBag = set()
    externalBags = set()
    while len(currentSearchBag) != 0:
        for bag in currentSearchBag:
            if bag not in externalBagDict: continue
            for externalBag in externalBagDict[bag]:
                externalBags.add(externalBag)
                nextSearchBag.add(externalBag)
        currentSearchBag = nextSearchBag.copy()
        nextSearchBag.clear()

    return len(externalBags)

#============================================
# Main Program
#============================================

try:
    print(f"Part 1 is {getExternalBagCount(loadInput(), 'shiny gold')}")

except Exception as e:
    print("Aborting..../n", e)

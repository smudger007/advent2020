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


def getInternalBagCount(inRules, inBagColour):
    
    # Turn the rules into a dictionary (stored globally), which shows which bags should be inside a bag
    # Global used as we count the bags using recusrion, which would mean potentially passing the dictionary many times, which 
    # is not ideal..

    pattern = re.compile("(\d+) (.*)bag")
    
    for rule in inRules:
        if "no other bag" in rule: continue
        parts = rule.split(" bags contain ")
        internalBagDict[parts[0]] = []
        for bag in parts[1].split(","):
            srch = pattern.search(bag)
            internalBagDict[parts[0]].append((int(srch.group(1).strip()), srch.group(2).strip()))
        
    # Return the count of internal bags 

    return getBagCount(inBagColour)

def getBagCount(inCol):
    if inCol not in internalBagDict:
        return 0
    else:
        directBagCount = 0
        insideBagCount = 0
        for entry in internalBagDict[inCol]:
            insideBagCount = insideBagCount + (entry[0] * getBagCount(entry[1]))
            directBagCount = directBagCount + entry[0]
        return insideBagCount + directBagCount

#============================================
# Main Program
#============================================

try:
    rules = loadInput()
    print(f"Part 1 is {getExternalBagCount(rules, 'shiny gold')} \n")

    internalBagDict = {}

    print(f"Part 2 is {getInternalBagCount(rules, 'shiny gold')}")

except Exception as e:
    print("Aborting..../n", e)

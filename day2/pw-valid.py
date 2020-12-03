import sys
import re

def loadPWFromFile():    
    with open("pw-file.txt") as f:
        content = f.read().splitlines()
    f.close()
    return content

def part1(pwlistIn):
    pattern = re.compile("(\d+)-(\d+) (.): (.+)")
    count = 0

    for pw in passwords:
        result = pattern.search(pw)
        if result.group(4).count(result.group(3)) >= int(result.group(1)) and result.group(4).count(result.group(3)) <= int(result.group(2)):
            count = count + 1
    return count

def part2(pwlistIn):
    pattern = re.compile("(\d+)-(\d+) (.): (.+)")
    count = 0

    for pw in passwords:
        result = pattern.search(pw)
        if (result.group(3) == result.group(4)[int(result.group(1)) - 1]) != (result.group(3) == result.group(4)[int(result.group(2)) - 1]):
            count = count + 1
    return count

#============================================
# Main Program
#============================================

try:
    passwords = loadPWFromFile()

    print(f"part one count is {part1(passwords)}")
    print(f"part two count is {part2(passwords)}")

except Exception as e:
    print("Aborting..../n", e)

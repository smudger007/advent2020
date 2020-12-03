import sys

def loadValuesFromFile():
    
    with open("expense-report.txt") as f:
        content = f.read().splitlines()
    f.close()
    return content

def getTwoExpenseResult(inExpenses):
    for i, valA in enumerate(inExpenses):
        for j in range(i+1, len(inExpenses)):
            if (int(valA) + int(inExpenses[j])) == 2020: return int(valA) * int(inExpenses[j])
    return 0

def getThreeExpenseResult(inExpenses):
    for i, valA in enumerate(inExpenses):
        for j in range(i+1, len(inExpenses)):
            for k in  range(j+1, len(inExpenses)):
                if (int(valA) + int(inExpenses[j]) + int(inExpenses[k])) == 2020: return int(valA) * int(inExpenses[j]) * int(inExpenses[k])
    return 0

#============================================
# Main Program
#============================================

try:
    print(getTwoExpenseResult(loadValuesFromFile()))
    print(getThreeExpenseResult(loadValuesFromFile()))

except Exception as e:
    print("Aborting..../n", e)

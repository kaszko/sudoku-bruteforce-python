import drawer.liner
import drawer.tabler
import digit
import navigator
import pprint

digits = []

lineNum = 0
with open('easy1.txt', 'r') as f:
    for line in f:
        charNum = 0
        digits.append([])
        if (lineNum < 9):
            for readChar in list(line):
                if (charNum < 9):
                    digits[lineNum].append(digit.digit(readChar))
                charNum += 1
            lineNum += 1

myTabler = drawer.tabler.tabler(digits)
myTabler.drawResult()
myTabler.drawDebug()

count = 0
while True:
    changed = False
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            currentDigit = digits[i][j]
            currentAvailableDigits = currentDigit.getAvailableDigits()
            if len(currentAvailableDigits) == 1:
                removeDigitNum = currentAvailableDigits[0]
                currentNavigator = navigator.navigator(i, j)

                for positions in currentNavigator.getAllPositions():
                    currentNavDigit = digits[positions[0]][positions[1]]
                    currentChanged = currentNavDigit.removeAvailableDigit(removeDigitNum)
                    if (currentChanged == True):
                        changed = True

    count += 1
    print count
    myTabler.drawDebug()
    if (changed == False) or (count>1000):
        break

print ""
print "Current result"
myTabler.drawResult()


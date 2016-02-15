import liner
import sys

class tabler:
    def __init__(self, digits):
        self.digits = digits
        self.liner = liner.liner()

    def drawColSeparator(self, colNum):
        if (colNum%3 == 0):
            sys.stdout.write("|")
        else:
            sys.stdout.write(":")

    def drawLineSeparator(self, separatorType, lineNum):
        if (separatorType == 'short'):
            if (lineNum%3 == 2):
                self.liner.drawShortStrongLine()
            else:
                self.liner.drawShortLightLine()
        else:
            if (lineNum%3 == 2):
                self.liner.drawLongStrongLine()
            else:
                self.liner.drawLongLightLine()

    def drawDebug(self):
        self.liner.drawLongStrongLine()
        for (lineNum, digitLine) in enumerate(self.digits):
            for (colNum,digit) in enumerate(digitLine):
                self.drawColSeparator(colNum)
                for i in [1, 2, 3]:
                    sys.stdout.write(digit.getAvailableDigitString(i))
            print "|"
            for (colNum,digit) in enumerate(digitLine):
                self.drawColSeparator(colNum)
                for i in [4, 5, 6]:
                    sys.stdout.write(digit.getAvailableDigitString(i))
            print "|"
            for (colNum,digit) in enumerate(digitLine):
                self.drawColSeparator(colNum)
                for i in [7, 8, 9]:
                    sys.stdout.write(digit.getAvailableDigitString(i))
            print "|"
            self.drawLineSeparator('long', lineNum)

    def drawResult(self):
        self.liner.drawShortStrongLine()
        for (lineNum, digitLine) in enumerate(self.digits):
            for (colNum,digit) in enumerate(digitLine):
                self.drawColSeparator(colNum)
                sys.stdout.write(digit.getFinalValue())
            print "|"
            self.drawLineSeparator('short', lineNum)


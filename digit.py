class digit:

    def __init__(self, initValue):
        if initValue == "x":
            self.availableDigits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.availableDigits = [int(initValue)]

    def getFinalValue(self):
        if len(self.availableDigits) == 1:
            return str(self.availableDigits[0])
        else:
            return " "

    def getAvailableDigitString(self, digitNum):
        if (digitNum in self.availableDigits):
            return str(digitNum)
        else:
            return " "

    def getAvailableDigits(self):
        return self.availableDigits

    def removeAvailableDigit(self, digitNum):
        if (digitNum in self.availableDigits):
            self.availableDigits.remove(digitNum)
            return True
        else:
            return False

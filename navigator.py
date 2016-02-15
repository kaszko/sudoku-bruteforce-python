class navigator:
    def __init__(self, lineNum, colNum):
        self.lineNum = lineNum
        self.colNum = colNum
        self.positions = []

    def addToPositions(self, position):
        if position not in self.positions:
            self.positions.append(position)

    def getAllPositions(self):
        self.getLinePositions()
        self.getColPositions()
        self.getBlockPositions()
        return self.positions

    def getLinePositions(self):
        for i in range(0, 9, 1):
            if (i != self.colNum):
                self.addToPositions([self.lineNum, i])
        return self.positions

    def getColPositions(self):
        digits = []
        for i in range(0, 9, 1):
            if (i != self.lineNum):
                self.addToPositions([i, self.colNum])
        return self.positions

    def getBlockPositions(self):
        digits = []
        startCol = self.colNum - self.colNum % 3
        startLine = self.lineNum - self.lineNum % 3
        for i in range(startLine, startLine+3, 1):
            for j in range(startCol, startCol+3, 1):
                if (i != self.lineNum) or (j != self.colNum):
                    self.addToPositions([i, j])
        return self.positions
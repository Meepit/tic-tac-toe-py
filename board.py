class Board():
    def __init__(self, cellClass, size=3):
        self.cellClass = cellClass
        self.size = size

    def getSize(self):
        return self.size

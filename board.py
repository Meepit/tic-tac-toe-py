class Board():
    def __init__(self, cellClass, size=3):
        self.cellClass = cellClass
        self.size = size
        self._generateBoard()

    def getSize(self):
        return self.size

    def _generateBoard(self):
        self.board = [[self.cellClass() for i in range(self.size)] for i in range(self.size)]

    def get_board(self):
        return self.board

    

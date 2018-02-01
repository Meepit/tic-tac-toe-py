class Board():
    def __init__(self, cell_class, size=3):
        self.cell_class = cell_class
        self.size = size
        self._generateBoard()

    def get_size(self):
        return self.size

    def _generateBoard(self):
        self.board = [[self.cell_class() for i in range(self.size)] for i in range(self.size)]

    def get_board(self):
        return self.board

class Board():
    def __init__(self, cell_class, board_validator, size=3):
        self.cell_class = cell_class
        self.board_validator = board_validator
        self.size = size
        self._generate_board()

    def get_size(self):
        return self.size

    def _generate_board(self):
        self.board = [[self.cell_class() for i in range(self.size)] for i in range(self.size)]

    def get_board(self):
        return self.board

    def get_string_cell_board(self):
        return [[self.board[i][j].get_value() for j in range(3)] for i in range(3)]

    def validate(self):
        self.board_validator.validate()

    def make_move(self, pos, value):
        if self.board[pos[0]][pos[1]].change_value(value):
            return True

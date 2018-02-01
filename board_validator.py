class BoardValidator():
    # Validates 2d array string boards
    def __init__(self, board_state):
        self.board_state = board_state

    def transpose_board(self):
        return [[self.board_state[j][i] for j in range(3)] for i in range(3)]

    def validate_non_diagonals(self):
        # if True then game over
        return True in ["".join(i) == "XXX" or "".join(i) == "OOO" for i in self.board_state + self.transpose_board()]

    def validate_diagonals(self):
        board = self.board_state
        diag_1 = "".join([board[i][i] for i in range(3)])
        diag_2 = "".join([board[2-i][i] for i in range(3)])
        return (diag_1 == "XXX" or diag_2 == "XXX") or (diag_1 == "OOO" or diag_2 == "OOO")

    def validate_stalemate(self):
        board = self.board_state
        return not " " in "".join(["".join(board[i]) for i in range(3)])

    def validate(self):
        # If any of the validate methods are true, game is over
        return not self.validate_non_diagonals() or self.validate_diagonals or self.validate_stalemate

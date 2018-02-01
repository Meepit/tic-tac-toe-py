class BoardValidator():
    def __init__(sef, board_state):
        self.board_state = board_state

    def transpose_board(self):
        return [[self.board_state[j][i] for j in range(3)] for i in range(3)]

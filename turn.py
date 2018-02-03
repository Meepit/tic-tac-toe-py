class Turn():
    def __init__(self, player, board):
        self.player = player
        self.board = board
        self.valid_turn = False

    def get_move(self):
        move, piece = self.player.make_move(), self.player.get_piece()
        if self.board.make_move(move, piece):
            self.valid_turn = True
        else:
            self.valid_turn = False

    def is_valid(self):
        return self.valid_turn

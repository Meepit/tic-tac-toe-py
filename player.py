class Player():
    def __init__(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def make_move(self, move):
        return move
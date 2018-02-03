class Player():
    def __init__(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def make_move(self):
        #Return 2d array of grid position
        user_input = input()
        return [int(user_input[0]), int(user_input[1])]

        return move

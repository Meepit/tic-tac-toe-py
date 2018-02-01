from random import choice

class Game():
    def __init__(self, player_class, turn_class, board):
        self.player_class = player_class
        self.turn_class = turn_class
        self.board = board
        self._generate_players()
        self._get_first()

    def _generate_players(self):
        self.player_1 = self.player_class('X')
        self.player_2 = self.player_class('O')

    def _get_first(self):
        self.next_turn = choice([self.player_1, self.player_2])

    def generate_next_turn(self):
        turn = self.turn_class(self.next_turn, self.board)
        if turn.is_valid():
            self._increment_turn()

    def _increment_turn(self):
        if self.next_turn == self.player_1:
            self.next_turn = self.player_2
        else:
            self.next_turn = self.player_1

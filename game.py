from random import choice

class Game():
    def __init__(self, player_class, turn_class):
        self.player_class = player_class
        self.turn_class = turn_class
        self._generate_players()
        self._get_first()

    def _generate_players(self):
        self.player_1 = self.player_class()
        self.player_2 = self.player_class()

    def _get_first(self):
        self.next_turn = choice([self.player_1, self.player_2])

    def generate_next_turn(self):
        self.turn_class()

import unittest
from unittest import mock
from unittest.mock import MagicMock
import mock

from game import Game

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player_class = mock.MagicMock()
        self.player_1 = mock.Mock()
        self.player_2 = mock.Mock()
        self.board = mock.Mock()
        self.turn_class = mock.Mock()
        self.player_class.side_effect = [self.player_1, self.player_2]

        self.game = Game(self.player_class, self.turn_class, self.board)

    def test_player_creation(self):
        self.assertEqual(self.player_1, self.game.player_1)

    def test_random_first_player(self):
        self.assertTrue(self.game.next_turn in [self.player_1, self.player_2])

    def test_turn_generation(self):
        self.game.generate_next_turn()
        self.turn_class.assert_called()

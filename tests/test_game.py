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
        self.turn_obj = mock.Mock()
        self.turn_class.return_value = self.turn_obj
        self.player_class.side_effect = [self.player_1, self.player_2]

        self.game = Game(self.player_class, self.turn_class, self.board)

    def test_player_creation(self):
        self.assertEqual(self.player_1, self.game.player_1)

    def test_random_first_player(self):
        self.assertTrue(self.game.next_turn in [self.player_1, self.player_2])

    def test_turn_generation(self):
        self.game.generate_next_turn()
        self.turn_class.assert_called()

    def test_successful_turn_increments_turn(self):
        self.game.next_turn = self.player_1
        self.turn_obj.is_valid = MagicMock(return_value= True)
        self.game.generate_next_turn()
        self.assertEqual(self.player_2, self.game.next_turn)

    def test_unsuccessful_turn_no_increment_turn(self):
        self.game.next_turn = self.player_1
        self.turn_obj.is_valid = MagicMock(return_value= False)
        self.game.generate_next_turn()
        self.assertEqual(self.player_1, self.game.next_turn)

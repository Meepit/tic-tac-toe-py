import unittest
from unittest import mock
from unittest.mock import MagicMock
import mock

from turn import Turn

class TurnTest(unittest.TestCase):
    def setUp(self):
        self.player = mock.Mock()
        self.board = mock.Mock()
        self.turn = Turn(self.player, self.board)

    def test_valid_move(self):
        self.player.get_move = MagicMock(return_value = 2)
        self.player.get_piece = MagicMock(return_value = 'X')
        self.board.make_move = MagicMock(return_value = True)
        self.turn.get_move()
        self.assertTrue(self.turn.is_valid())

    def test_invalid_move(self):
        self.player.get_move = MagicMock(return_value = 2)
        self.player.get_piece = MagicMock(return_value = 'X')
        self.board.make_move = MagicMock(return_value = False)
        self.turn.get_move()
        self.assertFalse(self.turn.is_valid())

    def test_invalid_turn_on_initialize(self):
        self.assertFalse(self.turn.is_valid())

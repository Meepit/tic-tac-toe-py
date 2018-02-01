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
        self.turn_class = mock.Mock()
        self.player_class.side_effect = [self.player_1, self.player_2]

        self.game = Game(self.player_class, self.turn_class)

    def test_player_creation(self):
        self.assertEqual(self.player_1, self.game.player_1)

import unittest
from unittest import mock
from unittest.mock import MagicMock
import mock

from player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player('X')

    def test_get_piece(self):
        self.assertEqual('X', self.player.piece)


    def test_make_move(self):
        self.assertEqual([0,0], self.player.make_move([0,0]))

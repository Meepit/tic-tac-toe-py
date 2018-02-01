import unittest
from unittest import mock
from unittest.mock import MagicMock
from pprint import pprint

from board import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.cellClass = mock.Mock()
        self.board = Board(self.cellClass)

    def test_default_size(self):
        self.assertEqual(3, self.board.getSize())

    def test_board_generation(self):
        self.assertEqual(3, len(self.board.board))

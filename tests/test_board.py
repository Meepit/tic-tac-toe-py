import unittest
from unittest import mock
from unittest.mock import MagicMock
from pprint import pprint

from board import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.cell_class = mock.Mock()
        self.board = Board(self.cell_class)

    def test_default_size(self):
        self.assertEqual(3, self.board.get_size())

    def test_board_generation(self):
        self.assertEqual(3, len(self.board.board))

    def test_get_board(self):
        self.assertEqual(3, len(self.board.get_board()))

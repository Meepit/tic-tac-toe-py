import unittest
from unittest import mock
from unittest.mock import MagicMock
from pprint import pprint
import mock

from board import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.cell_class = mock.Mock()
        self.cell_obj = mock.Mock()
        self.cell_obj.get_value = MagicMock(return_value= ' ')
        self.cell_class.return_value = self.cell_obj
        self.board = Board(self.cell_class)

    def test_default_size(self):
        self.assertEqual(3, self.board.get_size())

    def test_board_generation(self):
        self.assertEqual(3, len(self.board.board))

    def test_get_board(self):
        self.assertEqual(3, len(self.board.get_board()))

    def test_get_string_cell_board(self):
        self.assertEqual([[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']], self.board.get_string_cell_board())

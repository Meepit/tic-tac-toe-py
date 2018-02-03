import unittest
from unittest import mock
from unittest.mock import MagicMock
import mock

from board import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.cell_class = mock.Mock()
        self.cell_obj = mock.Mock()
        self.cell_obj.get_value = MagicMock(return_value= ' ')
        self.cell_class.return_value = self.cell_obj
        self.board_validator = MagicMock()
        self.board = Board(self.cell_class, self.board_validator)

    def test_default_size(self):
        self.assertEqual(3, self.board.get_size())

    def test_board_generation(self):
        self.assertEqual(3, len(self.board.board))

    def test_get_board(self):
        self.assertEqual(3, len(self.board.get_board()))

    def test_get_string_cell_board(self):
        self.assertEqual([[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']], self.board.get_string_cell_board())

    def test_validator_is_used(self):
        self.board.validate()
        self.board_validator.validate.assert_called()

    def test_make_move(self):
        self.cell_obj.get_value = MagicMock(return_value= 'X')
        self.board.make_move([0,0], 'X')
        self.assertEqual(self.board.board[0][0].get_value(), 'X')

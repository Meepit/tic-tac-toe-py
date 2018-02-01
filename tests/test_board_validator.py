import unittest
from unittest import mock
from unittest.mock import MagicMock
from board_validator import BoardValidator


class TestBoardValidator(unittest.TestCase):
    def setUp(self):
        self.board_state = mock.Mock()
        self.board_validator = BoardValidator(self.board_state)

    def test_validates_board_transpose(self):
        self.board_validator.board_state = [[0,1,2], [0,1,2], [0,1,2]]
        self.assertEqual(self.board_validator.transpose_board(), [[0,0,0], [1,1,1], [2,2,2]])

    def test_validate_non_diagonal(self):
        board_state = [['X', 'X', 'X'],['X', 'O', 'X'],['O', 'X', 'X']]
        self.board_validator.board_state = board_state
        self.assertTrue(self.board_validator.validate_non_diagonals())

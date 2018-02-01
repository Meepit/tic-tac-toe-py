import unittest
from unittest import mock
from unittest.mock import MagicMock


class TestBoardValidator(unittest.TestCase):
    def setUp(self):
        self.board_class = mock.Mock()
        self.board_validator = BoardValidator()

    def validates_board_transpose(self):
        self.board_class.board_state = [[0,1,2], [0,1,2], [0,1,2]]
        self.assertEqual(self.board_class.transpose_board(), [[0,0,0], [1,1,1], [2,2,2]])

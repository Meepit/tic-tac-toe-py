import unittest
from unittest import mock
from unittest.mock import MagicMock

from board import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.cellClass = mock.Mock()
        self.board = Board(self.cellClass)

    def test_default_size(self):
        self.assertEqual(3, self.board.getSize())

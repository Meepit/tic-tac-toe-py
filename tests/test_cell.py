import unittest
from unittest import mock
from unittest.mock import MagicMock
from cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell = Cell()

    def test_not_available_on_init(self):
        self.assertFalse(self.cell.is_available())

    def test_empty_state_on_init(self):
        self.assertEqual(' ', self.cell.get_value())
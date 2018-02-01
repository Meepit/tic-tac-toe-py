import unittest
from unittest import mock
from unittest.mock import MagicMock
from cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell = Cell()

    def test_not_available_on_init(self):
        self.assertTrue(self.cell.is_available())

    def test_empty_state_on_init(self):
        self.assertEqual(' ', self.cell.get_value())

    def test_change_value(self):
        self.cell.change_value('X')
        self.assertEqual('X', self.cell.get_value())

    def test_cannot_change_value_if_not_available(self):
        self.cell.change_value('X')
        self.cell.change_value('O')
        self.assertEqual('X', self.cell.get_value())

    def test_str(self):
        self.assertEqual(' ', self.cell.__repr__())

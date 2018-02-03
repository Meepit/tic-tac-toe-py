from board import Board
from game import Game
from cell import Cell
from board_validator import BoardValidator
from player import Player
from turn import Turn
from pprint import pprint

board_validator = BoardValidator('')
board = Board(Cell, board_validator)
board_validator.board_state = board.get_string_cell_board()
game = Game(Player, Turn, board)

game.generate_next_turn()
print(board.get_string_cell_board())
game.generate_next_turn()
print(board.get_string_cell_board())
game.generate_next_turn()
print(board.get_string_cell_board())
game.generate_next_turn()
print(board.get_string_cell_board())
game.generate_next_turn()
print(board.get_string_cell_board())
game.generate_next_turn()
print(board.get_string_cell_board())

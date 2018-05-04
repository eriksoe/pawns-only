from Board import *
from Moves import *

board = Board()

print(board.toString())

undo1 = board.move((0,1), (0,6))

print(board.toString())

undo1.undo()

print(board.toString())

moves = generateMoves(board, White)

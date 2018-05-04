from Board import *
from Moves import *

board = Board()

print(board.toString())

undo1 = board.move((0,1), (0,3))
undo2 = board.move((1,6), (1,4))

print(board.toString())

#undo2.undo()
#undo1.undo()

print(board.toString())

moves = generateMoves(board, White)

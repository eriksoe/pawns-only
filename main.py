from Board import *
from Moves import *
import random

board = Board()

print(board.toString())
curPlayer = White
while True:
    moves = generateMoves(board, curPlayer)
    if len(moves) == 0:
        print "Game over!"
        break

    move = random.choice(moves)

    undoHandle = move.apply()
    curPlayer = curPlayer.otherColor

    print(board.toString())
    

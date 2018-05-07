from Board import *
from Moves import *
import random

board = Board()

print(board.toString())
curPlayer = White
while True:
    moves = generateMoves(board, curPlayer)
    if len(moves) == 0:
        print "Game over - tie!"
        break

    move = random.choice(moves)
    move.apply()
    print(board.toString(move.dst))

    isWin = move.dst[1] == curPlayer.goalRow
    if isWin:
        print "Game over - %s won!" % curPlayer.name
        break

    curPlayer = curPlayer.otherColor
    

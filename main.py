#!/usr/bin/env python2.7
from Board import *
from Moves import *
from Game import *
from Player import HumanPlayer, RandomPlayer
from AIPlayer import AIPlayer
import random
import sys

#player1 = HumanPlayer()
#player2 = AIPlayer()
#
#game = Game(player1, player2)
#winner = game.play()
#print "Winner: %s" % (winner,)

player1 = AIPlayer()
player2 = RandomPlayer()

def tournament(n, player1, player2):
    wons = [0,0,0]
    for i in xrange(n):
        game = Game(player1, player2, quiet=True)
        (winner, winColor) = game.play()
        wons[winColor.flavourNr] += 1
        if i%10==9: sys.stderr.write('.')
    print(wons)
    return wons


#ai = AIPlayer()
#tournament(400, ai, RandomPlayer())
#tournament(400, RandomPlayer(), ai)

wwins = []
bwins = []
n = 100
for i in xrange(10):
    ai = AIPlayer()
    r = tournament(n, ai, RandomPlayer())
    wwins.append(r[White.flavourNr])
    r = tournament(n, RandomPlayer(), ai)
    bwins.append(r[Black.flavourNr])
    print("")
#tournament(50, AIPlayer(), RandomPlayer())
#tournament(50, RandomPlayer(), AIPlayer())

print("White wins: %s (of %s)" % (wwins, n))
print("Black wins: %s (of %s)" % (bwins, n))

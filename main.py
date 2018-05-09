from Board import *
from Moves import *
from Game import *
from Player import HumanPlayer, RandomPlayer
from AIPlayer import AIPlayer
import random

player1 = HumanPlayer()
player2 = AIPlayer()

game = Game(player1, player2)
winner = game.play()
print "Winner: %s" % (winner,)

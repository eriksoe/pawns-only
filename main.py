from Board import *
from Moves import *
from Game import *
from Player import *
import random

game = Game(RandomPlayer(), RandomPlayer())
winner = game.play()
print "Winner: %s" % (winner,)

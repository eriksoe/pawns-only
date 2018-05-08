import Moves
import random

class Player:
    def __init__(self):
        self.color = None

    def setColor(self, color):
        self.color = color
        
    # Abstract methods:
    # selectMove(board)

class RandomPlayer(Player):
    def __init__(self):
        pass#self.Player.__init()#(self)
        
    def selectMove(self, board):
        validMoves = Moves.generateMoves(board, self.color)
        return random.choice(validMoves)


class HumanPlayer(Player):
    def __init__(self):
        pass#Player(self)
        
        
    def selectMove(self, board):
        validMoves = Moves.generateMoves(board, self.color)
        print(validMoves) # TODO
        


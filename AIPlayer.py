from Player import Player
from Board import White
import Moves

class BrainBase:
    def boardToFeatures(self, board):
        size = 3*8*8 + 1
        acc = [0] * size
        for y in xrange(8):
            for x in xrange(8):
                idx = (y*8+x) * 3
                cell = board.cell(x, y)
                acc[idx + cell.flavourNr] = 1
        acc[3*8*8] = board.curColor.flavourNr - White.flavourNr
        return acc

        
class Brain1(BrainBase):
    pass
        
class AIPlayer(Player):
    def __init__(self):
        self.brain = Brain1()
        
    def selectMove(self, board):
        v = self.brain.boardToFeatures(board)
        print "Features: %s" % (v,)
        
        validMoves = Moves.generateMoves(board, self.color)
        return validMoves[0] # TODO

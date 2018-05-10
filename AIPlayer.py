from Player import Player
from Board import White
import Moves

import math
import numpy as np
import numpy.random as npr
import theano as t
import theano.tensor as tt
from theano.tensor.nnet.nnet import sigmoid

class BrainBase:
    inputVectorSize = 3*8*8 + 1
    def boardToInputVector(self, board):
        acc = [0] * BrainBase.inputVectorSize
        for y in xrange(8):
            for x in xrange(8):
                idx = (y*8+x) * 3
                cell = board.cell(x, y)
                acc[idx + cell.flavourNr] = 1
        acc[3*8*8] = board.curColor.flavourNr - White.flavourNr
        return acc

        
class Brain1(BrainBase):
    """Architecture:
    Input vector -> 64 hidden -> 1 valuation
    """
    def __init__(self):
        inSize = BrainBase.inputVectorSize
        h1Size = 64
        self.vIn = vIn = tt.dvector('in')
        self.vM1 = vM1 = tt.dmatrix('m1')
        self.vM2 = vM2 = tt.dvector('m2')
        self.vW1 = vW1 = tt.dvector('w1')
        self.vW2 = vW2 = tt.dscalar('w2')
        vH1 = sigmoid(tt.dot(vIn, vM1) + vW1)
        self.vOut = vOut = sigmoid(tt.dot(vH1, vM2) + vW2)
        t.pp(vOut)
        self.evalFun = t.function([vIn, vW1, vM1, vW2, vM2], vOut)

        self.m1 = 1/math.sqrt(inSize) * npr.standard_normal( (inSize, h1Size) )
        self.m2 = 1/math.sqrt(h1Size) * npr.standard_normal( (h1Size,) )

        self.w1 = 1/math.sqrt(inSize) * npr.standard_normal( (h1Size,) )
        self.w2 = 1/math.sqrt(h1Size) * npr.standard_normal( )

    def evaluate(self, board):
        inputVector0 = self.boardToInputVector(board)
        inputVector = np.array(inputVector0, dtype=np.float64)

        #rint "Args: %s" % ( [inputVector, self.m1, self.m2], )
        out = self.evalFun(inputVector, self.w1, self.m1, self.w2, self.m2)
        return out

        
class AIPlayer(Player):
    def __init__(self):
        self.brain = Brain1()
        
    def selectMove(self, board):        
        factor = 1 if self.color == White else -1

        v0 = self.brain.evaluate(board)
        #print "Valuation: %s" % v0
        
        validMoves = Moves.generateMoves(board, self.color)
        (bestMove, bestScore) = (None, -100 * factor)

        for move in validMoves:
            undoHandle = move.apply()
            score = self.brain.evaluate(board)
            undoHandle.undo()

            c = " "
            if score * factor > bestScore * factor:
                (bestMove, bestScore) = (move, score)
                c = "*"
            #print "  %c %s: %5.3f" % (c, move, score)
        
        return bestMove

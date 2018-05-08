import Moves
import random
import sys
import re

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
        while True:
            sys.stderr.write("Your move> ")
            #sys.stderr.flush()
            line = sys.stdin.readline()
            move = self.parseMove(line, board)
            if move in validMoves:
                return move
            else:
                sys.stderr.write("Invalid move :-(\n")

    def parseMove(self, line, board):
        m = re.match("^\\s*([a-h])([1-8])\\s*-\\s*([a-h])([1-8])\\s*$",
                     line)
        if m==None:
            return None

        def col(s): return ord(s)-ord("a")
        def row(s): return ord(s)-ord("1")
        src = (col(m.group(1)), row(m.group(2)))
        dst = (col(m.group(3)), row(m.group(4)))
        return Moves.Move(board, src, dst)
    
    



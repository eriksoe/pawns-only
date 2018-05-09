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
            elif move != None: # Incomplete move - try to complete it:
                candidates = [m for m in validMoves
                              if self.moveMatches(move, m)]
                if len(candidates) == 1:
                    return candidates[0]
                else:
                    sys.stderr.write("Ambiguous move\n")
            else:
                sys.stderr.write("Invalid move :-(\n")

    def moveMatches(self, cand, move):
        def m(a,b): return a==b or a==-1
        return (m(cand.src[0], move.src[0]) and
                m(cand.src[1], move.src[1]) and
                m(cand.dst[0], move.dst[0]) and
                m(cand.dst[1], move.dst[1]))
        

    def parseMove(self, line, board):
        def col(s): return ord(s)-ord("a")
        def row(s): return ord(s)-ord("1")

        m = re.match("^\\s*([a-h])([1-8])\\s*-\\s*([a-h])([1-8])\\s*$", line)
        if m!=None:
            src = (col(m.group(1)), row(m.group(2)))
            dst = (col(m.group(3)), row(m.group(4)))
            return Moves.Move(board, src, dst)

        m = re.match("^\\s*([a-h])([1-8])\\s*$", line)
        if m!=None:
            src = (-1,-1)
            dst = (col(m.group(1)), row(m.group(2)))
            return Moves.Move(board, src, dst)
        
        return None
    



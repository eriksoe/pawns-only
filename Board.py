# -*- encoding: utf-8 -*-
#export Board

class Cell:
    def __init__(self): pass
    # To implement: toString(); isEmpty()

    def hasColor(self, color):
        return self.__class__ == color
    
class EmptyCell(Cell):
    def toString(self, x, y): return "⧠ " if ((x+y)%2)==0 else "▨ "
    def isEmpty(self): return True

class White(Cell):
    def toString(self, x, y): return "♙ "
    def isEmpty(self): return False

class Black(Cell):
    def toString(self, x, y): return "♟ "
    def isEmpty(self): return False

White.otherColor = Black
Black.otherColor = White
    
def empty_row(): return 8 * [EmptyCell()]
def black_row(): return 8 * [Black()]
def white_row(): return 8 * [White()]

# BLACK CHESS PAWN (♟)
# WHITE CHESS PAWN (♙)

# SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL (▨)
# SQUARE WITH CONTOURED OUTLINE (⧠)
sqr1 = "▨"

ansiNormal = "\x1b[0m"
ansiBold = "\x1b[1m"
ansiColor = "\x1b[1;102m"
#ansiColor = "\x1b[1;36m"
ansiColorNormal = "\x1b[00m"

class Board:
    
    def __init__(self):
        self.b = [
            empty_row(),
            white_row(),
            empty_row(),
            empty_row(),
            empty_row(),
            empty_row(),
            black_row(),
            empty_row()
            ]
        
    def toString(self, emphPos=None):
        s = ""
        (ex,ey) = emphPos if emphPos != None else (-1,-1)
    
        rows = list(self.b)
        for y0 in xrange(8):
            y = 7 - y0
            row  = rows[y]
            line = ""
            for x in xrange(8):
                c = row[x]
                if (x,y) == emphPos: line += ansiColor
                line += c.toString(x, y)
                if (x,y) == emphPos: line += ansiNormal
            s += line + "\n"
        return s

    "Cell access:"
    def cell(self, x, y):
        return self.b[y][x]

    def withinBounds(self, x, y):
        return x>=0 and y>=0 and x<8 and y<8
                
    "Moving:"
    def move(self, src, dst):
        (sx,sy) = src
        (dx,dy) = dst
        old = self.b[dy][dx]
        self.b[dy][dx] = self.b[sy][sx]
        self.b[sy][sx] = EmptyCell()
        return Undoing(self, src, dst, old)

    def replaceCell(self, dst, oldCell):
        (dx,dy) = dst
        self.b[dy][dx] = oldCell        

class Undoing:
    def __init__(self, board, src, dst, oldCell):
        self.board = board
        self.src = src
        self.dst = dst
        self.oldCell = oldCell

    def undo(self):
        self.board.move(self.dst, self.src) # Move back
        self.board.replaceCell(self.dst, self.oldCell)

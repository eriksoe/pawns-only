# -*- encoding: utf-8 -*-
#export Board

ansiNormal = "\x1b[0m"
ansiBold = "\x1b[1m"
ansiTargetColor = "\x1b[1;102m" # Green
ansiIntermedColor = "\x1b[1;103m" # Yellow
#ansiColor = "\x1b[1;36m"
ansiColorNormal = "\x1b[00m"
ansiWhite = "\x1b[37m"
ansiBlack = "\x1b[30m"

#ansiWhiteBG = "\x1b[107;30m"
ansiBlackBG = "\x1b[40;97m"
ansiWhiteBG = "\x1b[48;5;231;30m"
ansiBlackBG = "\x1b[40;38;5;231m"

unfilledPiece = "♙ "
filledPiece = "♟ "

class Cell:
    def __init__(self): pass
    # To implement: toString(); isEmpty()
    # Color properties: name; homeRow; goalRow; playDirection

    def hasColor(self, color):
        return self.__class__ == color

    def _isBlackSquare(self, x, y):
        return (x+y)%2 == 0
    def _paintSqr(self, x, y, sw, sb):
#        if self._isBlackSquare(x,y):
        return (ansiBlackBG+sb if self._isBlackSquare(x, y) else ansiWhiteBG+sw)+ ansiNormal
        
    
class EmptyCell(Cell):
#    def toString(self, x, y): return "⧠ " if ((x+y)%2)==0 else "▨ "
    def toString(self, x, y):
        return self._paintSqr(x, y, "  ", "  ")
#        return (ansiBlack if self._isBlackSquare(x, y) else ansiWhite)+ "██" + ansiNormal
    def isEmpty(self): return True

class White(Cell):
    def toString(self, x, y):
        return self._paintSqr(x, y, unfilledPiece, filledPiece)
        #return "♙ "
    def isEmpty(self): return False

    name = "White"
    playDirection = 1
    homeRow = 1
    goalRow = 7

class Black(Cell):
    def toString(self, x, y):
        #return "♟ "
        return self._paintSqr(x, y, filledPiece, unfilledPiece)
    def isEmpty(self): return False

    name = "Black"
    playDirection = -1
    homeRow = 6
    goalRow = 0

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
        
    def toString(self, emphMove=None):
        s = ""
    
        rows = list(self.b)
        for y0 in xrange(8):
            y = 7 - y0
            row  = rows[y]
            line = ""
            for x in xrange(8):
                c = row[x]
                emph = self.calcEmph((x, y), emphMove)
                if emph != None: line += emph[0]
                line += c.toString(x, y)
                if emph != None: line += emph[1]
            s += line + "\n"
        return s

    def calcEmph(self, pos, emphMove):
        if emphMove == None:
            return None
        if pos == emphMove.dst:
            return (ansiTargetColor, ansiNormal)
        if pos == emphMove.src:
            return (ansiIntermedColor, ansiNormal)
        if pos in emphMove.intermediate:
            return (ansiIntermedColor, ansiNormal)
        return None

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

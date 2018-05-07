from Board import White, Black

class Move:
    def __init__(self, board, src, dst):
        self.board = board
        self.src = src
        self.dst = dst

    def apply(self):
        self.board.move(self.src, self.dst)

    def __str__(self):
        (sx,sy) = self.src
        (dx,dy) = self.dst
        return "(%d,%d)->(%d,%d)" % (sx, sy, dx, dy)

    def __repr__(self):
        (sx,sy) = self.src
        (dx,dy) = self.dst
        return "(%d,%d)->(%d,%d)" % (sx, sy, dx, dy)

print(Move(None, (1,2), (3,4)))


def generateMoves(board, color):
    moves = []
    for y in xrange(0,8):
        for x in xrange(0,8):
            src = (x,y)
            cell = board.cell(x, y)
            if not cell.hasColor(color): continue

            deltaY = color.playDirection
            homeY = color.homeRow

            y2 = y + deltaY
            if board.withinBounds(x,y2) and board.cell(x,y2).isEmpty():
                moves.append(Move(board, src, (x,y2)))

                # Also try two ahead - but only if one ahead is possible:
                y2 = y + 2*deltaY
                if y==homeY and board.withinBounds(x,y2) and board.cell(x,y2).isEmpty():
                    moves.append(Move(board, src, (x,y2)))

            # Try to take opponent's piece:
            y2 = y + deltaY
            x2 = x - 1
            if board.withinBounds(x2,y2) and board.cell(x2,y2).hasColor(color.otherColor):
                moves.append(Move(board, src, (x2,y2)))
            x2 = x + 1
            if board.withinBounds(x2,y2) and board.cell(x2,y2).hasColor(color.otherColor):
                moves.append(Move(board, src, (x2,y2)))


    return moves
                          
            


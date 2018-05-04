class Move:
    def __init__(self, board, src, dst):
        self.board = board
        self.src = src
        self.dst = dst

    def apply(self):
        self.board.move(self.src, self.dst)


def generateMoves(board, color):
    moves = []
    for y in xrange(0,8):
        for x in xrange(0,8):
            cell = board.cell(x, y)
            if not cell.hasColor(color): continue
            print cell
            


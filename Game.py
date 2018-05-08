from Board import *
from Moves import *

class Game:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

    def play(self):
        board = Board()

        (p1,p2) = (self.player1, self.player2)
        p1.setColor(White)
        p2.setColor(Black)
        
        print(board.toString())

        players = [(p1, White), (p2, Black)]
        turn = 0
        while True:
            turn += 1
            (curPlayer, curColor) = players[turn % 2]
            
            moves = generateMoves(board, curColor)
            if len(moves) == 0:
                print "Game over - tie!"
                winner = None
                break

            move = curPlayer.selectMove(board)
            if move not in moves:
                errmsg = "Invalid move! %s by %s (%s)" % (move, curColor.name, curPlayer)
                print("** "+errmsg)
                print("** Valid moves: %s" % (moves,))
                raise Error(errmsg)
            
            move.apply()
            print(board.toString(move))
        
            isWin = move.dst[1] == curColor.goalRow
            if isWin:
                print "Game over - %s (%s) won!" % (curColor.name, curPlayer)
                winner = (curPlayer, curColor)
                break
        
        return winner
    

from Board import *
from Moves import *

class Game:
    def __init__(self, p1, p2, quiet=False):
        self.player1 = p1
        self.player2 = p2
        self.quiet = quiet

    def playerForColor(self, color):
        return self.player1 if color == White else self.player2

    def say(self, msg):
        if not self.quiet: print(msg)
    
    def play(self):
        board = Board()

        (p1,p2) = (self.player1, self.player2)
        p1.setColor(White)
        p2.setColor(Black)
        
        if not self.quiet: print(board.toString())

        #players = [(p1, White), (p2, Black)]
        #turn = 0
        while True:
            #(curPlayer, curColor) = players[turn % 2]
            #turn += 1
            curColor = board.curColor
            curPlayer = self.playerForColor(curColor)

            moves = generateMoves(board, curColor)
            if len(moves) == 0:
                self.say("Game over - tie!")
                winner = (None, EmptyCell)
                break

            oldTurns = board.turns
            move = curPlayer.selectMove(board)
            if move not in moves:
                errmsg = "Invalid move! %s by %s (%s)" % (move, curColor.name, curPlayer)
                print("** "+errmsg)
                print("** Valid moves: %s" % (moves,))
                raise Exception(errmsg)
            if board.turns != oldTurns:
                errmsg = "Player cheated!? (color=%s, move=%s, turns=%d/%d)" % (curColor.name, move, oldTurns, board.turns)
                print("** "+errmsg)
                raise Exception(errmsg)

            self.say("%s's move: %s" % (curColor.name, move))
            move.apply()
            if not self.quiet: print(board.toString(move))
        
            isWin = move.dst[1] == curColor.goalRow
            if isWin:
                self.say("Game over - %s (%s) won!" % (curColor.name, curPlayer))
                winner = (curPlayer, curColor)
                break
        
        return winner
    

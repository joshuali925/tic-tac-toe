import sys
class tic_tac_toe(object):
    def __init__(self):
        self.board = [0] * 9
        self.pattern = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                        (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.player = True  # X moves first, 1=X, 2=O

    def printboard(self, board=None):
        def getchar(n):
            if n == 0: return ' '
            if n == 1: return 'X'
            if n == 2: return 'O'

        if not board: board = self.board
        for i in range(3):
            for j in range(3):
                print(getchar(board[i * 3 + j]), end='|')
            print()
        print('===========')

    def eval(self, board=None):
        if not board: board = self.board
        for x, y, z in self.pattern:
            if 0 != board[x] == board[y] == board[z]:
                return 1 if board[x] == 1 else -1
        return 0

    def terminal(self, board=None):
        if not board: board = self.board
        return 0 not in board or self.eval(board) != 0

    def alphabeta(self, board=None, player=None, alpha=-99999, beta=99999):
        if not board: board = self.board
        if player is None: player = self.player

        if self.terminal(board):
            return self.eval(board), None
        if player:
            best = -99999, None
            for empty in range(9):
                if board[empty] != 0: continue
                board[empty] = 1
                v, _ = self.alphabeta(board, False, alpha, beta)
                board[empty] = 0
                if v > best[0]: best = v, empty
                if best[0] >= beta: return best
                alpha = max(alpha, best[0])
        else:
            best = 99999, None
            for empty in range(9):
                if board[empty] != 0: continue
                board[empty] = 2
                v, _ = self.alphabeta(board, True, alpha, beta)
                board[empty] = 0
                if v < best[0]: best = v, empty
                if best[0] <= alpha: return best
                beta = min(beta, best[0])
        return best

    def start(self, ai_move=False):
        board = self.board
        if not ai_move: self.printboard()
        while True:
            if ai_move: _, x = self.alphabeta()
            else: x = int(input('Position: ')) - 1
            if not (0 <= x <= 8 and board[x] == 0):
                print('Invalid')
                continue
            board[x] = 1 if self.player else 2
            self.printboard()
            if self.terminal(): break
            self.player, ai_move = not self.player, not ai_move
        if self.eval() == 0: print('Tie')
        elif self.player: print('X wins')
        else: print('O wins')


game = tic_tac_toe()
if len(sys.argv) == 1: game.start()
else: game.start(True)

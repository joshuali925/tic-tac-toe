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
        if sum(board) == 0: return None, 0  # if empty, place on upper left corner

        if self.terminal(board):
            return self.eval(board), None
        move = -1
        if player:
            best = -99999
            for empty in range(9):
                if board[empty] != 0: continue
                board[empty] = 1
                v, _ = self.alphabeta(board, False, alpha, beta)
                board[empty] = 0
                if v > best:
                    best = v
                    move = empty
                if best >= beta:
                    return best, move
                alpha = max(alpha, best)
        else:
            best = 99999
            for empty in range(9):
                if board[empty] != 0: continue
                board[empty] = 2
                v, _ = self.alphabeta(board, True, alpha, beta)
                board[empty] = 0
                if v < best:
                    best = v
                    move = empty
                if best <= alpha:
                    return best, move
                beta = min(beta, best)
        return best, move

    def start(self, ai_move=False):
        board = self.board
        if not ai_move: self.printboard()
        while True:
            if ai_move: _, x = self.alphabeta()
            else: x = int(input('Position: ')) - 1
            if x > 8 or x < 0 or board[x] != 0:
                print('Invalid')
                continue
            board[x] = 1 if self.player else 2
            self.printboard()
            print('===========')
            if self.terminal():
                if self.eval() == 0: print('Tie')
                elif self.player: print('X wins')
                else: print('O wins')
                return
            self.player = not self.player
            ai_move = not ai_move


game = tic_tac_toe()
game.start()

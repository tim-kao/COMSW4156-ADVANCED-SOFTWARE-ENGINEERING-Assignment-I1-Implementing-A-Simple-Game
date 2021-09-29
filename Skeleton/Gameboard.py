class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.rows = rows = 6
        self.cols = cols = 7
        self.board = [['' for x in range(cols)] for y in range(rows)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.emptyRowAtCol = [self.rows - 1] * cols
        self.remain = rows * cols

    def judge(self, r, c) -> bool:
        if not self.isReady():
            return False
        left = right = c
        board = self.board
        player = board[r][c]
        # horizontal
        while left - 1 >= 0 and board[r][left - 1] == player:
            left -= 1
        while right + 1 < self.cols and board[r][right + 1] == player:
            right += 1
        if right - left >= 3:
            return True
        # vertical
        down = r
        while down + 1 < self.rows and board[down + 1][c] == player:
            down += 1
        if down - r >= 3:
            return True
        # diagonal, left-down
        left, down = c, r
        while left - 1 >= 0 and down + 1 < self.rows and \
                board[down + 1][left - 1] == player:
            left -= 1
            down += 1
        if down - r >= 3:
            return True
        # diagonal, right-down
        right, down = c, r
        while right + 1 < self.cols and down + 1 < self.rows and \
                board[down + 1][right + 1] == player:
            right += 1
            down += 1
        return down - r >= 3

    def isReady(self) -> tuple[bool, str]:
        lis = ['red', 'yellow']
        return self.player1 in lis and self.player2 in lis and\
            self.player1 != self.player2

    def isFinish(self) -> bool:
        return self.game_result != ""

    def switch(self):
        self.current_turn = 'p1' if self.current_turn == 'p2' else 'p2'

    def draw(self):
        self.game_result = 'Tie'

    def move(self, col, player) -> tuple[bool, str]:
        row = self.emptyRowAtCol[col]
        if row == -1:
            return False, 'No space left at this column'
        elif self.isFinish():
            return False, 'Game over'
        elif player != self.current_turn:
            return False, 'Not your turn'
        self.remain -= 1
        self.emptyRowAtCol[col] -= 1  # decrease row
        if self.current_turn == 'p1':
            self.board[row][col] = self.player1
        else:
            self.board[row][col] = self.player2
        if self.judge(row, col):
            if self.current_turn == 'p1':
                self.game_result = 'player1'
            else:
                self.game_result = 'player2'
        if self.remain == 0:
            self.draw()
        self.switch()
        return True, ''

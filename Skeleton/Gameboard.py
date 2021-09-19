import db

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


    def judge(self, r, c) -> bool: # check if anyone wins
        left = right = c
        board = self.board
        player = board[r][c]
        while left - 1 >= 0 and board[r][left - 1] == player:
            left -= 1
        while right + 1 < self.cols and board[r][right + 1] == player:
            right += 1
        if right - left >= 3:
            return True
        up = down = r
        while up - 1 >= 0 and board[up - 1][c] == player:
            up -= 1
        while down + 1 < self.rows and board[down + 1][c] == player:
            down += 1
        return down - up >= 3

    def isReady(self) -> bool:
        return (self.player1 and self.player2), 'Color not selected'

    def isFinish(self) -> bool:
        return self.game_result != ""


    def switch(self) -> bool:
        self.current_turn = 'p1' if self.current_turn == 'p2' else  'p2'


    def move(self, col, player) -> tuple[bool, str]:
        row = self.emptyRowAtCol[col]
        if row == -1:
            return False, 'No space left at this column'
        if self.isFinish():
            return False, 'Game over'
        if player != self.current_turn:
            return False, 'Not your turn'
        self.emptyRowAtCol[col] -= 1 # decrease row
        self.board[row][col] = self.player1 if self.current_turn == 'p1' else self.player2
        if self.judge(row, col):
            self.game_result = 'player1' if self.current_turn == 'p1' else 'player2'
        self.switch()
        return True, ''


'''
Add Helper functions as needed to handle moves and update board and turns
'''


    

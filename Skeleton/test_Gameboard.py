import unittest
from Gameboard import Gameboard


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Gameboard()

    def test_init_judge(self):
        # Check game initialization edge condition: move before picking colors
        self.assertEqual(self.game.judge(0, 0), False)

    def test_init_ready(self):
        # Check game initialization edge condition: readiness if not pick color
        self.assertEqual(self.game.isReady(), False)

    def test_ready(self):
        # Check game initialization edge condition after picking color
        self.game.player1, self.game.player2 = 'red', 'yellow'
        self.assertEqual(self.game.isReady(), True)

    def test_init_isFinish(self):
        # Check game initialization if game is finih or not
        self.assertEqual(self.game.isFinish(), False)

    def test_switch(self):
        # Check taking turns functionality
        self.assertEqual(self.game.current_turn, 'p1')
        self.game.switch()
        self.assertEqual(self.game.current_turn, 'p2')
        self.game.switch()
        self.assertEqual(self.game.current_turn, 'p1')

    def test_draw(self):
        # Check game result after draw game
        self.game.draw()
        self.assertEqual(self.game.game_result, 'Tie')

    def test_init_move(self):
        # Invalid move - not current player's turn
        self.assertEqual(self.game.move(0, 'p2'), (False, 'Not your turn'))

    def test_game_start(self):
        self.game.player1, self.game.player2 = 'red', 'yellow'
        self.assertEqual(self.game.move(0, 'p1'), (True, ''))

    def test_game_col_full(self):
        # Invalid move - current column is filled
        self.game.player1, self.game.player2 = 'red', 'yellow'
        for i in range(self.game.cols):
            if i % 2:
                self.game.move(0, 'p1')
            else:
                self.game.move(0, 'p2')
        res = (False, 'No space left at this column')
        self.assertEqual(self.game.move(0, 'p1'), res)

    def test_game_p1_win(self):
        # Happy path for correct move
        # Happy path for winning move in each of vertical
        # Invalid move - winner already declared in the end
        self.game.player1, self.game.player2 = 'red', 'yellow'
        t = (True, '')
        for i in range(7):
            if i % 2 == 0:
                self.assertEqual(self.game.move(0, 'p1'), t)
            else:
                self.assertEqual(self.game.move(1, 'p2'), t)
        self.assertEqual(self.game.game_result, 'player1')
        self.assertEqual(self.game.isFinish(), True)
        self.assertEqual(self.game.move(0, 'p1'), (False, 'Game over'))

    def test_game_p2_win(self):
        # Happy path for correct move
        # Happy path for winning move in each of horizontal
        # Invalid move - winner already declared in the end
        self.game.player1, self.game.player2 = 'red', 'yellow'
        t = (True, '')
        for i in range(8):
            if i % 2 == 0:
                self.assertEqual(self.game.move((6 + i // 2) % 7, 'p1'), t)
            else:
                self.assertEqual(self.game.move(i // 2, 'p2'), t)
        self.assertEqual(self.game.game_result, 'player2')
        self.assertEqual(self.game.isFinish(), True)

    def test_game_p2_win2(self):
        self.game.player1, self.game.player2 = 'red', 'yellow'
        t = (True, '')
        for i in range(8):
            if i % 2 == 0:
                self.assertEqual(self.game.move((0 - i // 2) % 7, 'p1'), t)
            else:
                self.assertEqual(self.game.move(6 - i // 2, 'p2'), t)
        self.assertEqual(self.game.isFinish(), True)

    def test_game_diagonal_pos(self):
        # Happy path for winning move in each of diagonal positive slope
        self.game.player1, self.game.player2 = 'red', 'yellow'
        t = (True, '')
        for i, c in enumerate([0, 1, 2, 2, 2, 3, 3, 3, 3, 5, 1]):
            if i % 2 == 0:
                self.assertEqual(self.game.move(c, 'p1'), t)
            else:
                self.assertEqual(self.game.move(c, 'p2'), t)
        self.assertEqual(self.game.game_result, 'player1')
        self.assertEqual(self.game.isFinish(), True)

    def test_game_diagonal_neg(self):
        # Happy path for winning move in each of diagonal negative slope
        self.game.player1, self.game.player2 = 'red', 'yellow'
        t = (True, '')
        cols = self.game.cols
        for i in range(22):
            if i % 2 == 0:
                self.assertEqual(self.game.move((6 - i) % cols, 'p1'), t)
            else:
                self.assertEqual(self.game.move((6 - i) % cols, 'p2'), t)
        self.assertEqual(self.game.game_result, 'player2')
        self.assertEqual(self.game.isFinish(), True)

    def test_game_draw(self):
        # Invalid move - draw (tie)
        self.game.player1, self.game.player2 = 'red', 'yellow'
        t = (True, '')
        rows, cols = self.game.rows, self.game.cols
        for i in range(rows * cols - 1):
            idx = (i // 4) * 2
            if i % 2 == 0:
                self.assertEqual(self.game.move(idx % cols, 'p1'), t)
            else:
                self.assertEqual(self.game.move((idx + 1) % cols, 'p2'), t)
        self.assertEqual(self.game.move(6, 'p2'), t)
        self.assertEqual(self.game.game_result, 'Tie')
        self.assertEqual(
            self.game.move(0, 'p1'), (False, 'No space left at this column'))
        self.assertEqual(self.game.isFinish(), True)


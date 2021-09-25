import unittest
from Gameboard import Gameboard


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Gameboard()

    def test_init_judge(self):
        self.assertEqual(self.game.judge(0, 0), False)

    def test_init_ready(self):
        self.assertEqual(self.game.isReady(), False)

    def test_ready(self):
        self.game.player1, self.game.player2 = 'red', 'yellow'
        self.assertEqual(self.game.isReady(), True)

    def test_init_isFinish(self):
        self.assertEqual(self.game.isFinish(), False)

    def test_switch(self):
        self.assertEqual(self.game.current_turn, 'p1')
        self.game.switch()
        self.assertEqual(self.game.current_turn, 'p2')
        self.game.switch()
        self.assertEqual(self.game.current_turn, 'p1')

    def test_draw(self):
        self.game.draw()
        self.assertEqual(self.game.game_result, 'Tie')

    def test_init_move(self):
        self.assertEqual(self.game.move(0, 'p2'), (False, 'Not your turn'))

    def test_game_start(self):
        self.game.player1, self.game.player2 = 'red', 'yellow'
        self.assertEqual(self.game.move(0, 'p1'), (True, ''))

    def test_game_col_full(self):
        self.game.player1, self.game.player2 = 'red', 'yellow'
        for i in range(self.game.cols):
            if i % 2:
                self.game.move(0, 'p1')
            else:
                self.game.move(0, 'p2')
        res = (False, 'No space left at this column')
        self.assertEqual(self.game.move(0, 'p1'), res)

    def test_game_p1_win(self):
        self.game.player1, self.game.player2 = 'red', 'yellow'
        t = (True, '')
        for i in range(7):
            if i % 2 == 0:
                self.assertEqual(self.game.move(0, 'p1'), t)
            else:
                self.assertEqual(self.game.move(1, 'p2'), t)
        self.assertEqual(self.game.isFinish(), True)
        self.assertEqual(self.game.move(0, 'p1'), (False, 'Game over'))

    def test_game_p2_win(self):
        self.game.player1, self.game.player2 = 'red', 'yellow'
        t = (True, '')
        for i in range(8):
            if i % 2 == 0:
                self.assertEqual(self.game.move((6 + i // 2) % 7, 'p1'), t)
            else:
                self.assertEqual(self.game.move(i // 2, 'p2'), t)
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

    def test_game_draw(self):
        self.game.player1, self.game.player2 = 'red', 'yellow'
        t = (True, '')
        for i in range(self.game.cols * self.game.rows):
            if i % 2 == 0:
                self.assertEqual(self.game.move(i % self.game.cols, 'p1'), t)
            else:
                self.assertEqual(self.game.move(i % self.game.cols, 'p2'), t)
        self.assertEqual(self.game.isFinish(), True)


if __name__ == '__main__':
    unittest.main()

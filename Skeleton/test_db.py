import unittest
import db
import sqlite3


class TestStringMethods(unittest.TestCase):

    def test_init(self):
        db.clear()
        db.init_db()
        cur = sqlite3.connect('sqlite_db').cursor()
        self.assertEqual(cur.execute("SELECT * FROM GAME").fetchall(), [])

    def test_getNone(self):
        db.clear()
        self.assertEqual(db.getMove(), None)

    def test_addMove(self):
        db.clear()
        db.init_db()
        board = [[''] * 7 for _ in range(6)]
        board[5][0] = 'red'
        board[5][1] = 'yellow'
        move = tuple(['p1'] + board + ['', 'red', 'yellow', 40])
        db.add_move(move)
        row = db.getMove()
        current_turn, board, game_result, player1, \
            player2, remain = row[0], list(row[1:7]), \
            row[7], row[8], row[9], int(row[10])
        self.assertEqual(current_turn, 'p1')
        self.assertEqual(game_result, '')
        self.assertEqual(player1, 'red')
        self.assertEqual(player2, 'yellow')
        self.assertEqual(remain, 40)
        for i in range(5):
            self.assertEqual(board[i], [''] * 7)
        self.assertEqual(board[-1], ['red', 'yellow'] + [''] * 5)

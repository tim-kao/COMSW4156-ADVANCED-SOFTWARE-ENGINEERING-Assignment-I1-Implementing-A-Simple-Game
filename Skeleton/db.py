import sqlite3
from sqlite3 import Error

'''
Initializes the Table GAME
Do not modify
'''


def init_db():
    # creates Table
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute('CREATE TABLE GAME(current_turn TEXT, board TEXT,' +
                     'winner TEXT, player1 TEXT, player2 TEXT' +
                     ', remaining_moves INT)')
        print('Database Online, table created')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


'''
move is a tuple (current_turn, board, winner, player1, player2,
remaining_moves)
Insert Tuple into table
'''


def add_move(move):  # will take in a tuple
    # Insert a row of data
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        cur = conn.cursor()
        rows = cur.execute("SELECT * FROM GAME").fetchall()
        # encode board into string with size of 42
        boardstr = ''
        for r in move[1:7]:
            for cell in r:
                boardstr += '0' if not cell else cell[0]
        cmd = "UPDATE GAME SET current_turn='" + move[0] + "', board='" + \
            boardstr + "', winner='" + move[7] + "', player1='" + move[8] + \
            "', player2='" + move[9] + "', remaining_moves=" + str(move[10]) \
            + ";"
        if not rows:  # no data available, do insertion
            cmd = "INSERT INTO GAME (current_turn, board, winner, player1, \
                    player2, remaining_moves) VALUES ('" + move[0] + "','" +\
                     boardstr + "','" + move[7] + "','" + move[8] + "','" +\
                     move[9] + "'," + str(move[10]) + ")"
        print(cmd)
        cur.execute(cmd)
        conn.commit()
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


'''
Get the last move played
return (current_turn, board, winner, player1, player2, remaining_moves)
'''


def getMove():
    # will return tuple(current_turn, board, winner, player1, player2,
    # remaining_moves) or None if db fails\
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        cur = conn.cursor()
        rows = cur.execute("SELECT * from GAME").fetchall()
        if not rows:
            return None
        board = [[''] * 7 for _ in range(6)]
        current_turn, boardstr, winner, player1, player2, remain = rows[0]
        for i, cell in enumerate(boardstr):
            if cell != '0':  # not None
                board[i // 7][i % 7] = 'yellow' if cell == 'y' else 'red'
        res = tuple([current_turn] + board + [winner,
                    player1, player2, remain])
        return res
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


'''
Clears the Table GAME
Do not modify
'''


def clear():
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute("DROP TABLE GAME")
        print('Database Cleared')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()

import sqlite3

DATABASE_NAME = "books.sqlite"

def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute('select * from books')
        for row in cur.fetchall():
            # print(row)
            print(dict(row))
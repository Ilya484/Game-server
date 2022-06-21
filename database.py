import sqlite3

db = sqlite3.connect('users.db')
cursor = db.cursor()


def try_create():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        nickname TEXT,
                        login TEXT,
                        password TEXT
                        )''')
    db.commit()
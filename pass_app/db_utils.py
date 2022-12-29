import sqlite3


def get_connection():
    conn = sqlite3.connect('lombard.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_all_items():
    conn = get_connection()
    c = conn.cursor()

    result = c.execute('SELECT * FROM "items"')
    return result.fetchall()

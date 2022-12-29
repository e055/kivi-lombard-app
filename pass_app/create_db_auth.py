import sqlite3

def create_db():

    conn = sqlite3.connect('lombard.db')

    c = conn.cursor()

    query = """
    CREATE TABLE "users" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "username"	TEXT,
        "password"	TEXT
    );
    """

    c.execute(query)

    conn.commit()
    conn.close()

create_db()
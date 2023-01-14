import sqlite3


def create_db_users():
    conn = sqlite3.connect('lombard.db')

    c = conn.cursor()

    query = """
    CREATE TABLE "users" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "username"	TEXT,
        "password"	TEXT,
        "email" TEXT,
        "tel" INTEGER,
        "nip" INTEGER
    );
    """

    c.execute(query)

    conn.commit()
    conn.close()




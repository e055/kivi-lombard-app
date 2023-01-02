import sqlite3


def create_db_items():
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    CREATE TABLE "items" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "item_name"	TEXT,
        "item_sn" TEXT,
        "take_price" REAL,
        "redemp_price" REAL,
        "date_in"	TEXT,
        "date_out"	TEXT,
        "owner"	INTEGER,
    );
    """
    c.execute(query)
    conn.commit()
    conn.close()


def create_db_lombard_items():
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    CREATE TABLE "lombard_items" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "item_name"	TEXT,
        "item_sn" TEXT,
        "take_price" REAL,
        "sugest_price" REAL,
        "date_in"	TEXT,
        "date_out"	TEXT,
        "owner" TEXT
    );
    """
    c.execute(query)
    conn.commit()
    conn.close()

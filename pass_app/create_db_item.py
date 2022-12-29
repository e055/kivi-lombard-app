import sqlite3


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
    "ownership" INTEGER
);
"""

c.execute(query)

conn.commit()
conn.close()

# owner ship w create table wartości 0 i 1. 0 jeśli przedmiot
# jeszcze nie przeszedł na własność lombardu.
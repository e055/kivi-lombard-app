import sqlite3
from werkzeug.security import generate_password_hash


def create_db():
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    CREATE TABLE "people" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "name"	TEXT,
        "surname"	TEXT,
        "pesel"	TEXT,
        "adres"	TEXT,
        "e-mail" TEXT,
        "tel" INTEGER
    );
    """
    c.execute(query)
    conn.commit()
    conn.close()


def create_db_seeler():
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    CREATE TABLE "seeler" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "name"	TEXT,
        "surname"	TEXT,
        "pesel"	TEXT,
        "e-mail" TEXT,
        "tel" INTEGER
    );
    """
    c.execute(query)
    conn.commit()
    conn.close()

# zmienic na pliki sql^


def create_user():
    password = '123'
    hashed_password = generate_password_hash(password)
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    INSERT INTO "users" VALUES (NULL, '123', ?)
    """
    c.execute(query, (hashed_password,))
    conn.commit()
    conn.close()




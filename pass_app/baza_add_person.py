import sqlite3


def create_person(name, surname, pesel, adres, email, phone):
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    INSERT INTO "people" VALUES (NULL, ?, ?, ?, ?, ?,? )
    """
    c.execute(query, (name, surname, pesel, adres, email, phone))
    conn.commit()
    conn.close()


def create_seeler(name, surname, pesel, email, phone):
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    INSERT INTO "seeler" VALUES (NULL, ?, ?, ?, ?, ? )
    """
    c.execute(query, (name, surname, pesel, email, phone))
    conn.commit()
    conn.close()

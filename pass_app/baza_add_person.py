import sqlite3
from baza_add_item import create_item


# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`
def create_person(name, surname, pesel, adres, email, phone):
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    INSERT INTO "people" VALUES (NULL, ?, ?, ?, ?, ?,? )
    """
    c.execute(query, (name, surname, pesel, adres, email, phone))
    conn.commit()
    conn.close()




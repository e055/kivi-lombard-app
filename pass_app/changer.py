import sqlite3
from datetime import date


def item_changer(a, b):
    # a = nowa kwota przedmiotu domyslnie powinno byc zero, wykupujac przedmiot placi sie calość b = id produktu
    conn = sqlite3.connect('lombard.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    query = """
    UPDATE items
    SET redemp_price = ?
    WHERE id = ?;
    """
    c.execute(query, (a, b))
    conn.commit()
    conn.close()


def date_item_changer(a, b):
    conn = sqlite3.connect('lombard.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    query = """
    UPDATE items
    SET date_out = ?
    WHERE id = ?;
    """
    c.execute(query, (a, b))
    conn.commit()
    conn.close()


def people_changer():
    conn = sqlite3.connect('lombard.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    query = """
        UPDATE people
    SET surname = 'DupaDupa'
    WHERE pesel = '88';
        """
    c.execute(query)
    conn.commit()
    conn.close()


def lombard_item_changer(id_a, value):
    id = id_a
    conn = sqlite3.connect('lombard.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    query = """
        UPDATE lombard_items
        SET sugest_price = ?,
       date_out = ?     
        WHERE id = ?;
        """
    c.execute(query, (value, date.today(), id))
    conn.commit()
    conn.close()

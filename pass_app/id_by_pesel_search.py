import sqlite3


# person_pesel = 90020945832 do testow

def id_search(person_pesel):
    person_pesel = int(person_pesel)
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    print(person_pesel)
    query = """
    SELECT * FROM "people" 
    WHERE "pesel" == ? ;
    """
    pesel = f'{person_pesel}'
    c.execute(query, (pesel,))
    items = c.fetchone()

    conn.close()
    return items[0]


def id_seeler_search(person_pesel):
    person_pesel = int(person_pesel)
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    print(person_pesel)
    query = """
    SELECT * FROM "seeler" 
    WHERE "pesel" == ? ;
    """
    pesel = f'{person_pesel}'
    c.execute(query, (pesel,))
    items = c.fetchone()

    conn.close()
    return items[0]

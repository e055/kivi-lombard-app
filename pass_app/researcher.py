import sqlite3


# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`

def researcher(z):
    id = z
    conn = sqlite3.connect('lombard.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    query = """
    SELECT * 
    FROM "items"
    WHERE ? = "items"."owner";
    """
    b = c.execute(query, (id,))

    return b.fetchall()



def client_by_pesel_search(person_pesel):
    person_pesel = person_pesel
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    print('jestem w funkcji client by pesel search')
    print(person_pesel)
    query = """
    SELECT * FROM "people" 
    WHERE "pesel" == ? ;
    """
    pesel = f'{person_pesel}'
    c.execute(query, (pesel,))
    items = c.fetchone()
    conn.close()
    item = {'id': items[0],
            'name': items[1],
            'surname': items[2],
            'pesel': items[3],
            'adres': items[4],
            'email': items[5],
            'tel': items[6]
            }
    return item


def client_by_id_search(person_id):
    person_pesel = int(person_id)
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    print(person_pesel)
    query = """
    SELECT * FROM "people" 
    WHERE "id" == ? ;
    """
    id = f'{person_id}'
    c.execute(query, (id,))
    items = c.fetchone()
    conn.close()
    item = {'id': items[0],
            'name': items[1],
            'surname': items[2],
            'pesel': items[3],
            'adres': items[4],
            'email': items[5],
            'tel': items[6]
            }
    return item

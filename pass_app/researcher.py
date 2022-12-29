import sqlite3

# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_init.py`
def researcher(z):
    id=z
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()

    query = """
    SELECT * 
    FROM "items"
    WHERE ? = "items"."owner";
    """

    b = c.execute(query, (id,))
    b = b.fetchall()
    # print(b)
    # for line in b:
    #     print(line)
    #
    conn.close()

    return b

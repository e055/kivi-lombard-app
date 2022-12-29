import sqlite3
from calc_and_date import date_count


# do poprawnego działania należy najpierw mieć bazę stworzoną za pomocą skryptu `baza_drop_and_create.py`
def create_item(item_name, take_price, item_sn, redemp_price, date_in, days, owner, ownership):
    d = date_in
    date_out = date_count(d, days)

    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    INSERT INTO "items" ("item_name", "take_price", "item_sn", "redemp_price", "date_in", "date_out", "owner", "ownership")
    VALUES (:item_name, :take_price, :item_sn,:redemp_price, :date_in, :date_out, :owner, :ownership);
    """
    item = {'item_name': item_name, "take_price": take_price, "item_sn": item_sn, "redemp_price": redemp_price,
            "date_in": date_in, "date_out": date_out,
            "owner": owner, "ownership": ownership}
    c.execute(query, item)
    conn.commit()
    conn.close()
    print(item)

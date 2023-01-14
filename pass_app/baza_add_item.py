import sqlite3
from calc_and_date import date_count


def create_item(item_name, take_price, item_sn, redemp_price, date_in, days, owner):
    d = date_in
    date_out = date_count(d, days)

    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    query = """
    INSERT INTO "items" ("item_name", "take_price", "item_sn", "redemp_price", "date_in", "date_out", "owner")
    VALUES (:item_name, :take_price, :item_sn,:redemp_price, :date_in, :date_out, :owner);
    """
    item = {'item_name': item_name, "take_price": take_price, "item_sn": item_sn, "redemp_price": redemp_price,
            "date_in": date_in, "date_out": date_out, "owner": owner}
    c.execute(query, item)
    conn.commit()
    conn.close()



def create_lombard_item(item_name, take_price, item_sn, sugest_price, date_in, owner):
    conn = sqlite3.connect('lombard.db')
    c = conn.cursor()
    x = "0"
    query = """
        INSERT INTO "lombard_items" ("item_name", "take_price", "item_sn", "sugest_price", "date_in","date_out", "owner")
        VALUES (:item_name, :take_price, :item_sn,:sugest_price, :date_in,:date_out,  :owner);
        """
    item = {'item_name': item_name, "take_price": take_price, "item_sn": item_sn, "sugest_price": sugest_price,
            "date_in": date_in, "date_out": x, "owner": owner}
    c.execute(query, item)
    conn.commit()
    conn.close()


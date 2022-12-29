import datetime
from calc_and_date import date_count
from calc_settings import compound_interest_yearly
from calc_settings import compound_interest_comission


def items_count(item_nam, val_i, dni):
    items = []
    values = 0
    item_id = 1
    item_name = item_nam
    val = val_i
    data_time = datetime.date.today()
    d = str(data_time)
    data, p = date_count(d, dni)
    val_comp_yearly = compound_interest_yearly(val, p)
    val_comp_commision = compound_interest_comission(val, p)
    val = val + round(val_comp_yearly, 2) + round(val_comp_commision, 2)
    val = val + 15  # 15 to kwota prowizji za sporzadzenie umowy
    values += val
    values = round(values, 2)
    item = {"item_id": item_id, "item_name": item_name, "val": round(val, 2), "data": data}
    items.append(item)

    return values, items


def create_person(n, s, a, i, t, item_nam, val_i, dni):
    name = n
    surname = s
    adress = a
    id_p = int(i)
    tel = t
    values, items = items_count(item_nam, val_i, dni)
    item_name = items
    sum_all = values
    person = {"name": name, "surname": surname, "adress": adress, "id": id_p, "tel": tel, "items": item_name,
              "sum": sum_all}
    return person

import datetime
from calc_and_date import date_count
from calc_settings import compound_interest_yearly
from calc_settings import compound_interest_comission


def items_count():
    items = []
    values = 0
    item_id = 1
    while True:
        a = input("Wprowadź przedmiot - wciśnij Enter, wpisz N aby przerwać: ")
        if a == "":
            item_name = input("Nazwa zastawianego przedmiotu: ")
            val = int(input("Podaj kwotę zastawu: "))
            data_time = datetime.date.today()
            d = str(data_time)
            print(data_time)
            print(d)
            data, p = date_count(d)
            val_comp_yearly = compound_interest_yearly(val, p)
            val_comp_commision = compound_interest_comission(val, p)
            val = val + round(val_comp_yearly, 2) + round(val_comp_commision, 2)
            print("Dodano prowizję w wysokości 15 PLN za sporządzenie dokumentacji pożyczki")
            val = val + 15
            values += val
            item = {"item_id": item_id, "item_name": item_name, "val": val, "data": data}
            items.append(item)
            item_id += 1
        else:
            break

    return values, items


def create_person2():
    name = input("Podaj imie : ")
    surname = input("Podaj nazwisko : ")
    adress = input("podaj adres : ")
    id_p = int(input("Numer dowodu: "))
    tel = int(input("Wprowadź numer telefonu: "))
    values, items = items_count()
    item_name = items
    sum_all = values

    person = {"name": name, "surname": surname, "adress": adress, "id": id_p, "tel": tel, "items": item_name,
              "sum": sum_all}
    return person

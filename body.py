import datetime
import json
import random
from create_person import create_person

people = []
lombard_items = []
id_counter = []
sold_items = []

def people_counter():
    ik = 0
    for i in people:
        ik += 1
    return ik


def people_cash_counter():
    kz = 0
    for person in people:
        kz += person["sum"]
    return kz

def read_sold_items():
    with open(f"x_plik_glowny.json", "r") as fh:
        deserialized_people = json.load(fh)
        sold_items.__iadd__(deserialized_people)

def read():
    with open(f"x_plik_glowny.json", "r") as fh:
        deserialized_people = json.load(fh)
        people.__iadd__(deserialized_people)
    with open(f"x_lombard_items.json", "r") as fh:
        deserialized_items = json.load(fh)
        lombard_items.__iadd__(deserialized_items)


def ad_person(n, s, a, i, t, item_nam, val_i, dni):
    person = create_person(n, s, a, i, t, item_nam, val_i, dni)
    people.append(person)

def print_people():
    people_list = ""
    l = 1
    for person in people:
        t = f" \n{l}. {person['name']} {person['surname']} \n {person['adress']} \n pesel: {person['id']} \n tel: {person['tel']} \n" \
            f"Kwota pożyczki: {person['sum']}\n\n"
        people_list += t
        l += 1
    return people_list


def print_lombard_items():
    items_list = ""
    for item in lombard_items:
        t = f"\n ID: {item['item_id']}\nNazwa: {item['item']}\nKwota pozyskania: {item['item_price']} PLN\n" \
            f"{item['take_date']}\n"
        items_list += t
    return items_list

def search(p):
    field = 'id'
    fraze = p
    results = []
    for person in people:
        if person[field] == fraze:
            results.append(person)
    if len(results) == 0:
        results = 0
    else:
        pass
    return results

def search_one_item(a):
    id = a
    results=[]
    for item in lombard_items:
        if item['item_id'] == id:
            results.append(item)
    return results

def payment(t, id_p, kwota):
    results = t
    id_ch = results[0]["id"]
    for person in people:
        if person["id"] == id_ch:
            nr = int(id_p)
            for item in person["items"]:
                if item["item_id"] == nr:
                    a = float(kwota)
                    item["val"] = item["val"] - a
                    person["sum"] = person["sum"] - a
                    c = f'Wpłacono {a} PLN za przedmiot:\n\n' \
                        f'{item["item_name"]}\n' \
                        f'Pozostało: {item["val"]} PLN\n' \
                        f'Pozostało łącznie: {person["sum"]} PLN'
                    return c


def check_sum():
    b = 0
    for person in people:
        if person["sum"] == 0:
            print(person, "\nUsunąć osobę ?")
            a = input("Y/N: ")
            if a == "Y" or "y":
                del people[b]
            else:
                break
        b += 1
    print("Brak osob z zerowym stanem zadluzenia ")


def lomb_item_counter():
    a = random.randint(101, 999)
    id_counter_list()
    while True:
        try:
            result = id_counter.index(a)
            if result >= 0:
                lomb_item_counter()
        except ValueError:
            return a


def new_item_id():
    c = lomb_item_counter()
    return c


def id_counter_list():
    for id_item in lombard_items:
        id_counter.append(int(id_item['item_id']))


def helper():
    a = lomb_item_counter()
    print(a)

def printlog(message, n):
    with open(f'./{n}.txt','a') as f: f.write(message+"\n")


def check_items():
    c1 = 0
    for person in people:
        c2 = 0
        for item in person['items']:
            d_str = item['data']
            d = datetime.datetime.strptime(d_str, "%Y-%m-%d")
            data_time = datetime.date.today()
            dd = str(data_time)
            d2_str = str(datetime.date.today())
            d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d")
            d3 = (d - d2)
            d4 = d3.days
            if d4 < 0:
                new_id = lomb_item_counter()
                item['item_id'] = new_id
                item_change = {"item_id": new_id, "name": person['name'], "surname": person['surname'],
                               "adress": person['adress'], "id": person['id'],
                               "tel": person['tel'], "item": item["item_name"], "item_price": item['val'], "take_date": dd}
                lombard_items.append(item_change)
                person['sum'] = person['sum'] - item['val']
                del people[c1]['items'][c2]
                continue
            else:
                pass
            c2 += 1
        c1 += 1


def create_item_buy(n, s, a, i, t, item_nam, val_i):
    new_id = new_item_id()
    name = n
    surname = s
    adress = a
    id_p = int(i)
    tel = t
    data_time = datetime.date.today()
    d = str(data_time)
    item = item_nam
    item_price = val_i
    item = {"item_id": new_id, "name": name, "surname": surname, "adress": adress, "id": id_p,
            "tel": tel, "item": item, "item_price": item_price, "take_date": d}
    lombard_items.append(item)

def sold_item(b, val):
    id = b
    item_val = val
    data_time = datetime.date.today()
    d = str(data_time)
    counter = 0
    for item in lombard_items:
        if item['item_id'] == id:
            c = [item['item'], item["item_price"], item_val, d]
            sold_items.append(c)
            del lombard_items[counter]
            print(sold_items)
            print(lombard_items)
            write_sold_items_json()
            read_sold_items()
            write_json()
        counter += 1

def write_sold_items_json():
    serialized_items = json.dumps(sold_items)
    with open(f"x_sold_items.json", "w") as fh:
        fh.write(serialized_items)


def write_json():
    serialized_people = json.dumps(people)
    serialized_items = json.dumps(lombard_items)
    with open(f"x_plik_glowny.json", "w") as fh:
        fh.write(serialized_people)
    with open(f"x_lombard_items.json", "w") as fh:
        fh.write(serialized_items)

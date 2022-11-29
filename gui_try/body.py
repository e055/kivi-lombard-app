import datetime
import json
import random
import yaml
from create_person import create_person2

people = []
lombard_items = []
id_counter = []


def ad_person():
    person = create_person2()
    people.append(person)


def print_people():
    for person in people:
        print(
            f" \n {person['name']} {person['surname']} \n "
            f" {person['id']} \n tel: {person['tel']} \n kwota zastawów : {person['sum']} PLN \n")
        print("Zastawione przedmioty: ")
        print_items(person)


def print_items(person):
    # for person in self.people:
    for item in person["items"]:
        print(f"{item['item_id']}. Nazwa: {item['item_name']} - kwota: {item['val']} PLN")


def print_lombard_items():
    for item in lombard_items:
        print(f"ID: {item['item_id']} \n Nazwa: {item['item_name']} \n Kwota pozyskanie {item['val']} PLN")


def search():
    field = input("Pole wyszukiwania: ").lower()
    fraze = input("Fraza (name,surname etc.): ")
    results = []
    for person in people:
        if str(person[field]) == fraze:
            results.append(person)
            print(
                f"{results[0]['name']} {results[0]['surname']} \n Kwota zadłużenia: {results[0]['sum']} PLN")
            y = input("Wiecej informacji y/n ? ")
            if y == "y":
                print(
                    f"{results[0]['name']} {results[0]['surname']} \n {results[0]['id']} \n "
                    f"tel: {results[0]['tel']} \n adres: {results[0]['adress']} kwota : {results[0]['sum']} PLN \n")
                print_items(person)
            else:
                break
        else:
            if results != 0:
                continue
            else:
                print("Brak osoby w bazie")
    return results


def payment():
    results = search()
    id_ch = results[0]["id"]
    print(f" Numer pesel: {id_ch}")
    for person in people:
        # print(person["id"])
        if person["id"] == id_ch:
            print_items(person)
            print(f"Kwota zadluzenia : {person['sum']}")
            nr = int(input("Podaj numer przedmiotu: "))
            for item in person["items"]:
                if item["item_id"] == nr:
                    a = int(input("Kwota wpłaty : "))
                    item["val"] = item["val"] - a
                    person["sum"] = person["sum"] - a
                    print(f" Pozostało:{item['item_name']} {item['val']}")


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
    while True:
        try:
            result = id_counter.index(a)
            if result >= 0:
                lomb_item_counter()
        except ValueError:
            return a


def id_counter_list():
    for id_item in lombard_items:
        id_counter.append(int(id_item['item_id']))


def helper():
    a = lomb_item_counter()
    print(a)


def check_items():
    c1 = 0
    for person in people:
        c2 = 0
        for item in person['items']:
            d_str = item['data']
            d = datetime.datetime.strptime(d_str, "%Y-%m-%d")
            d2_str = str(datetime.date.today())
            d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d")
            d3 = (d - d2)
            d4 = d3.days
            if d4 < 0:
                new_id = lomb_item_counter()
                item['item_id'] = new_id
                lombard_items.append(item)
                person['sum'] = person['sum'] - item['val']
                print(f"Przedmiot: \n {item['item_name']} wartość: {item['val']} PLN \n "
                      f"przechodzi na własność lombardu")
                del people[c1]['items'][c2]
                continue
            else:
                pass
            c2 += 1
        c1 += 1


def read():
    print("Wybierz format odczytu json/yaml")
    choose = input("--> :")
    if choose == "json":
        read_json()
    elif choose == "yaml":
        read_yaml()
    else:
        print("Coś poszło nie tak...")
    print("Plik wczytany prawidłowo !")
    return people, lombard_items


def write():
    print("Wybierz format zapisu json/yaml")
    choose = input("--> :")
    if choose == "json":
        write_json()
    elif choose == "yaml":
        write_yaml()
    else:
        print("Coś poszło nie tak...")
    print("Plik zapisany prawidłowo !")


def read_json():
    p = input("Podaj nazwę istniejacej bazy: ")
    with open(f"{p}_plik_glowny.json", "r") as fh:
        deserialized_people = json.load(fh)
        people = deserialized_people
    with open(f"{p}_lombard_items.json", "r") as fh:
        deserialized_items = json.load(fh)
        lombard_items = deserialized_items
    return people, lombard_items


def checkerr():
    id_counter_list()
    check_sum()
    check_items()


def read_yaml():
    p = input("Podaj nazwę istniejacej bazy: ")
    with open(f"{p}_plik_glowny.yml", "r") as fh:
        deserialized_people = yaml.load(fh, Loader=yaml.FullLoader)
        people = deserialized_people
    with open(f"{p}_lombard_items.yml", "r") as fh:
        deserialized_items = yaml.load(fh, Loader=yaml.FullLoader)
        lombard_items = deserialized_items
    id_counter_list()
    check_sum()
    check_items()
    return people, lombard_items


def write_json():
    p = input("Podaj nazwę istniejacej bazy jesli chcesz nadpisac bądź utworz nową: ")
    serialized_people = json.dumps(people)
    serialized_items = json.dumps(lombard_items)
    with open(f"{p}_plik_glowny.json", "w") as fh:
        fh.write(serialized_people)
    with open(f"{p}_lombard_items.json", "w") as fh:
        fh.write(serialized_items)


def write_yaml():
    p = input("Podaj nazwę istniejacej bazy jesli chcesz nadpisac bądź utworz nową: ")
    serialized_people = yaml.dump(people)
    serialized_items = yaml.dump(lombard_items)
    with open(f"{p}_plik_glowny.yml", "w") as fh:
        fh.write(serialized_people)
    with open(f"{p}_lombard_items.yml", "w") as fh:
        fh.write(serialized_items)


def run(cmdd):
    while True:
        cmd = cmdd
        if cmd == "add":
            ad_person()
        elif cmd == "list":
            print_people()
        elif cmd == "search":
            search()
        elif cmd == "read":
            read()
            checkerr()
        elif cmd == "write":
            write()
        elif cmd == "che":
            check_items()
        elif cmd == "hh":
            helper()
        elif cmd == "pay":
            payment()
        elif cmd == "lomb":
            print_lombard_items()
        elif cmd == "new":
            print("do uzupelnienia")
        elif cmd == "quit":
            a = input("Niezapisane dane zostaną utracone, zapisać ? t/n :")
            if a == "t":
                write()
            else:
                print("end")
                exit(0)
            print("end")
            exit(0)
        else:
            print("No such command. Type again!")

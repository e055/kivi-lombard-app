from datetime import date
import requests
from db_utils import get_all_items

def date_count(d):
    date_r = date.fromisoformat(d)
    today = date.today()
    val = date_r - today
    val = str(val).split(' ', 1)
    val = int(val[0])
    return val

def three_days_checker():
    l = []
    a = get_all_items()
    for i in a:
        if date_count(i[6]) < 3:
            l.append(i)
    return l


def lombard_gold_price(a):
    a = float(a)
    b = a*0.3
    a = a - b
    return a

def gold_checker():
    headers = {'Accept': 'application/json'}
    response = requests.get('http://api.nbp.pl/api/cenyzlota', headers=headers)
    a = response.json()
    nbp_price = a[0]['cena']
    lombard_price = lombard_gold_price(nbp_price)
    return nbp_price , lombard_price



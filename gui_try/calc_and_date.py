import datetime


def date_count(d):
    data = datetime.datetime.strptime(d, "%Y-%m-%d")
    p = redline_date()
    td = datetime.timedelta(p)
    data_l = data + td
    data_l = str(data_l)
    data_str = ""
    for i in range(10):
        data_str += data_l[i]
    return data_str , p


def redline_date():
    print("Wybierz długość zastawu")
    a = int(input("Wybierz 7, 14, 31 dni: "))
    return a
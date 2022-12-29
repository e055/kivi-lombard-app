import datetime


def date_count(d, dni):
    data = datetime.datetime.strptime(d, "%Y-%m-%d")
    dni = int(dni)
    data_l = data + datetime.timedelta(days=dni)
    data_l = str(data_l)
    data_str = ""
    for i in range(10):
        data_str += data_l[i]
    return data_str

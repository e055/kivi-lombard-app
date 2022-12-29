def compound_interest_comission(k_start, xx, p=1.8, n=1, k=365):
    factor = 1 + p / (100 * k)
    exp = n * k
    res = k_start * factor ** exp
    res = (res - k_start) * xx
    res = round(res, 2)
    return res


def compound_interest_yearly(k_start, x, p=10, n=1, k=1):
    factor = 1 + p / (100 * k)
    exp = n * k
    res = k_start * factor ** exp
    res = (res - k_start) / 365
    res = res * x
    res = round(res, 2)
    return res


def items_val(val_i, dni):
    values = 0
    val = int(val_i)
    p = int(dni)
    val_comp_yearly = compound_interest_yearly(val, p)
    val_comp_commision = compound_interest_comission(val, p)
    val = val + round(val_comp_yearly, 2) + round(val_comp_commision, 2)
    val = val + 15  # 15 to kwota prowizji za sporzadzenie umowy
    values += val
    values = round(values, 2)

    return values

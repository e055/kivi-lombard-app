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
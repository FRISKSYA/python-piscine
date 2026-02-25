import math


def NULL_not_found(object: any) -> int:
    t = type(object)
    if object is None:
        print(f"Nothing: {object} {t}")
    elif t is float and math.isnan(object):
        print(f"Cheese: {object} {t}")
    elif t is int and object == 0:
        print(f"Zero: {object} {t}")
    elif t is str and object == "":
        print(f"Empty: {t}")
    elif t is bool and object is False:
        print(f"Fake: {object} {t}")
    else:
        print("Type not Found")
        return 1
    return 0

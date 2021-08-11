from . import *


def convert(keyword):
    temp = []
    for i in keyword:
        temp.append(unidecode(i))

    return temp
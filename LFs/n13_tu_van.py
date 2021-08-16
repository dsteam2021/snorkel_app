from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_13(x):
    try:
        keyword = ['tư vấn']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']:
                return 13
    except: 
        # print(x)
        pass

    return -1

lfs = [keyword_13]

def get_lfs():
    return lfs
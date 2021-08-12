from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_10(x):
    try:
        keyword = ['khách sạn', 'lưu trú', 'phòng nghỉ']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned'] and x['check_btype'] != 'Xây lắp':
                return 10
    except: 
        # print(x)
        pass

    return -1

lfs = [keyword_10]

def get_lfs():
    return lfs
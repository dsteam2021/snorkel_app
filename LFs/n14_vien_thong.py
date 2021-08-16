from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_14(x):
    try:
        keyword = ['cước gói', 'viễn thông', 'truyền hình', 'cáp', 'cước']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']:
                return 14
    except: 
        # print(x)
        pass

    return -1

lfs = [keyword_14]

def get_lfs():
    return lfs
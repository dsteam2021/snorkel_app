from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_6(x):
    try:
        keyword = ['tên miền', '.com', '.vn', 'phần mềm']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']:
                return 6
    except: 
        # print(x)
        pass
        
    return -1

lfs = [keyword_6]

def get_lfs():
    return lfs
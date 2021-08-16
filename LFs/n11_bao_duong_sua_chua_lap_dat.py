from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_11(x):
    try:
        keyword = ['bảo trì', 'sửa chữa', 'lắp đặt', 'kiểm tra']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']:
                return 11
    except: 
        # print(x)
        pass

    return -1

lfs = [keyword_11]

def get_lfs():
    return lfs
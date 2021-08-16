from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_12(x):
    try:
        keyword = ['quảng cáo', 'chương trình', 'bảng hiệu', 'tiệc', 'hội nghị', 'sự kiện']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']:
                return 12
    except: 
        # print(x)
        pass

    return -1

lfs = [keyword_12]

def get_lfs():
    return lfs
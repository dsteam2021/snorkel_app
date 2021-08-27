from . import *
from .util import convert


# Khiêm
@labeling_function()
def keyword_29(x):
    try:
        keyword = ['ống xả', 'khung', 'lốp', 'bánh răng', 'hộp số', 'đầm bàn', 'động cơ']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']: 
                return 29
    except: 
        # print(x)
        pass
        
    return -1

lfs = [keyword_29]
    
def get_lfs():
    return lfs

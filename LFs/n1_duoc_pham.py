from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_1(x):
    try:
        if x['check_btype'] == 'Dược phẩm':
            keyword = ['thuốc', 'dược']
            for i in keyword:
                if i in x['name_cleaned']: 
                    return 1

        elif x['check_btype'] != 'Dược phẩm':
            pass
            
        don_vi = ['ml', 'l', 'lít', 'lit', 'mg', 'g', 'kg']
        for i in don_vi:
            if i in x['name'].split(): 
                return 1
            if re.search('[0-9].' + i, x['name']):
                return 1

    except: 
        # print(x)
        pass
        
    return -1

lfs = [keyword_1]

def get_lfs():
    return lfs
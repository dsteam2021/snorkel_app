from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_0(x):
    try:
        if x['check_btype'] == 'Bất động sản':
            keyword = ['tiền thuế', 'phí']
            keyword.extend(convert(keyword))
            for i in keyword:
                if i in x['name_cleaned']: 
                    return 0
        elif x['check_btype'] != 'Bất động sản':
            pass
    except: 
        # print(x)
        pass
        
    return -1

lfs = [keyword_0]

def get_lfs():
    return lfs
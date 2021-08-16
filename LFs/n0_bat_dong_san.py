from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_0(x):
    try:
        if x['check_btype'] == 'Bất động sản':
            keyword = ['tiền thuế', 'phí', 'dự án', 'thuê']
            keyword.extend(convert(keyword))
            for i in keyword:
                if i in x['name_cleaned']: 
                    return 0
        elif x['check_btype'] != 'Bất động sản':
            keyword = ['địa chính', 'chỉnh lý', 'trích lục', 'môi giới']
            keyword.extend(convert(keyword))
            for i in keyword:
                if i in x['name_cleaned']: 
                    return 0
    except: 
        # print(x)
        pass
        
    return -1

# Huy
@labeling_function()
def pattern_0(x):
    if re.search('tiền.*đất', x['name_cleaned']):
        return 0
    elif re.search('tiền.*mặt bằng', x['name_cleaned']):
        return 0
    if re.search('thuê.*đất', x['name_cleaned']):
        return 0
    elif re.search('thuê.*mặt bằng', x['name_cleaned']):
        return 0
    return -1

lfs = [keyword_0, pattern_0]
    
def get_lfs():
    return lfs
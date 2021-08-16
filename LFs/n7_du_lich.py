from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_7(x):
    try:
        keyword = ['du lịch', 'tour']
        for i in keyword:
            if i in x['name_cleaned']:
                return 7
    except:
        print(x)

    return -1

# Huy
@labeling_function()
def pattern_7(x):
    try:
        if re.search('dịch vụ.*tour', x['name_cleaned'], flags=re.I):
            return 7
        elif re.search('dich vu.*tour', x['name_cleaned'], flags=re.I):
            return 7
        elif re.search('dich vu.*du lich', x['name_cleaned'], flags=re.I):
            return 7
        elif re.search('dịch vụ.*du lịch', x['name_cleaned'], flags=re.I):
            return 7
    except: 
        # print(x)
        pass
        
    return -1

lfs = [keyword_7, pattern_7]

def get_lfs():
    return lfs
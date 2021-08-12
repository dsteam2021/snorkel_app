from . import *
from .util import convert


@labeling_function()
def keyword_5(x):
    pass

# Huy
@labeling_function()
def pattern_5(x):
    try:
        if re.search('dịch vụ.*lao động', x['name_cleaned'], flgs=re.I):
            return 5
        elif re.search('dich vu.*lao dong', x['name_cleaned'], flgs=re.I):
            return 5
    except: 
        # print(x)
        pass
        
    return -1

lfs = [pattern_5]

def get_lfs():
    return lfs
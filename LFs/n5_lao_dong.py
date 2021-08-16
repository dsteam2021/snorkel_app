from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_5(x):
    keyword = ['ca', 'giờ', 'làm việc', 'lao động', 'nhân viên', 'nhân công', 'dịch vụ', 'đào tạo']
    if x['check_btype'] == 'Dịch vụ cung ứng lao động và việc làm':
        for i in keyword:
            if i in x['name_cleaned']:
              return 5
    
    return -1

# Huy
@labeling_function()
def pattern_5(x):
    try:
        if re.search('dịch vụ.*lao động', x['name_cleaned'], flags=re.I):
            return 5
        elif re.search('dich vu.*lao dong', x['name_cleaned'], flags=re.I):
            return 5
        
        if re.search('cung ứng.*lao động', x['name_cleaned'], flags=re.I):
            return 5
        elif re.search('cung ung.*lao dong', x['name_cleaned'], flags=re.I):
            return 5
    except: 
        # print(x)
        pass
        
    return -1

lfs = [keyword_5, pattern_5]

def get_lfs():
    return lfs
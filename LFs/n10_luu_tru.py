from . import *
from .util import convert


# Huy
@labeling_function()
def keyword_10(x):
    try:
        keyword = ['khách sạn', 'lưu trú', 'phòng nghỉ']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned'] and x['check_btype'] != 'Xây lắp':
                return 10
    except: 
        # print(x)
        pass

    return -1

# Huy
@labeling_function()
def pattern_10(x):
    if re.search('dịch vụ.*phòng', x['name_cleaned']):
      return 10
    elif re.search('dịch vụ.*nghỉ', x['name_cleaned']):
      return 10  

    return -1

lfs = [keyword_10, pattern_10]

def get_lfs():
    return lfs
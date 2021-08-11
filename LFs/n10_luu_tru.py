from __init__ import *

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
        print(x)
    return -1
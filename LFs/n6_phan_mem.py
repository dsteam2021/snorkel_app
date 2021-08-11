from . import *


# Huy
@labeling_function()
def keyword_6(x):
    try:
        keyword = ['tên miền', '.com', '.vn', 'phần mềm']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']:
                return 6
    except:
        print(x)
        
    return -1
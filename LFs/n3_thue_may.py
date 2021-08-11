from __init__ import *

# Huy
@labeling_function()
def keyword_3(x):
    try:
        keyword = ['phí', 'thuế']
        keyword.extend(convert(keyword))
        if x['check_btype'] == 'Máy móc, thiết bị cơ khí, kim khí':
            for i in keyword:
                if i in x['name_cleaned']:
                    return 3
        elif x['check_btype'] != 'Máy móc, thiết bị cơ khí, kim khí':
            pass
    except:
        print(x)
        
    return -1

# Huy
@labeling_function()
def pattern_3(x):
    try:
        if re.search('phí thuê.*máy', x['name_cleaned'], flags=re.I):
            return 3
        elif re.search('phi thue.*may', x['name_cleaned'], flags=re.I):
            return 3
    except:
        print(x)

    return -1
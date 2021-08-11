from __init__ import *


# Huy
@labeling_function()
def key_word_1(x):
    try:
        if x['check_btype'] == 'Dược phẩm':
            keyword = ['thuốc', 'dược']
            keyword.extend(convert(keyword))
            for i in keyword:
                if (i in x['name_cleaned']) or (i in x['company_name']): 
                    return 1

            don_vi = ['ml', 'l', 'lít', 'lit', 'mg', 'g', 'kg']
            for i in don_vi:
                if i in x['name_cleaned'].split(): 
                    return 1
                for j in x['name_cleaned'].split():
                    if re.search('[0-9].*' + 'i', j):
                        return 1

        elif x['check_btype'] != 'Dược phẩm':
            pass
    except: 
        print(x)
        
    return -1
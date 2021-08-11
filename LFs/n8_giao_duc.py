from . import *


# Huy - có cả nhãn 9-(in ấn xuất bản)
@labeling_function()
def keyword_8(x):
    try:
        keyword = ['học phí', 'học kì', 'học kỳ', 'năm học']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']:
                if 'in' in x['check_btype'].split(): 
                    return 9 # in ấn 
                elif 'in' in x['company_name'].split():
                    return 9 # in ấn
                else:
                    return 8
    except:
        print(x)
    
    return -1
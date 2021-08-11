from . import *


# Huy
@labeling_function()
def keyword_9(x):
    try:
        keyword = ['giấy', 'nhãn', 'decal', 'tem', 'label', 'tờ', 'bao', 'hộp']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']:
                if (i=='bao' or i=='hộp'):
                    if (x['check_btype'] == 'Dịch vụ in ấn, xuất bản') \
                        or ('in' in x['company_name'].split()) \
                        or ('bao bì' in x['company_name'].split()):
                        return 9
                else:
                    return 9
    except:
        print(x)
    
    return -1
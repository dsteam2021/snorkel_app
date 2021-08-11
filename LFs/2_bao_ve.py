from __init__ import *


@labeling_function()
def keyword_2(x):
    pass

# Huy
@labeling_function()
def pattern_2(x):
    try:
        if re.search('dịch vụ.*bảo vệ', x['name_cleaned'], flags=re.I):
            return 2
        elif re.search('dich vu.*bao ve', x['name_cleaned'], flags=re.I):
            return 2
    except:
        print(x)
        
    return -1
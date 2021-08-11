from __init__ import *


@labeling_function()
def keyword_2(x):
    pass

@labeling_function()
def pattern_2(x):
    if re.search('dịch vụ.*bảo vệ', x['name_cleaned'], flags=re.I):
        return 2
    elif re.search('dich vu.*bao ve', x['name_cleaned'], flags=re.I):
        return 2
    return -1


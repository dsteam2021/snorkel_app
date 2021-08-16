from . import *


#Khiem
@labeling_function()
def nckh_0(x):
    #parttern
    keywords = ['thử ngiệm', 'thí nghiệm', 'hiệu chuẩn', 'kiểm định']
    for each in keywords:
        if each in x['name_cleaned']:
            return 27
    return -1

lfs = [nckh_0]

def get_lfs():
    return lfs 
from . import *


#Khiem
@labeling_function() 
def vanphongpham_0(x):
    #companyname
    return 23 if "văn phòng phẩm" in x['company_name'] else -1
   
@labeling_function()
def vanphongpham_1(x):
    #keywords
    if x['name_cleaned'].split()[0] == 'bìa':
        return 23
    keywords = ['đồ chơi', 'băng keo', 'bút', 'bài tập', 'bảng tính', 'gôm tẩy', 'phấn']
    for each in keywords:
        if each in x['name_cleaned']:
            return 23
    return -1

lfs = [vanphongpham_0, vanphongpham_1]

def get_lfs():
    return lfs 
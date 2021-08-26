from . import *


#Khiem
import numpy as np
@labeling_function() 
def gasdau_0(x):
    #keywords, parttern
    keywords = ["xăng", "gas", "diezen", "dầu nhờn", "dầu nhớt", "dầu do", "dầu phanh", "nhớt", "oil"]
    for each in keywords:
        if each in x['name_cleaned']:
            return 22
    return -1

@labeling_function() 
def gasdau_1(x):
    try:
        #units and check_btype
        if x['check_btype'] != 'Kinh doanh gas, xăng dầu':
            return -1
        keywords = ['l', 'lít', 'lit', 'ml', 'thùng', 'lon', 'can']
        for each in keywords:
            if x['unit_clean'] == each:
                return 22
    except: 
        pass
    return -1

lfs = [gasdau_0, gasdau_1]

def get_lfs():
    return lfs 
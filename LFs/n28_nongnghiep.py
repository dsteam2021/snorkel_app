from . import *


#Khiem
@labeling_function()
def nongnghiep_0(x):
    #keywords - parttern
    keywords = ['tưới tiêu', 'nuôi trồng']
    for each in keywords:
        if each in x['name_cleaned']:
            return 28
    return -1

@labeling_function()
def nongnghiep_1(x):
    #keywords - pattern - checkBtype
    if x['check_btype'] != 'Nông nghiệp':
        return -1
    keywords = ['củ']
    keywords = {each:0 for each in keywords}
    for each in x['name_cleaned'].split():
        if each in keywords:
            return 28
    pattern = ['trồng cây', 'cây cảnh']
    for each in pattern:
        if each in x['name_cleaned']:
            return 28
    return -1

lfs = [nongnghiep_0, nongnghiep_1]

def get_lfs():
    return lfs 
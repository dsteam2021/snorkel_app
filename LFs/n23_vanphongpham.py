from . import *


#Khiem
@labeling_function() 
def vanphongpham_0(x):
    #companyname
    return 23 if "văn phòng phẩm" in x['company_name'] else -1
   
@labeling_function()
def vanphongpham_1(x):
    #keywords
    keywords = ['đồ chơi', 'băng keo', 'bút', 'bài tập', 'bảng tính', 'gôm tẩy', 'phấn', 'mica', 'vở', 'ghim kẹp', 'kim bấm',
                'ruột chì', 'compa', "ghim dập", "dập ghim", "kẹp giấy", "xếp hình", "bóp viết", "chuốt chì"]
    for each in keywords:
        if each in x['name_cleaned']:
            return 23
    return -1

@labeling_function()
def vanphongpham_2(x):
    #first word
    keywords = ['bìa', 'sổ', 'băng keo', "móc khóa", "sưu tập", "bộ sưu tập", "bấm", 'giấy decal', 'giấy note', 'băng dính',
                'hồ dán', 'hồ khô', 'hồ nước', 'ghim bấm', "giấy in", "bút", "băng đô"]
    for each in keywords:
        if re.search("^" + each, x['name_cleaned']):
            return 23
    return -1

lfs = [vanphongpham_0, vanphongpham_1, vanphongpham_2]

def get_lfs():
    return lfs 
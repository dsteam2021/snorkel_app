from . import *

#Khiem
@labeling_function()
def hoachat_0(x):
    #pattern - keywords
    remove_words = ["nhãn", "thử nghiệm", "trưng bày", "thí nghiệm", "hoa quả"]
    for each in remove_words:
        if each in x['name_cleaned']: 
          return -1
    keywords = ["hóa chất", "nước giặt", "chất thử", "nước tẩy", "ethanol", "sunlight", "sữa rửa mặt", "sữa tắm",
                "dầu gội", "dau goi", "kem đánh răng", "nước giặt", "khử mùi", "kem dưỡng", "kem trắng", "nước hoa"]
    for each in keywords:
        if each in x['name_cleaned']:
          return 19
    return -1

@labeling_function()
def hoachat_1(x):
    #keywords
    remove_words = ["nhãn", "thử nghiệm", "trưng bày", "thí nghiệm"]
    for each in remove_words:
        if each in x['name_cleaned']: 
          return -1
    keywords = ["gift", "ure", "srm", "lifebuoy", "levinia", "acid", "axit", "omo"]
    keywords = {each:0 for each in keywords}
    arr_words = x['name_cleaned'].split()  
    for each in arr_words:
        if each in keywords:
            return 19
    return -1

@labeling_function()
def hoachat_2(x):
    #first pattern
    keywords = ["dung dịch", "đạm", "phân bón", "nước rửa", "phân hữu cơ", "dung môi", "phụ gia", "chất phụ gia",
                "cồn", "chế phẩm", "bột giặt", "chất tẩy", "gel", "bột gel"]
    for each in keywords:
        if re.search("^" + each, x['name_cleaned']):
            return 19
    return -1

lfs = [hoachat_0, hoachat_1, hoachat_2]

def get_lfs():
    return lfs 

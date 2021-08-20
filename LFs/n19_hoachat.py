from . import *

#Khiem
@labeling_function()
def hoachat_0(x):
    #pattern - keywords
    remove_words = ["nhãn", "thử nghiệm", "trưng bày", "thí nghiệm", "nước hoa quả", "quảng cảo"]
    for each in remove_words:
        if each in x['name_cleaned']: 
          return -1
    keywords = ["hóa chất", "nước giặt", "chất thử", "nước tẩy", "ethanol", "sunlight", "sữa rửa mặt", "sữa tắm", "dầu xả", "dưỡng ẩm",
                "dầu gội", "dau goi",  "nước giặt", "khử mùi", "kem trắng", "nước hoa", "tinh dầu", "sơn móng", "dưỡng da", "bột màu",
                "kem nền", "dưỡng chất", "sunsilk", "nhuộm tóc", "tinh chất", "chống nắng", "tẩy rửa", "hương liệu", "diệt khuẩn",
                "sát khuẩn", "dung môi", "dạ hương", "tẩy trang", 'hút ẩm', "phẩm màu", "vi sinh"]
    for each in keywords:
        if each in x['name_cleaned']:
          return 19
    return -1

@labeling_function()
def hoachat_1(x):
    #keywords
    remove_words = ["nhãn", "thử nghiệm", "trưng bày", "thí nghiệm", "quảng cáo", "chi phí"]
    for each in remove_words:
        if each in x['name_cleaned']: 
          return -1
    keywords = ["gift", "ure", "srm", "lifebuoy", "levinia", "acid", "axit", "omo", "dove", "lifebouy", "agar",
                "mascara", "potassium", "vim", "comfort", "cif", "javel", "javen","xmen", "x-men", "serum", "sodium",
                "ponds", "downy", "kdr"]
    keywords = {each:0 for each in keywords}
    arr_words = x['name_cleaned'].split()  
    for each in arr_words:
        if each in keywords:
            return 19
    return -1

@labeling_function()
def hoachat_2(x):
    #first pattern
    keywords = ["dung dịch", "đạm", "phân bón", "nước rửa", "phân hữu cơ", "dung môi", "phụ gia", "chất phụ gia", "xà bông",
                "cồn", "chế phẩm", "bột giặt", "chất tẩy", "gel", "bột gel", "thuốc diệt", "thuốc trừ sâu", "cuộn trừ sâu",
                "nước lau", "nước súc", "son ", "xà phòng", "xịt", "phân npk", "phân kali", "kali", "kaly", "npk", "clear",
                "tẩy", "hóa chất", "chất"]
    for each in keywords:
        if re.search("^" + each, x['name_cleaned']):
            return 19
    return -1

@labeling_function()
def hoachat_3(x):
    keywords = {"nhuộm": {"ws" : ["thuốc", "dịch", "màu", "kem"], "tr": 0},
                "kem": {"ws" : ["bôi", "chống", "đánh răng", "dưỡng", "cream", "mụn", "cạo râu", "tẩy", "da", "lót", "vệ sinh", "trị", "mặt"], "tr": 1},
                "chất": {"ws": ["chuẩn", "thấm", "hút", "chống", "thơm", "khử", "bảo quản", "bôi trơn", "xúc tác", "màu", "kích thích"], "tr": 1},
                "nước": {"ws": ["chuẩn", "cất", "tẩy", "khử", "xả", "giặt", "lau", "xịt", "rữa", "sinh"], "tr": 1},
                "mặt nạ": {"ws": ["bột", "thâm", "sữa", "giấy", "dưỡng", 'chăm sóc', "da", "mask", "đất sét", "thải độc", "trang", "skin", "mụn", "trắng"], "tr": 1},
                "dầu": {"ws": ["tắm", "dưỡng", "thơm", "xả", "xã", "massage"], "tr": 1},
                "vệ sinh": {"ws": ["tẩy", "gel", "bọt", "xịt", "bột", "dầu", "dung dịch"], "tr": 0}}

    for each in keywords:
        for sw in keywords[each]["ws"]:
            if keywords[each]["tr"] == 0:
              if re.search(sw + ".*" + each, x['name_cleaned']):
                  return 19
            else:
              if re.search(each + ".*" + sw, x['name_cleaned']):
                  return 19   
    return -1

lfs = [hoachat_0, hoachat_1, hoachat_2, hoachat_3]

def get_lfs():
    return lfs 

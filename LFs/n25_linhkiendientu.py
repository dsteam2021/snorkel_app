from . import *


#Khiem
@labeling_function()
def vitinhlinhkien_0(x):
    #keywords - parttern
    if "phí thuê" in x['name_cleaned'] and "chi phí thuê" in x['name_cleaned']:
        return -1
    keywords = ['màn hình', 'vi tính', 'máy tính', 'điều khiển', 'mực in', 'máy in', 'định tuyến', 'vô tuyến', 'thu phát', 'mạch chính',
                'dây chuyển', 'cổng chuyển', 'ổ cứng', 'cảm biến', 'mực photocopy', 'máy photocopy', "bàn phím", 'ổ nguồn', "ổ đĩa",
                'chuyển mạch', 'bộ nhớ', 'bộ điện thoại', 'thẻ nhớ', 'mạch chuyển', "không dây"]
    for each in keywords:
        if each in x['name_cleaned']:
            return 25
    return -1

@labeling_function()
def vitinhlinhkien_1(x):
    #keywords 
    keywords = ['switch', 'logitech', 'fuhlen', 'dell', 'asus', 'genius', 'msi', 'acer', 'cpu', 'gpu', 'core', 'dlink', 'usb', 'hdmi', 'vga', 'ibm', "cạc", "loghitech", "lenovo", "micro"]
    keywords = {each:0 for each in keywords}
    arr_words = x['name_cleaned'].split()
    for each in arr_words:
        if each in keywords:
            return 25
    return -1

@labeling_function()
def vitinhlinhkien_2(x):
    #firstword
    keywords = ['pin', 'đtdđ', 'điện thoại', 'đầu ghi', 'camera', 'bộ camera', "bàn phím", "chip", "chíp", "máy quét", "máy tính", "cáp",
                "dây cáp", "điện trở", "máy điện trở", "card", "micro", "bộ micro", "tai nghe"]   
    for each in keywords:
        if re.search("^" + each, x['name_cleaned']):
            return 25
    return -1

lfs = [vitinhlinhkien_0, vitinhlinhkien_1, vitinhlinhkien_2]

def get_lfs():
    return lfs 
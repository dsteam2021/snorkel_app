#Khiem
@labeling_function()
def vitinhlinhkien_0(x):
    #keywords - parttern
    keywords = ['màn hình', 'vi tính', 'máy tính', 'điều khiển', 'mực in', 'máy in', 'định tuyến', 'vô tuyến', 'thu phát', 'mạch chính',
                'dây chuyển', 'cổng chuyển', 'ổ cứng']
    for each in keywords:
        if each in x['name_cleaned']:
            return 25
    return -1

@labeling_function()
def vitinhlinhkien_1(x):
    #keywords 
    keywords = ['logitech', 'fuhlen', 'dell', 'asus', 'genius', 'acer', 'cpu', 'gpu', 'core', 'dlink', 'usb', 'hdmi', 'vga']
    keywords = {each:0 for each in keywords}
    arr_words = x['name_cleaned'].split()
    for each in arr_words:
        if each in keywords:
            return 25
    return -1

lfs = [vitinhlinhkien_0, vitinhlinhkien_1]

def get_lfs():
    return lfs 
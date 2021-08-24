from . import *

#Khiem
@labeling_function()
def maymockimkhi_0(x):
    #firstwords
    keywords = ['máy biến áp', 'biến áp', 'khuôn đúc', "bu lông", 'máy cắt', "bulong", "kìm", "vít ", "nút nhấn", "van ", "máy hàn",
                'khớp nối', 'máy cắt', "tủ điều khiển", "mô tơ", "trụ ", "máy bơm", "bản lề", "máy nén", "tủ điện", "máy may", "côn ",
                "vòng bi", "máy dò", "máy đo"]
    for each in keywords:
        if re.search("^" + each, x['name_cleaned']):
            return 9
    return -1

@labeling_function()
def maymockimkhi_1(x):
    #pattern
    keywords = ['máy cưa', 'lưỡi cưa', "thủy lực", 'nam châm', "khuôn trục", "mỏ lết", 'băng tải', "cờ lê", "máy khoan", "máy chà",
                "mũi khoan", "tô vít", "tô vit", "tua vít", "mũi phay", "con lăn", "máy thổi", "máy mài", "máy vặn", "máy xới"]
    for each in keywords:
      if each in x['name_cleaned']:
          return 9
    return -1

lfs = [maymockimkhi_0, maymockimkhi_1]

def get_lfs():
    return lfs 
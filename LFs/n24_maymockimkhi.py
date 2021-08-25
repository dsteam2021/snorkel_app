from . import *

#Khiem
@labeling_function()
def maymockimkhi_0(x):
    #firstwords
    keywords = ['máy biến áp', 'biến áp', 'khuôn đúc', "bu lông", 'máy cắt', "bulong", "kìm", "vít ", "nút nhấn", "van ", "máy hàn",
                'khớp nối', 'máy cắt', "tủ điều khiển", "mô tơ", "trụ ", "máy bơm", "bản lề", "máy nén", "tủ điện", "máy may", "côn ",
                "vòng bi", "máy dò", "máy đo", "gá "]
    for each in keywords:
        if re.search("^" + each, x['name_cleaned']):
            return 24
    return -1

@labeling_function()
def maymockimkhi_1(x):
    #pattern
    keywords = ['máy cưa', 'lưỡi cưa', "thủy lực", 'nam châm', "khuôn trục", "mỏ lết", 'băng tải', "cờ lê", "máy khoan", "máy chà",
                "mũi khoan", "tô vít", "tô vit", "tua vít", "mũi phay", "con lăn", "máy thổi", "máy mài", "máy vặn", "máy xới", "jig "]
    for each in keywords:
      if each in x['name_cleaned']:
          return 24
    return -1

@labeling_function()
def maymockimkhi_2(x):
    keywords = {"khuôn": {"ws" : ["trục", "đúc", "dao", "pvc", "inox", "nhôm", "thép", "đồng", "ép", "lò", "hàn", "bế", "gá"], "tr": 1},
                "dao_1": {"ws": ["phay", "cắt", "trụ", "phẳng", "tiện"], "tr": 1},
                "dao_2": {"ws": ["mài", "kẹp", "mảnh", "chuôi", "cán"], "tr": 0},
                "gá_1": {"ws": ["đồ", "tấm"], "tr": 0},
                "gá_2": {"ws": ["kẹp", "đỡ"], "tr": 1}}
    for each in keywords:
        t = each.split('_')[0]
        for sw in keywords[each]["ws"]:
            if keywords[each]["tr"] == 0:
              if re.search(sw + ".*" + t, x['name_cleaned']):
                  return 24
            else:
              if re.search(t + ".*" + sw, x['name_cleaned']):
                  return 24    
    return -1

lfs = [maymockimkhi_0, maymockimkhi_1, maymockimkhi_2]

def get_lfs():
    return lfs 
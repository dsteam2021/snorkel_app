from . import *


#Khiem
@labeling_function() 
def vanphongpham_0(x):
    #companyname
    return 23 if "văn phòng phẩm" in x['company_name'] else -1
   
@labeling_function()
def vanphongpham_1(x):
    remove_words = ['trang điểm']
    for each in remove_words:
        if each in x['name_cleaned']:
            return -1
    #keywords
    keywords = ['đồ chơi', 'băng keo', 'bút', 'bài tập', 'bảng tính', 'gôm tẩy', 'phấn', 'mica', 'vở', 'ghim kẹp', 'kim bấm',
                'ruột chì', 'compa', "ghim dập", "dập ghim", "kẹp giấy", "xếp hình", "bóp viết", "chuốt chì", "lau bảng",
                "xóa bảng", "doraemon"]
    for each in keywords:
        if each in x['name_cleaned']:
            return 23
    return -1

@labeling_function()
def vanphongpham_2(x):
    #first word
    keywords = ['bìa', 'sổ', 'băng keo', "móc khóa", "sưu tập", "bộ sưu tập", "bấm", 'giấy decal', 'giấy note', 'băng dính',
                'hồ dán', 'hồ khô', 'hồ nước', 'ghim bấm', "giấy in", "bút", "băng đô", "file", "kẹp file", "chia file", "deli "
                "cặp"]
    for each in keywords:
        if re.search("^" + each, x['name_cleaned']):
            return 23
    return -1

@labeling_function()
def vanphongpham_3(x):
    #keyword giấy
    if re.search("^giấy ", x['name'].lower()) or re.search("^tập giấy ", x['name'].lower()):
        pairWords = ['than', 'lụa', 'ráp', 'fax', 'an', "deli", "màu", "giáp", "excell", "offset"]
        for each in x['name'].split():
            if re.match("^[aA][0-9]", each) or each.lower() in pairWords:
                return 23
    return -1

@labeling_function()
def vanphongpham_4(x):
    #keyword giấy
    keywords = {"kéo": {"ws": ["văn phòng", "lụa", "màu", "bấm", "cắt chỉ", "cắt giấy", "nhỏ", "thiên long", "vp", "tóc", "lớn", "deli"], "tr": 1},
                "deli": {"ws": ["dao", "ghim", "bấm", "gôm", "bút", "chì", "kẹp", "gọt", "giá", "tẩy", "bảng", "hồ sơ", "cặp"], "tr": 0},
                "giấy": {"ws": ["mĩ thuật", "mỹ thuật", "gói quà", "thắm dầu", "thủ công", "trang trí"], "tr": 1},
                "bảng": {"ws": ["tên", "ghim", "môn", "từ", "đen", "vẽ", "số"], "tr": 1},
                "tập": {"ws": ["tô", "học sinh", "chữ", "màu", "toán", "trang", "chữ", "đi"], "tr": 1},
                "dây": {"ws": ["thẻ", "đeo", "nhảy"], "tr": 1},
                "thước": {"ws": ["dây", "kẻ", "học sinh", "cuộn", "góc", "dẻo"], "tr": 1}}
    for each in keywords:
        for sw in keywords[each]["ws"]:
            if keywords[each]["tr"] == 0:
              if re.search(sw + ".*" + each, x['name_cleaned']) or re.search(sw + ".*" + each, x['name'].lower()):
                  return 23
            else:
              if re.search(each + ".*" + sw, x['name_cleaned']) or re.search(each + ".*" + sw, x['name'].lower()):
                  return 23    
    return -1


lfs = [vanphongpham_0, vanphongpham_1, vanphongpham_2, vanphongpham_3]

def get_lfs():
    return lfs 
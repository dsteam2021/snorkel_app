#author=hanghust

from snorkel.labeling import labeling_function

@labeling_function()
def do_dung_gia_dinh_40(x):
    do_dung_gia_dinh = set(['bàn_chải', 'chổi', 'dao', 'rổ', 'muỗng', 'đũa', 'lau_nhà', 'chén', 'quét', 'bát', 'lược', 'dĩa', 'thìa', 'thớt', 'dao_cạo', 'nĩa', 'bình_xịt'])
    if any(substring in x.name_cleaned.split() for substring in do_dung_gia_dinh):
        return 40
    return -1

lfs = [do_dung_gia_dinh_40]

def get_lfs():
    return lfs 
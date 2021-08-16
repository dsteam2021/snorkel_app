
#author=hanghust

from snorkel.labeling import labeling_function


@labeling_function()
def do_an_42(x):
    do_an = set(['kem', 'kẹo', 'socola', 'nướng', 'bánh_quy', 'cơm', 'xào', 'chiên', 'ăn_uống', 'snack', 'chocolate', 'dừa',
            'bánh_mì', 'phô_mai', 'cosy', 'lẩu', 'hải_sản', 'vani', 'merino', 'trái_cây', 'đậu_phộng', 'đậu_xanh', 'choco', 
            'xúc_xích', 'ăn_liền', 'chuối', 'sữa_chua', 'burger', 'bún', 'salad', 'celano', 'sôcôla', 'xoài', 'cake', 'cookies', 
            'súp', 'chua_cay', 'thập_cẩm', 'phomai', 'cheese', 'sầu_riêng', 'cốm', 'mật_ong', 'hạnh_nhân', 'bánh_tráng', 'cháo'])
    if any(substring in x.name_cleaned.split() for substring in do_an):
        return 42
    return -1

@labeling_function()
def company_do_an_42(x):
    do_an_cn = set(['nhà_hàng', 'ăn_uống', 'dinh_dưỡng'])
    if any(substring in x.company_name.split() for substring in do_an_cn):
        return 42
    return -1

lfs = [do_an_42, company_do_an_42]

def get_lfs():
    return lfs 
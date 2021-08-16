#author=hanghust

from snorkel.labeling import labeling_function


@labeling_function(pre=[spacy])
def tb_y_te_33(x):
    tb_y_te = set(['khẩu_trang', 'nẹp', 'nhiệt_kế', 'găng_tay', 'tiêm', 'gạc', 'kit', 'ống_nghiệm', 'vô_trùng', 'huyết_áp', 'nhĩ_kỳ', 'tĩnh_mạch'])
    if any(substring in x.name_cleaned.split() for substring in tb_y_te):
        return 33
    return -1


lfs = [tb_y_te_33]

def get_lfs():
    return lfs 
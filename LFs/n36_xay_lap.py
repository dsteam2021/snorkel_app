#author=hanghust

from snorkel.labeling import labeling_function

@labeling_function(pre=[spacy])
def xay_lap_36(x):
    xay_lap = set(['thi_công', 'công_trình', 'dự_án', 'hạng_mục', 'gói_thầu', 'thẩm_tra', 'nghiệm_thu', 'dự_toán', 'đường_ống', 'xây_lắp', 'tháo_dỡ'])
    if any(substring in x.name_cleaned.split() for substring in xay_lap):
        return 36
    return -1

lfs = [xay_lap_36]

def get_lfs():
    return lfs 
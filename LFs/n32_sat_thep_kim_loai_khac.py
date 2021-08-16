#author=hanghust

from snorkel.labeling import labeling_function

@labeling_function(pre=[spacy])
def sat_thep_kl_32(x):
    sat_thep_kl = set(['thép', 'kẽm', 'nhôm', 'sắt', 'đồng', 'không_gỉ', 'hợp_kim', 'định_hình', 'thanh_giằng',  'thiếc'])
    if any(substring in x.name_cleaned.split() for substring in sat_thep_kl):
        return 32
    return -1

@labeling_function(pre=[spacy])
def company_sat_thep_kl_32(x):
    sat_thep_kl_cn =  set(['thép', 'kẽm', 'nhôm', 'inox', 'sắt', 'đồng', 'hợp_kim', 'thiếc'])
    if any(substring in x.company_name.split() for substring in sat_thep_kl_cn):
        return 32
    return -1

lfs = [sat_thep_kl_32, company_sat_thep_kl_32]

def get_lfs():
    return lfs 
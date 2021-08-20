
#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy])
def do_an_42(x):
    do_an = set(['kem', 'kẹo', 'socola', 'nướng', 'bánh_quy', 'cơm', 'xào', 'chiên', 'ăn_uống', 'snack', 'chocolate', 'dừa',
            'bánh_mì', 'phô_mai', 'cosy', 'lẩu', 'hải_sản', 'vani', 'merino', 'trái_cây', 'đậu_phộng', 'đậu_xanh', 'choco', 
            'xúc_xích', 'ăn_liền', 'chuối', 'sữa_chua', 'burger', 'bún', 'salad', 'celano', 'sôcôla', 'xoài', 'cake', 'cookies', 
            'súp', 'chua_cay', 'thập_cẩm', 'phomai', 'cheese', 'sầu_riêng', 'cốm', 'mật_ong', 'hạnh_nhân', 'bánh_tráng', 'cháo'])
    # if any(substring in x.name_cleaned for substring in do_an):
    #     return 42
    try:
        for substring in do_an:
            if substring in x.name_cleaned:
                return 42
    except:
        return -1
    return -1

@labeling_function(pre=[spacy_cn])
def company_do_an_42(x):
    do_an_cn = set(['nhà_hàng', 'ăn_uống', 'dinh_dưỡng'])
    # if any(substring in x.company_name for substring in do_an_cn):
    #     return 42
    try:
        for substring in do_an_cn:
            if substring in x.company_name:
                return 42
    except:
        return -1
    return -1

lfs = [do_an_42, company_do_an_42]

def get_lfs():
    return lfs 
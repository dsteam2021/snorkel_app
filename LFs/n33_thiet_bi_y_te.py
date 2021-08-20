#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="text", doc_field="doc", memoize=True)
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
import re

@labeling_function(pre=[spacy])
def tb_y_te_33(x):
    tb_y_te = set(['khẩu_trang', 'nẹp', 'nhiệt_kế', 'găng_tay', 'tiêm', 'gạc', 'kit', 'ống_nghiệm', 'vô_trùng', 'huyết_áp', 'nhĩ_kỳ', 'tĩnh_mạch'])
    # if any(substring in x.name_cleaned for substring in tb_y_te):
    #     return 33
    try:
        for substring in tb_y_te:
            if substring in x.name_cleaned:
                return 33
    except:
        return -1
    return -1

@labeling_function()
def company_tb_y_te_33(x):
    
    try:
        if 'thiết bị y tế' in x.company_name or 'dụng cụ y khoa' in x.company_name:
            return 33
        else:
            return -1
    except:
        return -1

lfs = [tb_y_te_33, company_tb_y_te_33]

def get_lfs():
    return lfs 
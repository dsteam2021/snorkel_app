#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy])
def xay_lap_36(x):
    try: 
        xay_lap = set(['thi_công', 'công_trình', 'dự_án', 'hạng_mục', 'gói_thầu', 'thẩm_tra', 'nghiệm_thu', 'dự_toán', 'đường_ống', 'xây_lắp', 'tháo_dỡ'])
        # if any(substring in x.name_cleaned for substring in xay_lap):
        #     return 36
        for substring in xay_lap:
            if substring in x.name_cleaned:
                return 36
    except:
        return -1
    return -1

@labeling_function(pre=[spacy_cn])
def company_xay_lap_36(x):
    try: 
        xay_lap_cn = set(['thi_công', 'công_trình', 'xây_lắp', 'xây_dựng'])
        # if any(substring in x.name_cleaned for substring in xay_lap):
        #     return 36
        for substring in xay_lap_cn:
            if substring in x.company_name:
                return 36
    except:
        return -1
    return -1
lfs = [xay_lap_36, company_xay_lap_36]

def get_lfs():
    return lfs 
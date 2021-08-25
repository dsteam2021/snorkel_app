#author=hanghust

from snorkel.labeling import labeling_function
# from snorkel.preprocess.nlp import SpacyPreprocessor
# spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
# spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

# @labeling_function(pre=[spacy])
@labeling_function()
def sat_thep_kl_32(x):
    sat_thep_kl = set(['thép', 'kẽm', 'nhôm', 'sắt', 'đồng', 'không gỉ', 'hợp kim', 'định hình', 'thanh giằng',  'thiếc',
    'không rỉ'])
    # if any(substring in x.name_cleaned for substring in sat_thep_kl):
    #     return 32
    try:
        for substring in sat_thep_kl:
            if substring in x.name_cleaned.lower():
                return 32
    except:
        return -1
    return -1

# @labeling_function(pre=[spacy_cn])
@labeling_function()
def company_sat_thep_kl_32(x):
    sat_thep_kl_cn =  set(['thép', 'kẽm', 'nhôm', 'inox', 'sắt', 'đồng', 'hợp kim', 'thiếc'])
    # if any(substring in x.company_name for substring in sat_thep_kl_cn):
    #     return 32
    try:
        for substring in sat_thep_kl_cn:
            if substring in x.company_name.lower():
                return 32
    except:
        return -1
    return -1

lfs = [sat_thep_kl_32, company_sat_thep_kl_32]

def get_lfs():
    return lfs 
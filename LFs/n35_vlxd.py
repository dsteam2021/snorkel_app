#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy])
def vlxd_35(x):
    vlxd =  set(['sơn', 'gạch', 'pvc', 'xi_măng', 'ppr', 'upvc', 'hdpe', 'bê_tông', 'ngói', 'xịt', 'tường', 'lavabo', 'cát', 'bệt', 'thạch_cao', 'ốp_lát', 'nội_thất', 'ngoại_thất', 'dekko', 'bồn_cầu',
            'vòi_sen', 'gạch_men', 'granite', 'dulux', 'sika'])
    # if any(substring in x.name_cleaned for substring in vlxd):
    #     return 35
    try:
        for substring in vlxd:
            if substring in x.name_cleaned:
                return 35
    except:
        return -1
    return -1

lfs = [vlxd_35]

def get_lfs():
    return lfs 
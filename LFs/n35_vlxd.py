#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
# spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)

# @labeling_function(pre=[spacy])
@labeling_function()
def vlxd_35(x):
    vlxd =  set(['sơn', 'gạch', 'pvc', 'xi măng', 'ppr', 'upvc', 'hdpe', 'bê tông', 'ngói', 'xịt', 'tường', 'lavabo', 'cát', 'bệt', 'thạch cao', 'ốp lát', 'nội thất', 'ngoại thất', 'dekko', 'bồn cầu',
            'vòi sen', 'gạch men', 'granite', 'dulux', 'sika', 'ceramic', 'ốp lát'])
    # if any(substring in x.name_cleaned for substring in vlxd):
    #     return 35
    try:
        for substring in vlxd:
            if substring in x.name_cleaned.lower():
                return 35
    except:
        return -1
    return -1

@labeling_function()
def company_vlxd_35(x):
    vlxd_cn =  set(['vật liệu xây dựng', 'sơn'])
    # if any(substring in x.name_cleaned for substring in vlxd):
    #     return 35
    try:
        for substring in vlxd_cn:
            if substring in x.company_name.lower():
                return 35
    except:
        return -1
    return -1
lfs = [vlxd_35, company_vlxd_35]

def get_lfs():
    return lfs 
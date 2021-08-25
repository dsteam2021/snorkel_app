#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

# @labeling_function(pre=[spacy])
@labeling_function()
def oto_xemay_38(x):
    oto_xemay = set(['honda', 'ô tô', 'xe máy', 'hyundai', 'mô tô', 'yamaha', 'toyota', 'xe đạp', 'wave', 'mitsubishi', 'suzuki', 'vision', 'gắn máy', 'future', 'accent',
             'santafe', 'sirius', 'ôtô', 'kia', 'ford', 'isuzu', 'tucson', 'thaco', 'espero', 'mazda', 'sym', 'exciter', 'alpha', 'winnerx', 'xpander', 'fortuner', 'sedan', 'winner'])
    # if any(substring in x.name_cleaned for substring in oto_xemay):
    #     return 38
    try:
        for substring in oto_xemay:
            if substring in x.name_cleaned.lower():
                return 38
    except:
        return -1
    return -1

# @labeling_function(pre=[spacy_cn])
@labeling_function()
def company_oto_xemay_38(x):
    oto_xemay_cn = set(['ô tô', 'xe máy', 'hyundai', 'toyota', 'ôtô', 'xe đạp', 'mô tô', 'motors', 'daehan'])
    # if any(substring in x.company_name for substring in oto_xemay_cn):
    #     return 38
    try:
        for substring in oto_xemay_cn:
            if substring in x.company_name.lower():
                return 38
    except:
        return -1
    return -1


lfs = [oto_xemay_38, company_oto_xemay_38]

def get_lfs():
    return lfs 
#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy])
def oto_xemay_38(x):
    oto_xemay = set(['honda', 'ô_tô', 'xe_máy', 'ô_tô_con', 'hyundai', 'mô_tô', 'yamaha', 'toyota', 'xe_đạp', 'wave', 'mitsubishi', 'suzuki', 'vision', 'xe_máy_điện', 'gắn_máy', 'future', 'accent',
             'santafe', 'sirius', 'ôtô', 'kia', 'ford', 'isuzu', 'tucson', 'thaco', 'espero', 'mazda', 'sym', 'exciter', 'alpha', 'winnerx', 'xpander', 'fortuner', 'sedan', 'winner'])
    if any(substring in x.name_cleaned for substring in oto_xemay):
        return 38
    return -1

@labeling_function(pre=[spacy_cn])
def company_oto_xemay_38(x):
    oto_xemay_cn = set(['ô_tô', 'xe_máy', 'hyundai', 'toyota', 'ôtô', 'xe_đạp', 'mô_tô', 'motors', 'daehan'])
    if any(substring in x.company_name for substring in oto_xemay_cn):
        return 38
    return -1


lfs = [oto_xemay_38, company_oto_xemay_38]

def get_lfs():
    return lfs 
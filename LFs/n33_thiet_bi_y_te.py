#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="text", doc_field="doc", memoize=True)
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy])
def tb_y_te_33(x):
    tb_y_te = set(['khẩu_trang', 'nẹp', 'nhiệt_kế', 'găng_tay', 'tiêm', 'gạc', 'kit', 'ống_nghiệm', 'vô_trùng', 'huyết_áp', 'nhĩ_kỳ', 'tĩnh_mạch'])
    if any(substring in x.name_cleaned for substring in tb_y_te):
        return 33
    return -1


lfs = [tb_y_te_33]

def get_lfs():
    return lfs 
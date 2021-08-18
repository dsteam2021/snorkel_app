#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)


@labeling_function(pre=[spacy_cn])
def company_thuc_pham_34(x):
    thuc_pham_cn =  set(['thực_phẩm', 'foods', 'chợ'])
    # if any(substring in x.company_name for substring in thuc_pham_cn):
    #     return 34
    for substring in thuc_pham_cn:
        if substring in x.company_name:
            return 34
    return -1

lfs = [company_thuc_pham_34]

def get_lfs():
    return lfs 
#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy])
def nhua_caosu_giay_31(x):
    nhua_caosu_giay = set(['nhựa', 'cao_su', 'giấy', 'cao', 'su', 'mica', 'osmia', 'hdpe', 'lldpe', 'silicon', 'pallet', 'băng_dính', 'cosano'])
    # if any(substring in x.name_cleaned for substring in do_dung_gia_dinh):
    #     return 40
    try:
        for substring in nhua_caosu_giay:
            if substring in x.name_cleaned and x.check_btype == 'Sản xuất sản phẩm từ nhựa, cao su, giấy':
                return 31
    except:
        return -1
    return -1

lfs = [nhua_caosu_giay_31]

def get_lfs():
    return lfs 
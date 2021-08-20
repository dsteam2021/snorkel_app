#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy])
def do_uong_41(x):
    do_uong = set(['rượu', 'sữa', 'trà', 'bia', 'rượu_vang', 'sauvignon', 'cabernet', 'vinamilk', 'tiger', 'scu', 'milk', 'sting', 'soda', 'pepsi', 'sleek', 'chateau', 'tea', 'sữa_tươi', 'blanc', 'cà_phê', 'heineken', 
                   'siro', 'sinh_tố', 'bia_lon',  'coca', 'nước_ngọt', 'milo', 'chardonnay', 'coke', 'merlot', 'vodka', 'wine', 'syrup', 'cafe', 'nước_khoáng', 'twister', 'vfresh', 'lavie', 'fanta', 'lipton', 'nestle',
                   'nescafe', 'susu', 'reserva', 'whisky', 'pinot', 'bia_chai', 'sprite', 'mirinda', 'nước_giải_khát', 'shiraz', 'special', 'chivas', 'coffee', 'probi', 'revive', 'aquafina', 'sirô', 'bordeaux', 'oolong', 'latte', 'monin'])
    # if any(substring in x.name_cleaned for substring in do_uong):
    #     return 41
    try:
        for substring in do_uong:
            if substring in x.name_cleaned:
                return 41
    except:
        return -1
    return -1

@labeling_function(pre=[spacy_cn])
def company_do_uong_41(x):
    do_uong_cn = set(['rượu', 'uống'])
    # if any(substring in x.company_name for substring in do_uong_cn):
    #     return 41
    try:
        for substring in do_uong_cn:
            if substring in x.company_name:
                return 41
    except:
        return -1
    return -1

lfs = [do_uong_41, company_do_uong_41]

def get_lfs():
    return lfs 
#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)


@labeling_function(pre=[spacy])
def dien_may_thiet_bi_gia_dung_39(x):
    dien_may_thiet_bi_gia_dung = set(['quạt', 'ổ_cắm', 'nồi', 'bếp', 'dây_điện', 'cầu_dao', 'tivi', 'ắc_quy', 'panasonic', 'phích', 'cầu_chì', 'tủ_lạnh', 'máy_lạnh', 'daikin', 'máy_xay',  'máy_giặt', 'quạt_trần', 'cơm_điện', 'đèn_pin',
                              'inverter', 'samsung', 'đồng_hồ', 'lioa', 'điện_áp', 'aptomat', 'toshiba', 'asanzo', 'siêu_tốc', 'sunhouse'])
    # if any(substring in x.name_cleaned for substring in dien_may_thiet_bi_gia_dung):
    #     return 39
    try:
        for substring in dien_may_thiet_bi_gia_dung:
            if substring in x.name_cleaned:
                return 39
    except:
        return -1
    return -1

@labeling_function(pre=[spacy_cn])
def company_dien_may_thiet_bi_gia_dung_39(x):
    dien_may_thiet_bi_gia_dung_cn = set( ['điện_máy', 'điện_lạnh', 'cơ_điện_lạnh'])
    # if any(substring in x.company_name for substring in dien_may_thiet_bi_gia_dung_cn):
    #     return 39
    try:
        for substring in dien_may_thiet_bi_gia_dung_cn:
            if substring in x.company_name:
                return 39
    except:
        return -1
    return -1

lfs = [dien_may_thiet_bi_gia_dung_39, company_dien_may_thiet_bi_gia_dung_39]

def get_lfs():
    return lfs 
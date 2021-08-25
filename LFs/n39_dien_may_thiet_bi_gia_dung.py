#author=hanghust

from snorkel.labeling import labeling_function
# from snorkel.preprocess.nlp import SpacyPreprocessor
# spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
# spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)


# @labeling_function(pre=[spacy])
@labeling_function()
def dien_may_thiet_bi_gia_dung_39(x):
    dien_may_thiet_bi_gia_dung = set(['quạt', 'ổ cắm', 'nồi', 'bếp', 'dây điện', 'cầu dao', 'tivi', 'ắc quy', 'panasonic', 'phích', 'cầu chì', 'tủ lạnh', 'máy lạnh', 'daikin', 'máy xay',  'máy giặt', 'quạt trần', 'cơm điện', 'đèn pin',
                              'inverter', 'samsung', 'đồng hồ', 'lioa', 'điện áp', 'aptomat', 'toshiba', 'asanzo', 'siêu tốc', 'sunhouse'])
    # if any(substring in x.name_cleaned for substring in dien_may_thiet_bi_gia_dung):
    #     return 39
    try:
        for substring in dien_may_thiet_bi_gia_dung:
            if substring in x.name_cleaned.lower():
                return 39
    except:
        return -1
    return -1

# @labeling_function(pre=[spacy_cn])
@labeling_function()
def company_dien_may_thiet_bi_gia_dung_39(x):
    dien_may_thiet_bi_gia_dung_cn = set( ['điện máy', 'điện lạnh'])
    # if any(substring in x.company_name for substring in dien_may_thiet_bi_gia_dung_cn):
    #     return 39
    try:
        for substring in dien_may_thiet_bi_gia_dung_cn:
            if substring in x.company_name.lower():
                return 39
    except:
        return -1
    return -1

lfs = [dien_may_thiet_bi_gia_dung_39, company_dien_may_thiet_bi_gia_dung_39]

def get_lfs():
    return lfs 
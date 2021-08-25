
#author=hanghust

from snorkel.labeling import labeling_function
# from snorkel.preprocess.nlp import SpacyPreprocessor
# spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
# spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

# @labeling_function(pre=[spacy])
@labeling_function()
def do_an_42(x):
    do_an = set(['kem', 'kẹo', 'socola', 'nướng', 'bánh quy', 'cơm', 'xào', 'chiên', 'ăn uống', 'snack', 'chocolate', 'dừa',
            'bánh mì', 'phô mai', 'cosy', 'lẩu', 'hải sản', 'vani', 'merino', 'trái cây', 'đậu phộng', 'đậu xanh', 'choco', 
            'xúc xích', 'ăn liền', 'chuối', 'sữa chua', 'burger', 'bún', 'salad', 'celano', 'sôcôla', 'xoài', 'cake', 'cookies', 
            'súp', 'chua cay', 'thập cẩm', 'phomai', 'cheese', 'sầu riêng', 'cốm', 'mật ong', 'hạnh nhân', 'bánh tráng', 'cháo'])
    # if any(substring in x.name_cleaned for substring in do_an):
    #     return 42
    try:
        for substring in do_an:
            if substring in x.name_cleaned.lower():
                return 42
    except:
        return -1
    return -1

# @labeling_function(pre=[spacy_cn])
@labeling_function()
def company_do_an_42(x):
    do_an_cn = set(['nhà hàng', 'ăn uống', 'dinh dưỡng', 'restaurant'])
    # if any(substring in x.company_name for substring in do_an_cn):
    #     return 42
    try:
        for substring in do_an_cn:
            if substring in x.company_name.lower():
                return 42
    except:
        return -1
    return -1

lfs = [do_an_42, company_do_an_42]

def get_lfs():
    return lfs 
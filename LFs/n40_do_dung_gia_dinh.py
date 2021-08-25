#author=hanghust

from snorkel.labeling import labeling_function
# from snorkel.preprocess.nlp import SpacyPreprocessor
# spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)

# @labeling_function(pre=[spacy])
@labeling_function()
def do_dung_gia_dinh_40(x):
    do_dung_gia_dinh = set(['bàn chải', 'chổi', 'dao', 'rổ', 'muỗng', 'đũa', 'lau nhà', 'chén', 'quét', 'bát', 'lược', 'dĩa', 'thìa', 'thớt', 'dao cạo', 'nĩa', 'bình xịt'])
    # if any(substring in x.name_cleaned for substring in do_dung_gia_dinh):
    #     return 40
    try:
        for substring in do_dung_gia_dinh:
            if substring in x.name_cleaned.lower():
                return 40
    except:
        return -1
    return -1

lfs = [do_dung_gia_dinh_40]

def get_lfs():
    return lfs 
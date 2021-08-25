#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
# spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
# spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

# @labeling_function(pre=[spacy])

@labeling_function()
def xay_lap_36(x):
    try: 
        xay_lap = set(['thi công', 'công trình', 'dự án', 'hạng mục', 'gói thầu', 'giám sát', 'nghiệm thu', 'dự toán', 'đường ống', 'xây lắp', 'tháo dỡ',
        'thẩm tra', 'bản vẽ', 'hạng mục', 'lắp đặt', 'dự toán', 'cải tạo', 'xây dựng'])
        # if any(substring in x.name_cleaned for substring in xay_lap):
        #     return 36
        for substring in xay_lap:
            if substring in x.name_cleaned.lower():
                return 36
    except:
        return -1
    return -1

# @labeling_function(pre=[spacy_cn])

@labeling_function()
def company_xay_lap_36(x):
    try: 
        xay_lap_cn = set(['thi công', 'công trình', 'xây lắp', 'xây dựng'])
        # if any(substring in x.name_cleaned for substring in xay_lap):
        #     return 36
        for substring in xay_lap_cn:
            if substring in x.company_name.lower():
                return 36
    except:
        return -1
    return -1
lfs = [xay_lap_36, company_xay_lap_36]

def get_lfs():
    return lfs 
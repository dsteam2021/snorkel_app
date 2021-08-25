#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
# spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
# spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

# @labeling_function(pre=[spacy])
@labeling_function()
def thuc_pham_34(x):
    thuc_pham =  set(['thịt', 'bò', 'cá', 'đông lạnh', 'gà', 'heo', 'mì', 'gạo',  'rau', 'ớt', 'muối', 'sườn', 'bắp', 'nước mắm', 'gia vị', 
                      'nạc', 'đùi', 'trứng', 'hữu cơ', 'tương ớt',  'xúc xích', 'ngũ cốc', 'khoai tây', 'phở', 'tỏi', 'cá ngừ', 'cà chua', 
                      'maggi', 'ridielac', 'nui', 'cá hồi', 'thực phẩm', 'organic', 'knorr', 'chanh', 'vịt', 'bột ngọt', 'củ cải', 'chinsu', 
                      'xà lách', 'gừng', 'fillet', 'đậu nành', 'mắm', 'thăn', 'lợn', 'mì tôm', 'tôm'])
    # if any(substring in x.company_name for substring in thuc_pham_cn):
    #     return 34
    try:
        for substring in thuc_pham:
            if substring in x.name_cleaned.lower():
                return 34
    except:
        return -1
    return -1

# @labeling_function(pre=[spacy_cn])
@labeling_function()
def company_thuc_pham_34(x):
    thuc_pham_cn =  set(['thực phẩm', 'foods', 'chợ'])
    # if any(substring in x.company_name for substring in thuc_pham_cn):
    #     return 34
    try:
        for substring in thuc_pham_cn:
            if substring in x.company_name.lower():
                return 34
    except:
        return -1
    return -1

lfs = [thuc_pham_34, company_thuc_pham_34]

def get_lfs():
    return lfs 
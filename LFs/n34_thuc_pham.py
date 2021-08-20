#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy])
def thuc_pham_34(x):
    thuc_pham =  set(['thịt', 'bò', 'cá', 'đông_lạnh', 'gà', 'heo', 'mì', 'gạo',  'rau', 'ớt', 'muối', 'sườn', 'bắp', 'nước_mắm', 'gia_vị', 
                      'nạc', 'đùi', 'trứng', 'hữu_cơ', 'tương_ớt',  'xúc_xích', 'ngũ_cốc', 'khoai_tây', 'phở', 'tỏi', 'cá_ngừ', 'cà_chua', 
                      'maggi', 'ridielac', 'nui', 'cá_hồi', 'thực_phẩm', 'organic', 'knorr', 'chanh', 'vịt', 'bột_ngọt', 'củ_cải', 'chinsu', 
                      'xà_lách', 'gừng', 'fillet', 'đậu_nành', 'mắm'])
    # if any(substring in x.company_name for substring in thuc_pham_cn):
    #     return 34
    try:
        for substring in thuc_pham:
            if substring in x.name_cleaned:
                return 34
    except:
        return -1
    return -1

@labeling_function(pre=[spacy_cn])
def company_thuc_pham_34(x):
    thuc_pham_cn =  set(['thực_phẩm', 'foods', 'chợ'])
    # if any(substring in x.company_name for substring in thuc_pham_cn):
    #     return 34
    try:
        for substring in thuc_pham_cn:
            if substring in x.company_name:
                return 34
    except:
        return -1
    return -1

lfs = [thuc_pham_34, company_thuc_pham_34]

def get_lfs():
    return lfs 
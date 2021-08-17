#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy])
def y_te_37(x):
    y_te = set(['khám', 'kiểm_dịch', 'xét_nghiệm', 'sức_khỏe', 'siêu_âm', 'giám_định', 'xquang', 'bệnh', 'điều_trị', 'pcr', 'viện_phí', 'nội_soi', 'phẫu_thuật', 'nhổ', 'cột_sống', 'tủy', 'phổi', 
        'tế_bào', 'họng',  'igg', 'nước_tiểu', 'tổng_phân_tích','điện_tim', 'vết_thương', 'khâu', 'ung_thư', 'hiv', 'chuyên_khoa', 'thắt_lưng'])
    if any(substring in x.name_cleaned for substring in y_te):
        return 37
    return -1

@labeling_function(pre=[spacy_cn])
def company_y_te_37(x):
    y_te_cn = set(['bệnh_viện', 'đa_khoa', 'phòng_khám', 'pháp_y', 'y_khoa', 'tâm_thần', 'bệnh_tật', 'kiểm_dịch', 'phục_hồi', 'cấp_cứu', 'chỉnh_hình', 'nam_khoa', 'sức_khỏe',
           'bác_sĩ', 'nha_khoa', 'trị_liệu', 'thú_y', 'y_học'])
    if any(substring in x.company_name for substring in y_te_cn):
        return 37
    return -1

lfs = [y_te_37, company_y_te_37]

def get_lfs():
    return lfs 
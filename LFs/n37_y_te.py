#author=hanghust

from snorkel.labeling import labeling_function
# from snorkel.preprocess.nlp import SpacyPreprocessor
# spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
# spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

# @labeling_function(pre=[spacy])
@labeling_function()
def y_te_37(x):
    y_te = set(['khám', 'kiểm dịch', 'xét nghiệm', 'sức khỏe', 'siêu âm', 'giám định', 'xquang', 'bệnh', 'điều trị', 'pcr', 'viện phí', 'nội soi', 'phẫu thuật', 'nhổ', 'cột sống', 'tủy', 'phổi', 
        'tế bào', 'họng',  'igg', 'nước tiểu', 'tổng phân tích','điện tim', 'vết thương', 'khâu', 'ung thư', 'hiv', 'chuyên khoa', 'thắt lưng', 'bảo hiểm', 'bồi dưỡng', 'điện châm', 'tổn hại',
        'tử thi', 'tử thi', 'chếch', 'cộng hưởng', 'phụ khoa', 'vết thương', 'khớp', 'tiêm vắc'])
    # if any(substring in x.name_cleaned for substring in y_te):
    #     return 37
    try:
        for substring in y_te:
            if substring in x.name_cleaned.lower():
                return 37
    except:
        return -1
    return -1

# @labeling_function(pre=[spacy_cn])
@labeling_function()
def company_y_te_37(x):
    y_te_cn = set(['bệnh viện', 'đa khoa', 'phòng khám', 'pháp y', 'y khoa', 'tâm thần', 'bệnh tật', 'kiểm dịch', 'phục hồi', 'cấp cứu', 'chỉnh hình', 'nam khoa', 'sức khỏe',
           'bác sĩ', 'nha khoa', 'trị liệu', 'thú y', 'y học'])
    # if any(substring in x.company_name for substring in y_te_cn):
    #     return 37
    try:
        for substring in y_te_cn:
            if substring in x.company_name.lower():
                return 37
    except:
        return -1
    return -1

lfs = [y_te_37, company_y_te_37]

def get_lfs():
    return lfs 
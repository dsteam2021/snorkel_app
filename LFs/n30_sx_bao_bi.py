#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
# spacy = SpacyPreprocessor(text_field="name_cleaned", doc_field="doc", memoize=True)
# spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

# @labeling_function(pre=[spacy])
@labeling_function()
def sx_bao_bi_30(x):
    sx_bao_bi = set(['bao bì', 'nhãn mác', 'bao', 'bì', 'nắp', 'carton', 'túi', 'màng', 'nhãn', 'box', 'bag', 'sticker', 'nilon', 'flexo', 'bìa', 'henckels', 'spoon', 'hdpe',  'proof'])
    # if any(substring in x.company_name for substring in sx_bao_bi_cn):
    #     return 30
    try:
        for substring in sx_bao_bi:
            if substring in x.name_cleaned.lower() and x.check_btype == 'Sản xuất bao bì':
                return 30
    except:
        return -1
    return -1

# @labeling_function(pre=[spacy_cn])
@labeling_function()
def company_sx_bao_bi_30(x):
    sx_bao_bi_cn = set(['bao bì', 'nhãn mác'])
    # if any(substring in x.company_name for substring in sx_bao_bi_cn):
    #     return 30
    try:
        for substring in sx_bao_bi_cn:
            if substring in x.company_name.lower():
                return 30
    except:
        return -1
    return -1

lfs = [sx_bao_bi_30, company_sx_bao_bi_30]

def get_lfs():
    return lfs 
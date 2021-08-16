#author=hanghust

from snorkel.labeling import labeling_function


@labeling_function(pre=[spacy])
def company_sx_bao_bi_30(x):
    sx_bao_bi_cn = set(['bao_bì', 'nhãn_mác'])
    if any(substring in x.company_name.split() for substring in sx_bao_bi_cn):
        return 30
    return -1

lfs = [company_sx_bao_bi_30]

def get_lfs():
    return lfs 
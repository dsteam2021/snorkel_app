#author=hanghust

from snorkel.labeling import labeling_function


@labeling_function(pre=[spacy])
def oto_xemay_38(x):
    oto_xemay = set(['honda', 'ô_tô', 'xe_máy', 'ô_tô_con', 'hyundai', 'mô_tô', 'yamaha', 'toyota', 'xe_đạp', 'wave', 'mitsubishi', 'suzuki', 'vision', 'xe_máy_điện', 'gắn_máy', 'future', 'accent',
             'santafe', 'sirius', 'ôtô', 'kia', 'ford', 'isuzu', 'tucson', 'thaco', 'espero', 'mazda', 'sym', 'exciter', 'alpha', 'winnerx', 'xpander', 'fortuner', 'sedan', 'winner'])
    if any(substring in x.name_cleaned.split() for substring in oto_xemay):
        return 38
    return -1

@labeling_function(pre=[spacy])
def company_oto_xemay_38(x):
    oto_xemay_cn = set(['ô_tô', 'xe_máy', 'hyundai', 'toyota', 'ôtô', 'xe_đạp', 'mô_tô', 'motors', 'daehan'])
    if any(substring in x.company_name.split() for substring in oto_xemay_cn):
        return 38
    return -1


lfs = [oto_xemay_38, company_oto_xemay_38]

def get_lfs():
    return lfs 
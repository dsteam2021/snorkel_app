#author=hanghust

from snorkel.labeling import labeling_function



@labeling_function()
def company_thuc_pham_34(x):
    thuc_pham_cn =  set(['thực_phẩm', 'foods', 'siêu_thị', 'chợ'])
    if any(substring in x.company_name.split() for substring in thuc_pham_cn):
        return 34
    return -1

lfs = [company_thuc_pham_34]

def get_lfs():
    return lfs 
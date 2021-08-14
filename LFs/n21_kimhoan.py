#Khiêm
@labeling_function() 
def kimhoan_0(x):
    #keywords, parttern
    keywords = ['nhẫn', 'mặt dây chuyền', 'bông tai', 'vàng', 'kim cương', 'ngọc trai', 'bảng tính']
    for each in keywords:
        if each in x['name_cleaned']:
            return 21
    return -1

@labeling_function() 
def kimhoan_1(x):
    #companyname
    keywords = ['trang sức']
    for each in keywords:
        if each in x['company_name']:
            return 21
    return -1

lfs = [kimhoan_0, kimhoan_1]

def get_lfs():
    return lfs  
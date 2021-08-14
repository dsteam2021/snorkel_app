#Khiem
@labeling_function()  
def mathanggiayda_0(x):
    #keywords, first 3
    keywords = ['áo', 'quần', 'vải', 'mũ', 'giày', 'giầy', 'váy', 'đầm', 'nón', 'thảm', 'túi']
    keywords = {each:0 for each in keywords}
    arr_words = x['name_cleaned'].split()[:3]
    for each in arr_words:
        if each in keywords:
            return 26
    return -1

@labeling_function()  
def mathanggiayda_1(x):
    #parttern
    keywords = ['ba lô', 'sơ mi', 'so mi', 'tạp dề']
    for each in keywords:
        if each in x['name_cleaned']:
            return 26
    return -1

lfs = [mathanggiayda_0, mathanggiayda_1]

def get_lfs():
    return lfs 
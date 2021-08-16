from . import *
from .util import convert


# Huy - có cả nhãn 9-(in ấn xuất bản)
@labeling_function()
def keyword_8(x):
    try:
        keyword = ['học phí', 'học kì', 'học kỳ', 'năm học', 'tiền học', 'giáo viên', 'đại học', 'giáo dục', 'đào tạo']
        for i in keyword:
            if i in x['name_cleaned']:
                if 'in' in x['check_btype'].split(): 
                    return 9 # in ấn 
                elif 'in' in x['company_name'].split():
                    return 9 # in ấn
                else:
                    return 8
    except: 
        # print(x)
        pass
    
    return -1

# Huy
@labeling_function()
def pattern_8(x):
    if re.search('[0-9][A-Z][0-9]', x['name'], flags=re.I) and x['check_btype']=='Dịch vụ giáo dục và đào tạo':
      return 8
    
    return -1

lfs = [keyword_8, pattern_8]

def get_lfs():
    return lfs
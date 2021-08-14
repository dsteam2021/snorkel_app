#Khiem
@labeling_function()
def dichvuvantai_0(x):
  #pair keywords
  key_words = ['phí', 'cước', 'nội địa']
  if "vận tải" in x['name_cleaned'] or "vận chuyển" in x['name_cleaned']:
    for each in key_words:
        if each in x['name_cleaned']:
          return 15
  return -1

@labeling_function()
def dichvuvantai_1(x):
  #keyword and check_btype
  if ('vận tải' in x['name_cleaned'] or "vận chuyển" in x['name_cleaned']) and x['check_btype'] == 'Dịch vụ vận tải và cho thuê kho bãi':
    return 15
  return -1  

lfs = [dichvuvantai_0, dichvuvantai_1]

def get_lfs():
    return lfs  
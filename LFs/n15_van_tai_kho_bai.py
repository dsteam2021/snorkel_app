from . import *


#Khiem
@labeling_function()
def dichvuvantai_0(x):
  #keywords and check_btype
  if x["check_btype"] != 'Dịch vụ vận tải và cho thuê kho bãi':
      return -1
  key_words = ['phí', 'cước', 'nội địa', 'chi phí']
  for each in key_words:
      if each in x['name_cleaned']:
        return 15
  return -1

@labeling_function()
def dichvuvantai_1(x):
  #keyword
  if ('vận tải' in x['name_cleaned'] or "vận chuyển" in x['name_cleaned']):
    return 15
  return -1  

@labeling_function()
def dichvuvantai_2(x):
  #pattern keywords
  keywords = ['vé máy bay', 'vé du lịch', 'phí thuê', "thuê xe"]
  for each in keywords:
      if each in x['name_cleaned']:
          return 15
  return -1

@labeling_function()
def dichvuvantai_3(x):
  #unit
  keywords = ['chuyến', 'cont']
  for each in keywords:
      if x['unit_clean'] == each:
          return 15
  return -1

lfs = [dichvuvantai_0, dichvuvantai_1, dichvuvantai_2, dichvuvantai_3]

def get_lfs():
    return lfs  
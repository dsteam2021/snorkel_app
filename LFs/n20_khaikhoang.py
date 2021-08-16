from . import *


#Khiêm
@labeling_function()
def khaikhoang_0(x):
  #keywords and check_btype
  if x['check_btype'] != 'Khai khoáng':
      return -1
  keywords = ['than', 'cát', 'đá', 'thạch anh']
  for each in keywords:
      if each in x['name_cleaned']:
          return 20
  return -1

@labeling_function()
def khaikhoang_1(x):
  #compname
  keywords = ['khai khoáng', 'khoáng sản']
  for each in keywords:
      if each in x['company_name']:
          return 20
  return -1

lfs = [khaikhoang_0, khaikhoang_1]

def get_lfs():
    return lfs  
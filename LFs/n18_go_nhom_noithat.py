from . import *


#Khiêm
@labeling_function()
def gonhomtbi_0(x):
  #compname
  keywords = ['gỗ', 'nhôm', 'mộc', 'nội thất']
  for each in keywords:
    if each in x['company_name']:
        return 18
  return -1

@labeling_function()
def gonhomtbi_1(x):
  #keywords and check_btype
  keywords = ['ghế', 'tủ', 'bàn', 'kệ', 'gỗ', 'giường', "nhôm", "wooden", "wood"]
  keywords = {each:0 for each in keywords}
  #if x['check_btype'] != 'Gỗ, nhôm, kính, thiết bị nội thất':
  #    return -1
  arr_words = x['name_cleaned'].split()
  for each in arr_words:
      if each in keywords:
          return 18
  return -1

@labeling_function()
def gonhomtbi_2(x):
   #pattern
   keywords = ['kệ tivi']  
   for each in keywords:
      if each in x['name_cleaned']:
          return 18
   return -1

lfs = [gonhomtbi_0, gonhomtbi_1, gonhomtbi_2]

def get_lfs():
    return lfs  
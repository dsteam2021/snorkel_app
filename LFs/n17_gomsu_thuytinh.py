from . import *


#Khiem
@labeling_function()
def gomsu_1(x):
  #company_name and keywords itemname
  keywords = ['gốm', 'sứ', 'thủy tinh']
  for each in keywords:
      if each in x['name_cleaned']:
          return 17
  if pd.isnull(x['company_name']):
      return -1
  for each in keywords:
      if each in x['company_name']:
          return 17
  return -1

@labeling_function()
def gomsu_2(x):
  #pair keywords
  keywords_1 = {"kính": -1, "bát": -1, "ly": -1, "lọ": -1, "cốc": -1, "dĩa": -1, "đĩa": -1, "tách": -1, "chén": -1, "bình": -1, "ấm": -1}
  # keywords_2 = {"gốm": -1, "sứ": -1, "thủy": -1}
  arr_words = x['name_cleaned'].split()
  for i in range(len(arr_words)):
      if arr_words[i] in keywords_1:
         return 17
  return -1

lfs = [gomsu_1, gomsu_2]

def get_lfs():
    return lfs  
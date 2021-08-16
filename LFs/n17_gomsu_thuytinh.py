from . import *


#Khiem
@labeling_function()
def gomsu_1(x):
  #company_name
  if pd.isnull(x['company_name']):
      return -1
  keywords_comp = ['gốm', 'sứ', 'thủy tinh']
  for each in keywords_comp:
      if each in x['company_name']:
        return 17
  return -1

@labeling_function()
def gomsu_2(x):
  #pair keywords
  keywords_1 = {"kính": -1, "bát": -1, "ly": -1, "lọ": -1, "cốc": -1}
  keywords_2 = {"gốm": -1, "sứ": -1, "thủy": -1}
  arr_words = x['name_cleaned'].split()
  for i in range(len(arr_words)):
      if arr_words[i] in keywords_1:
        try:
          if arr_words[i + 1] in keywords_2:
            return 17
        except:
          continue
  return -1

lfs = [gomsu_1, gomsu_2]

def get_lfs():
    return lfs  
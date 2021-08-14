#Khiem
@labeling_function()
def dichvuvesinh_0(x):
  #parttern 
  keywords = ['dịch vu vệ sinh', 'phí vệ sinh', 'thu gom']
  for each in keywords:
    if each in x['name_cleaned']:
      return 16
  return -1

@labeling_function()
def dichvuvesinh_1(x):
  #compName
  if "môi trường" in x['company_name']:
    return 16
  return -1

@labeling_function()
def dichvuvesinh_2(x):
  #pattern and check_btype
  if x['check_btype'] != 'Dịch vụ vệ sinh môi trường đô thị':
      return -1
  keywords = ['xử lý', 'rác', 'chất thải']
  for each in keywords:
      if each in x['name_cleaned']:
          return 16
  return -1

lfs = [dichvuvesinh_0, dichvuvesinh_1, dichvuvesinh_2]

def get_lfs():
    return lfs  
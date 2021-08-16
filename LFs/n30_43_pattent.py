#author=hanghust

from snorkel.labeling import labeling_function
import pandas as pd
import swifter
import ast

def convert_stringlist_to_list(s):
    return ast.literal_eval(s)

df_pair1 = pd.read_csv("LFs/Pattent_data/pair_word_apriori_1_hangnt.csv")
df_pair2 = pd.read_csv("LFs/Pattent_data/pair_word_apriori_2_hangnt.csv")
# df_pair3 = pd.read_csv("\Pattent_data\pair_word_apriori_3_hangnt.csv")

df_pair1['items'] = df_pair1['items'].swifter.apply(convert_stringlist_to_list)
df_pair2['items'] = df_pair2['items'].swifter.apply(convert_stringlist_to_list)
df_pair3['items'] = df_pair3['items'].swifter.apply(convert_stringlist_to_list)

df_pair1 = pd.concat([df_pair1, df_pair2, df_pair3], ignore_index=True)

@labeling_function()
def pattent_for_career_1(x):
    for pair_word, label in zip(df_pair1['items'], df_pair1['label_encode']):
        if set(pair_word) <= set(x.name_cleaned.split()):
            return label
    return -1

lfs = [pattent_for_career_1]

def get_lfs():
<<<<<<< HEAD
    return lfs
=======
    return lfs 
>>>>>>> labeling function for sx bao bi --> do an

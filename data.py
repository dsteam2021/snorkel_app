import os
import numpy as np
import pandas as pd

from sklearn import preprocessing

from parameter import get_args


args = get_args()

def load_data(args):
    data_path = os.path.join(args.data_path, args.file_name)
    df = pd.read_csv(data_path)

    if ('train' in args.file_name):
        le = preprocessing.LabelEncoder()
        label = le.fit_transform(df['label'].unique())

        dict_temp = {}

        for i, j in zip(df['label'].unique(), label):
            dict_temp[j] = i
        
        print(dict_temp)

    df.fillna('0', inplace=True)

    return df

# load_data(args, 'train.csv')
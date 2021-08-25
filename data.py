import os
import numpy as np
import pandas as pd

from sklearn import preprocessing

from parameter import get_args


args = get_args()

def load_data(args):
    """
    Args:
        args: 
    Return:
        df: (pd.DataFrame) data
        num_of_label: (int) number of labels
        dict_temp: (dictionary) ví dụ (keys, values): (0, "Bất động sản")
    """
    data_path = os.path.join(args.data_path, args.file_name)
    df = pd.read_csv(data_path)

    if args.num_test > 0:
        df = df[:args.num_test]

    if ('train' in args.file_name):
        le = preprocessing.LabelEncoder()
        label = le.fit_transform(df['label'].unique())

        dict_temp = {}

        for i, j in zip(df['label'].unique(), label):
            dict_temp[j] = i
        
    df.fillna('0', inplace=True)
    num_of_label = len(dict_temp.keys())

    return df, num_of_label, dict_temp

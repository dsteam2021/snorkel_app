import os
import time
import numpy as np
import pandas as pd

from pathlib import Path


def save_result(args, time, L_train, L_analyst, df):
    """
    Args:
        args:
        time: (datetime) time create folder to save result
        L_train: (np.array) L_train
        L_analyst: (pd.DataFrame) L_analyst: Polarity, Coverage, Overlap, Conflict
        df: (pd.DataFrame) data
    Return:
        None
    """
    if not os.path.isdir('result'):
        os.mkdir('result')
    time = str(time)
    if not os.path.isdir(time):
        Path('result/' + time).mkdir(parents=True)
        L_analyst.to_csv(os.path.join('result', time, 'L_analyst.csv'))
        np.save(os.path.join('result', time, 'L_train.csv'), L_train)
        df.to_csv(os.path.join('result', time, 'train_labeled.csv'), index=False)

    number_of_lfs = len(L_analyst.j)
    list_of_lfs = L_analyst.index.tolist()

    # Polarity
    empty_lfs = []
    for i, j in enumerate(L_analyst.Polarity.values):
        if (len(j) == 0):
            empty_lfs.append(list_of_lfs[i])

    # Coverage
    coverage = L_analyst.Coverage.sum()

    print('-' * 100)
    print('Empty LFs: {}'.format(empty_lfs))
    print('Coverage:  {}'.format(coverage))


def plot_overlap(args, time, df: pd.DataFrame, L_train, L_analyst, dict_temp):
    """
    Args:
        args: 
        time: (string) datetime create file
        df: (pd.DataFrame) data
        L_train: (np.array) L_train
        L_analyst: (pd.DataFrame) L_analyst: Polarity, Coverage, Overlap, Conflict
        dict_temp: (dictionary) ví dụ (keys, values): (0, "Bất động sản")
    Return:
        None
    """
    if not os.path.exists(os.path.join('result', time)):
        if not os.path.exists('result'):
            os.mkdir('result')
        os.mkdir(os.path.join('result', time))

    f = open(os.path.join('result', time, 'overlap.txt'), 'a')

    list_of_lfs = L_analyst.index.tolist()
    for index, y in enumerate(L_train):
        overlap_label = (np.unique(y[y > 0]))
        if len(overlap_label) > 1:
            f.write(df.iloc[index]['name'] + '----' + df.iloc[index]['label'] + '\n')
            for j, label in enumerate(y):
                if label > 0: f.write('LFs : {}, Label: {}\n'.format(list_of_lfs[j], dict_temp[label]))
            f.write('*' * 100 + '\n')
    
    f.close()
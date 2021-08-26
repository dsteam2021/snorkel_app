import os
import time
import json
import numpy as np
import pandas as pd

from pathlib import Path


def save_result(args, time, L_train, L_analyst, df, y_preds, dict_temp):
    """
    Args:
        args:
        time: (datetime) time create folder to save result
        L_train: (np.array) L_train
        L_analyst: (pd.DataFrame) L_analyst: Polarity, Coverage, Overlap, Conflict
        df: (pd.DataFrame) data
        y_preds: y_preds: (np.array) predicted output by Snorkel after get L_train, has shape (data point, )
        dict_temp: 
    Return:
        df: (pd.DataFrame) data + predicted output 
    """
    if not os.path.isdir('result'):
        os.mkdir('result')
    time = str(time)
    if not os.path.isdir(time):
        Path('result/' + time).mkdir(parents=True)
        L_analyst.to_csv(os.path.join('result', time, 'L_analyst.csv'))
        np.save(os.path.join('result', time, 'L_train.csv'), L_train)

        dict_temp[-1] = 'Unknow'
        df['label_snorkel'] = y_preds
        df['label_snorkel'] = df['label_snorkel'].apply(lambda x: dict_temp[x])
        df.to_csv(os.path.join('result', time, 'train_labeled.csv'), index=False)

    number_of_lfs = len(L_analyst.j)
    list_of_lfs = L_analyst.index.tolist()

    # Polarity
    empty_lfs = []
    for i, j in enumerate(L_analyst.Polarity.values):
        if (len(j) == 0):
            empty_lfs.append(list_of_lfs[i])

    print('-' * 100)
    print('Empty LFs: {}, over {} lfs, empty {:.2f} %'.format(empty_lfs, number_of_lfs, len(empty_lfs) / number_of_lfs))

    return df


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
        Path(os.path.join('result', time)).mkdir(parents=True)

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


def plot_result(args, time, df: pd.DataFrame, dict_temp):
    """
    Args:
        args:
        time: (String) datetime create file
        df: (pd.DataFrame) data
        dict_temp: (dictionary) ví dụ (keys, values): (0, "Bất động sản")
    Return:
        None
    """
    # df_temp: data point labeled by Snorkel
    df_temp = df[df['label_snorkel'] != 'Unknow']

    # 'Unknow': unlabeled data
    coverage = len(df[df['label_snorkel'] != 'Unknow']) / len(df) * 100
    accuracy_1 = len(df[df['label_snorkel'] == df['label']]) / len(df) * 100
    accuracy_2 = len(df_temp[df_temp['label_snorkel'] == df_temp['label']]) / len(df_temp) * 100

    print('Coverage:                    {:.2f} %'.format(coverage))
    print('Accuracy over all dataset:   {:.2f} %'.format(accuracy_1))
    print('Accuracy over all labeled:   {:.2f} %'.format(accuracy_2))

    if not os.path.exists(os.path.join('result', time)):
        if not os.path.exists('result'):
            os.mkdir('result')
        Path(os.path.join('result', time)).mkdir(parents=True)

    f = open(os.path.join('result', time, 'result.txt'), 'a')

    f.write('Coverage:                    {:.2f} %\n'.format(coverage))
    f.write('Accuracy over all dataset:   {:.2f} %\n'.format(accuracy_1))
    f.write('Accuracy over all labeled:   {:.2f} %\n'.format(accuracy_2))
    f.write('*' * 100)

    for i in dict_temp.keys():
        if i == -1:
            continue
        f.write('{}:\n'.format(dict_temp[i]))
        # df_temp: data point labeled by Snorkel
        df_labeled = df[df['label'] == dict_temp[i]]

        # 'Unknow': unlabeled data
        coverage = len(df_labeled[df_labeled['label_snorkel'] != 'Unknow']) / len(df_labeled) * 100
        accuracy = len(df_labeled[df_labeled['label_snorkel'] == dict_temp[i]]) / len(df_labeled) * 100

        df_temp = df_labeled[df_labeled['label_snorkel'] != 'Unknow']
        conflict = len(df_temp[df_temp['label_snorkel'] != dict_temp[i]]) / len(df_labeled) * 100

        f.write('\tCoverage:            {:.2f} %\n'.format(coverage))
        f.write('\tAccuracy:            {:.2f} %\n'.format(accuracy))
        f.write('\tConflict:            {:.2f} %\n'.format(conflict))
        f.write('\n')

    f.close()

    
def get_result(df):
    list_unique = df['label'].unique()
    list_unique = {each:{"match": 0, "total": 0, "error": {}} for each in list_unique}
    def getMatch(lb, lb_snor):
        list_unique[lb]['total'] += 1
        if lb == lb_snor:
            list_unique[lb]['match'] += 1
        else:
            if lb_snor not in list_unique[lb]['error']:
                list_unique[lb]['error'][lb_snor] = 0
            list_unique[lb]['error'][lb_snor] += 1
    np.vectorize(getMatch)(df['label'], df['label_snorkel'])
    if not os.path.isdir('result'):
        os.mkdir('result')
    with open('result/result.json', 'w', encoding='utf8') as fp:
         json.dump(list_unique, fp, ensure_ascii=False)
    return

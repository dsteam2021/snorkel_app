import os
import time
import numpy as np
import pandas as pd

from pathlib import Path


def save_result(time, L_train, L_analyst, df):
    if not os.path.isdir('result'):
        os.mkdir('result')
    time = str(time)
    if not os.path.isdir(time):
        Path('result/' + time).mkdir(parents=True)
        L_analyst.to_csv(os.path.join('result', time, 'L_analyst.csv'))
        np.save(os.path.join('result', time, 'L_train.csv'), L_train)
        df.to_csv(os.path.join('result', time, 'train_labeled.csv'), index=False)
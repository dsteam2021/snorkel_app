import os
import regex as re
import numpy as np
import pandas as pd

from unidecode import unidecode
from snorkel.labeling.model import LabelModel
from snorkel.labeling import labeling_function, PandasLFApplier, LFAnalysis
from snorkel.labeling.apply.dask import PandasParallelLFApplier

lfs = []
# n0_bat_dong_san.py -> n0_bat_dong_san
# lọc các file lfs để auto import
list_lfs = [i.split('.')[0] for i in os.listdir('LFs') if (i != 'util.py' and i[0] != '_' and i.split('.')[-1] == 'py')]
for i in list_lfs:
    file_lfs = __import__('LFs.' + i, fromlist=['get_lfs'])
    lfs.extend(file_lfs.get_lfs())
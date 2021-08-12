import os
import regex as re
import numpy as np
import pandas as pd

from unidecode import unidecode


def convert(keyword):
    '''
    Args:
        keyword: danh sách các từ keyword
    Return:
        (list): list các từ keyword không dấu
    '''
    temp = []
    for i in keyword:
        temp.append(unidecode(i))

    return temp
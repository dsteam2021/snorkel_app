import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_path', type=str, default='data/')
    parser.add_argument('--file_name', type=str, default='train.csv')

    args = parser.parse_args()

    return args
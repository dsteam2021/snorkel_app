import argparse


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_path', type=str, default='data/')

    args = parser.parse_args()

    return args
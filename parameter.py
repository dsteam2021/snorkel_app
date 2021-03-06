import argparse


def get_args():
    parser = argparse.ArgumentParser()

    # Load data
    parser.add_argument('--data_path', type=str, default='data/', help='folder data')
    parser.add_argument('--file_name', type=str, default='train.csv', help='file name data')
    parser.add_argument('--num_test', type=int, default=-1, help='numer of data point to test')

    # L_train
    parser.add_argument('--core', type=int, default=6, help='core to run parallel')

    # Snorkel
    parser.add_argument('--major_vote', action='store_true', help='Majority Vote Snorkel')
    parser.add_argument('--label_model', action='store_true', help='Label Model Snorkel')

    ## Label model
    parser.add_argument('--epoch', type=int, default=100, help='epoch to train label model')
    parser.add_argument('--seed', type=int, default=42, help='seed for recon result')

    args = parser.parse_args()

    return args

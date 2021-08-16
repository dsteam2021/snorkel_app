import argparse


def get_args():
    parser = argparse.ArgumentParser()

    # Load data
    parser.add_argument('--data_path', type=str, default='data/')
    parser.add_argument('--file_name', type=str, default='train.csv')

    # Snorkel
    parser.add_argument('--major_vote', action='store_true', help='Majority Vote Snorkel')
    parser.add_argument('--label_model', action='store_true', help='Label Model Snorkel')

    args = parser.parse_args()

    return args
import os
import time
import datetime
date = str(datetime.datetime.now())

from LFs import *
from LFs import lfs
from data import load_data
from util import get_result, save_result, plot_overlap
from parameter import get_args

from snorkel.labeling.model import LabelModel
from snorkel.labeling.model import MajorityLabelVoter


if __name__ == "__main__":
    def get_L(args, df, lfs):
        """
        Args:
            args:
            df: (pd.DataFrame) data
            lfs: (list) list labeling function get from LFS/__init__.py
        Return:
            L_train: (np.array) output of labeling function, has shape (n, m): (data point, number labeling functions)
            L_analyst: (pd.DataFrame) 
        """
        if args.core == 1: 
            # lfs: List  các labeling function ở LFs
            applier = PandasLFApplier(lfs=lfs)
            L_train = applier.apply(df=df)
        elif args.core > 1: 
            applier = PandasParallelLFApplier(lfs)
            L_train = applier.apply(df=df, n_parallel=args.core)

        L_analyst = LFAnalysis(L=L_train, lfs=lfs).lf_summary()

        return L_train, L_analyst
    
    def get_label(args, num_of_label, L_train):
        """
        Args:
            args:
            num_of_label: (int) number labels
            L_train: (np.array) output of labeling function, has shape (n, m): (data point, number labeling functions)
        Return:
            y_preds: (np.array) predicted output by Snorkel after get L_train, has shape (data point, )
        """
        # Dùng major vote hoặc label_model để tìm nhãn
        if args.major_vote:
            majority_model = MajorityLabelVoter()
            y_preds = majority_model.predict(L=L_train)
        elif args.label_model:
            label_model = LabelModel(cardinality=num_of_label, verbose=True)
            label_model.fit(L_train=L_train, n_epochs=args.epoch, log_freq=100, seed=args.seed)
            y_preds = label_model.predict(L=L_train)
        else:
            label_model = LabelModel(cardinality=num_of_label, verbose=True)
            label_model.fit(L_train=L_train, n_epochs=args.epoch, log_freq=100, seed=args.seed)
            y_preds = label_model.predict(L=L_train)

        return y_preds
    
    args = get_args()
    start = time.time()

    df, num_of_label, dict_temp = load_data(args)

    L_train, L_analyst = get_L(args, df, lfs)
    
    y_preds = get_label(args, num_of_label, L_train)

    print("Time consuming: {}".format(time.time() - start))

    # get_result(df)
    df_new = save_result(args, date, L_train, L_analyst, df, y_preds, dict_temp)
    plot_overlap(args, date, df, L_train, L_analyst, dict_temp)

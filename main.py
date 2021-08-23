import os
import time
import datetime
date = str(datetime.datetime.now())

from LFs import *
from LFs import lfs
from data import load_data
from util import save_result, plot_overlap
from parameter import get_args

from snorkel.labeling.model import LabelModel
from snorkel.labeling.model import MajorityLabelVoter


def get_L(args, df, lfs):
    if args.core == 1: 
        # lfs: List  các labeling function ở LFs
        applier = PandasLFApplier(lfs=lfs) 
    elif args.core > 1: 
        applier = PandasParallelLFApplier(lfs, n_parallel=args.core)
        
    L_train = applier.apply(df=df)
    L_analyst = LFAnalysis(L=L_train, lfs=lfs).lf_summary()

    return L_train, L_analyst


def get_label(args, num_of_label, L_train):
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


if __name__ == "__main__":
    args = get_args()
    start = time.time()

    df, num_of_label, dict_temp = load_data(args)

    L_train, L_analyst = get_L(args, df, lfs)
    
    y_preds = get_label(args, num_of_label, L_train)

    df['label_snorkel'] = y_preds

    print("Time consuming: {}".format(time.time() - start))

    save_result(args, date, L_train, L_analyst, df)
    plot_overlap(args, date, df, L_train, L_analyst, dict_temp)

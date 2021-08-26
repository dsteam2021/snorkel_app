import os
import sys
import time
import datetime
date = str(datetime.datetime.now())

from LFs import *
from LFs import lfs
from data import load_data
from util import get_result, save_result, plot_overlap, plot_result
from parameter import get_args

from snorkel.labeling.model import LabelModel
from snorkel.labeling.model import MajorityLabelVoter


if __name__ == "__main__":
    args = get_args()
    start = time.time()
    
    df, num_of_label, dict_temp = load_data(args)
    
    print('Num of label: {}'.format(num_of_label))

    # sys.exit()

    if args.core == 1: 
        # lfs: List  các labeling function ở LFs
        applier = PandasLFApplier(lfs=lfs)
        L_train = applier.apply(df=df)
    elif args.core > 1: 
        applier = PandasParallelLFApplier(lfs)
        L_train = applier.apply(df=df, n_parallel=args.core)

    L_analyst = LFAnalysis(L=L_train, lfs=lfs).lf_summary()
    
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

    print("Time consuming: {}".format(time.time() - start))

    # get_result(df)
    df_new = save_result(args, date, L_train, L_analyst, df, y_preds, dict_temp)
    plot_overlap(args, date, df, L_train, L_analyst, dict_temp)
    plot_result(args, date, df_new, dict_temp)

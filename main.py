import os
import time
import datetime
date = datetime.datetime.now()


from LFs import *
from util import *
from data import load_data
from parameter import get_args

from snorkel.labeling.model import LabelModel
from snorkel.labeling.model import MajorityLabelVoter


if __name__ == "__main__":
    args = get_args()
    start = time.time()

    df, num_of_label = load_data(args)

    # lfs: List  các labeling function ở LFs
    applier = PandasLFApplier(lfs=lfs) 
    # applier = PandasParallelLFApplier(lfs)
    L_train = applier.apply(df=df)
    L_analyst = LFAnalysis(L=L_train, lfs=lfs).lf_summary()
    
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

    df['label_snorkel'] = y_preds

    print(time.time() - start)

    save_result(date, L_train, L_analyst, df)
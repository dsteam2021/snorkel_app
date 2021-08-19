import os
import time

from LFs import *
from util import *
from data import load_data
from parameter import get_args

if __name__ == "__main__":
    args = get_args()
    start = time.time()

    df, num_of_label = load_data(args)

    # lfs: List  các labeling function ở LFs
    applier = PandasLFApplier(lfs=lfs) 
    # applier = PandasParallelLFApplier(lfs)
    L_train = applier.apply(df=df)
    L_analyst = LFAnalysis(L=L_train, lfs=lfs).lf_summary()
    
    label_model = LabelModel(cardinality=num_of_label, verbose=True)
    label_model.fit(L_train=L_train, n_epochs=100, log_freq=100, seed=42)

    y_preds = label_model.predict(L=L_train)
    df['label_snorkel'] = y_preds

    print(time.time() - start)

    save_result(start, L_train, L_analyst, df)
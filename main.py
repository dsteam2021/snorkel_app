import os

from LFs import *
from data import load_data
from parameter import get_args


if __name__ == "__main__":
    args = get_args()

    # lfs: List  các labeling function ở LFs
    applier = PandasLFApplier(lfs=lfs) 
    L_train = applier.apply(df=load_data(args), progress_bar=True)

    L_analyst = LFAnalysis(L=L_train, lfs=lfs).lf_summary()
    print(L_analyst)
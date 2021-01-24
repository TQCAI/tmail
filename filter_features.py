#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Date    : 2021-01-24
# @Contact    : qichun.tang@bupt.edu.cn
import numpy as np
import pandas as pd
from boruta import BorutaPy
from sklearn.ensemble import ExtraTreesClassifier
from joblib import dump

boruta = BorutaPy(
    ExtraTreesClassifier(max_depth=5, n_jobs=4),
    n_estimators='auto', max_iter=30, random_state=0, verbose=2)

train = pd.read_pickle('data/train.pkl')
train.fillna(0, inplace=True)
train[np.isinf(train)] = 0
y = train.pop('label')
boruta.fit(train, y)
dump(boruta, 'data/boruta.pkl')
print(boruta)

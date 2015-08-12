# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

df = pd.read_csv('../data/rollingsales_manhattan_processed.csv',encoding='utf-8')

df = df.as_matrix()
dfTrain, dfTest = train_test_split(df, test_size=0.2)

# X is are the sales price (training data)
#df_X_train = dfTrain[:,5:6]
#df_X_test = dfTest[:,5:6

# X is are all the variables except neighborhood (training data)
df_X_train = dfTrain[:,2:3]
df_X_test = dfTest[:,2:3]

# y is the neighborhood (target data)
df_y_train = dfTrain[:,7:8]
df_y_test = dfTest[:,7:8]

kNN = KNeighborsClassifier(n_neighbors=3)
kNN.fit(df_X_train, df_y_train)


for k in range(1,20):
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(df_X_train, df_y_train)
    # make predictions
    expected = df_y_test
    predicted = kNN.predict(df_X_test)
    # misclassification rate
    error_rate = (predicted != expected).mean()
    print('%d:, %.2f' % (k, error_rate))
    
    
    

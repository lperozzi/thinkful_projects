# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn_pandas import DataFrameMapper, cross_val_score
import sklearn.preprocessing, sklearn.decomposition, sklearn.linear_model, sklearn.pipeline, sklearn.metrics

df = pd.read_csv('data/rollingsales_manhattan_processed.csv',encoding='utf-8')

# categorical value to binaries values
mapper = DataFrameMapper([('TAX CLASS AT PRESENT', sklearn.preprocessing.LabelBinarizer()), # column 0:5
                          ('BUILDING CLASS AT PRESENT', sklearn.preprocessing.LabelBinarizer()), # column 5:98
                          ('TOTAL UNITS', None), # column 98:99
                          ('SALE PRICE', None), # column 99:100
                          ('NEIGHBORHOOD', None), # column 100:101
                          ('RESIDENTIAL UNITS', None), # column 101:102
                        ])

df = mapper.fit_transform(df.copy())

# transform to a matrix
#df = df.as_matrix()
# split the data set into training data (80%) and tets data(20%)
dfTrain, dfTest = train_test_split(df, test_size=0.2)

# X is TAX CLASS AT PRESENT (training data)
#df_X_train = dfTrain[:,0:5]
#df_X_test = dfTest[:,0:5]

# X is BUILDING CLASS AT PRESENT (training data)
#df_X_train = dfTrain[:,5:98]
#df_X_test = dfTest[:,5:98]

# X is TOTAL UNITS (training data)
#df_X_train = dfTrain[:,98:99]
#df_X_test = dfTest[:,98:99]

# X is RESIDENTIAL UNITS (training data)
df_X_train = dfTrain[:,101:102]
df_X_test = dfTest[:,101:102]

# X is SALE PRICE (training data)
#df_X_train = dfTrain[:,99:100]
#df_X_test = dfTest[:,99:100]
#
# X is all variables together (training data)
#df_X_train = dfTrain[:,0:100]
#df_X_test = dfTest[:,0:100]

# y is the neighborhood (target data)
df_y_train = dfTrain[:,100:101]
df_y_test = dfTest[:,100:101]

# make the classification
kNN = KNeighborsClassifier(n_neighbors=3)
kNN.fit(df_X_train, df_y_train)

# testing the prediction error_rate for k varying form 1 to 30
for k in range(1,30):
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(df_X_train, df_y_train)
    # make predictions
    expected = df_y_test
    predicted = kNN.predict(df_X_test)
    # accuracy_score
    print('%d:, %.2f' % (k, accuracy_score(expected,predicted)))
    


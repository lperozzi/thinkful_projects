# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:11:48 2015

@author: lorenzoperozzi
"""
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

filename = "data/images.csv"
df = pd.read_csv(filename)

# We want to predict if the image is landscape. 
df['landscape'] = df['image'] == 'landscape' # 

# Split in train-test sets
df_train, df_test = train_test_split(df, test_size = 0.2, random_state=0)

min_misclassification = 1.0
min_k = 1
indep_col = ["r_1","r_2","r_3","r_4","r_5","g_1","g_2","g_3","g_4","g_5","b_1","b_2","b_3","b_4","b_5"]
label_col = ["landscape"]
for k in range(1,20):
    model = KNeighborsClassifier(n_neighbors=k) # using euclidean distance
    model.fit(df_train[indep_col], df_train[label_col])
    misclassification = ( model.predict(df_test[indep_col]) != df_test[label_col].as_matrix() ).mean()
    print 'k = {0} has misclassification error {1:.5f}'.format(k, misclassification)
    if misclassification < min_misclassification:
        min_misclassification = misclassification
        min_k = k

print "The minimum misclassification in train set is obtained for k={0}".format(min_k)
# -*- coding: utf-8 -*-
# where: https://courses.thinkful.com/data-001v2/assignment/4.1.5
# why : training and test sets
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split


# 1st method to create a dataframe
age = np.array([69,66,49,49,58,44])
income = np.array([3,57,79,17,26,71])
credit = ['low','low','low','low','high','high']

data = {"age":age, "income":income, "credit":credit}
df = pd.DataFrame(data)

print df

# second method to create a dataframe
df2 = pd.DataFrame.from_items([('age', [69,66,49,49,58,44]), ('income', [3,57,79,17,26,71]),('credit',['low','low','low','low','high','high'])])

print df2

# Question: Why the first method print me income column after credit column????
print('Question: Why the first method print me income column after credit column????')
print('')
print('')
print('')

# training phase
dfTrain, dfTest = train_test_split(df, test_size=0.2)
# this is the subset of labels for the training set
cl = dfTrain[:,2]
# But this give  me an error


# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel('../data/rollingsales_manhattan.xls',skiprows=4)

# selcting only entry that honor these conditions
df = df.loc[(df["TOTAL UNITS"] != 0) & (df["LAND SQUARE FEET"] != 0) & 
             (df["GROSS SQUARE FEET"] != 0) & (df["SALE PRICE"] != 0)]

# dropping columns that are not interesting
df.drop(['BOROUGH','BLOCK','LOT','EASE-MENT','APARTMENT NUMBER'],
             inplace=True, axis=1)


# plotting scatter_matrix of all values
pd.scatter_matrix(df)
plt.show()

print '''Sales price seems to be correlated with gross square meters and # of 
       total units'''
      
      
df.to_csv('../data/rollingsales_manhattan_processed.csv',encoding='utf-8')
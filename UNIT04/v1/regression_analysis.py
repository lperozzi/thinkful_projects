# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('data/rollingsales_manhattan_processed.csv',encoding='utf-8')


# replacing column name blank space with underscore to use in statsmodel formula
cols = df.columns
cols = cols.map(lambda x: x.replace(' ', '_') if isinstance(x, (str, unicode)) else x)
df.columns = cols


# starting regression analysis using linear OLS
model = smf.ols(formula="GROSS_SQUARE_FEET ~ SALE_PRICE", data=df) 
fitted_model = model.fit()
coeffs = fitted_model.params
print fitted_model.summary()
print "The model obtained is y = {0} + {1}*x".format(*coeffs)

# model prediction
model_grosssquarefeet = fitted_model.predict(df[['SALE_PRICE']]) # pay attention to the argument format

# Plot the data. What type is it? What should we expect from it?
plt.plot(df["SALE_PRICE"]/1000000., df["GROSS_SQUARE_FEET"]/1000., 's')
plt.plot(df['SALE_PRICE']/1000000., model_grosssquarefeet/1000., 'or', label='Model fitted to data')
plt.xlabel("SALES PRICE (in milion of $)")
plt.ylabel("GROSS SQUARE FEET (in thousand of feet)")
#plt.xscale('log')
#plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()


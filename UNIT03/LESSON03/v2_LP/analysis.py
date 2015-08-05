# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:55:31 2015

@author: lorenzoperozzi
"""

#  ## Plotting and analysis 

# In[29]:

# Plotting scatterplot with and without logarithmic x axes as weel histograms of all variables to analyzing distributions
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import formula form statsmodel
import statsmodels.formula.api as smf

merged_df = pd.read_csv('data/merged.csv', encoding = 'utf-8')
school_df = pd.read_csv('data/school.csv', encoding = 'utf-8')
#merged_df['GDP'] = merged_df['GDP']/10000000.

men = school_df.men.describe()
women = school_df.women.describe()
total = school_df.total.describe()


# Histogram of distribution (men, women, total)
fig = plt.figure()
ax = plt.gca()
ax.hist(merged_df['total'])
ax.set_xlabel('total')
ax.set_ylabel('frequency')
ax.set_title('histogram for total school exp life')
plt.show()

print "The median expectancy total school life is {0:.2f} years".format(total['50%'])

fig = plt.figure()
ax = plt.gca()
ax.hist(merged_df['men'])
ax.set_xlabel('men')
ax.set_ylabel('frequency')
ax.set_title('histogram for men school exp life')
plt.show()

print "The median expectancy school life for men is {0:.2f} years".format(men['50%'])


fig = plt.figure()
ax = plt.gca()
ax.hist(merged_df['women'])
ax.set_xlabel('women')
ax.set_ylabel('frequency')
ax.set_title('histogram for women school exp life')
plt.show()

print "The median expectancy school life for women is {0:.2f} years".format(women['50%'])



# Note: merged_df has only 147 entry vs school_df that has 183 entry. 
# this changes the values of the mean, median and standard deviation

# Scatter plot GDP vs scholl life expectancy (men, women, total)

#school_life_exp = merged_df['total'] # for total
school_life_exp = merged_df['men']  # for men
#school_life_exp = merged_df['women'] # for women

# linear x and y scale
fig = plt.figure()
ax = plt.gca()
ax.scatter(merged_df['GDP'],school_life_exp)
ax.set_xlabel('GDP')
ax.set_ylabel('men')
ax.set_title('Linear x and y scale')
plt.show()

# log x scale and linear y scale
fig = plt.figure()
ax = plt.gca()
ax.scatter(merged_df['GDP'],school_life_exp)
#ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('GDP')
ax.set_ylabel('men')
ax.set_title('Log x and linear y scale')
plt.show()

# log x and y scale
fig = plt.figure()
ax = plt.gca()
ax.scatter(merged_df['GDP'],school_life_exp)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel('GDP')
ax.set_ylabel('men')
ax.set_title('Log x - log y scale')
plt.show()



# Doing some analysis, fit a model
# Ordinary Least Squares = Linear Regression
# 
model = smf.ols(formula="men ~ np.log(GDP)", data=merged_df) # choose total, men or women

fitted_model = model.fit()
corr = fitted_model.rsquared_adj
coeffs = fitted_model.params
print fitted_model.summary()
print "The correlation between GDP and expectancy is only  of {0:.2f}".format(corr)
print "The model obtained is y = {0} + {1}*x".format(*coeffs)

# model prediction
school_life_model = fitted_model.predict(merged_df[['GDP']]) # pay attention to the argument format

# Plotting results
fig = plt.figure()
ax = plt.gca()
# Plotting the data
ax.scatter(merged_df['GDP'],school_life_exp)
# plotting the prediciton model: linear sx and y cale
ax.plot(merged_df['GDP'], school_life_model, 'r', label='Model fitted to data')
ax.set_xlabel('GDP')
ax.set_ylabel('men')
ax.set_title('Linear x and y scale')
plt.show()

fig = plt.figure()
ax = plt.gca()
# Plotting the data
ax.scatter(merged_df['GDP'],school_life_exp)
# plotting the prediciton model: log x scale, linear y scale
ax.plot(merged_df['GDP'], school_life_model, 'r', label='Model fitted to data')
ax.set_xlabel('GDP')
ax.set_ylabel('men')
ax.set_title('Linear x and y scale')
ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()

fig = plt.figure()
ax = plt.gca()
# Plotting the data
ax.scatter(merged_df['GDP'],school_life_exp)
# plotting the prediciton model: log x and y scale
ax.plot(merged_df['GDP'], school_life_model, 'r', label='Model fitted to data')
ax.set_xlabel('GDP')
ax.set_ylabel('men')
ax.set_title('Linear x and y scale')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

# My question is: I'm not sure that it is the right way to do analysis. Can
# we plot predicition made on log axis  (men ~ log(GDP)) on data that are plotted 
# with different axis scale? My guess is no, but how to make a good prediction for 
# log(x) - log(y) scale (see analysis below)

model = smf.ols(formula="np.log(men) ~ np.log(GDP)", data=merged_df) # choose total, men or women

fitted_model = model.fit()
corr = fitted_model.rsquared_adj
coeffs = fitted_model.params
print fitted_model.summary()
print "The correlation between GDP and expectancy is only  of {0:.2f}".format(corr)
print "The model obtained is y = {0} + {1}*x".format(*coeffs)

# model prediction
school_life_model = fitted_model.predict(merged_df[['GDP']]) # pay attention to the argument format

# Plotting results
fig = plt.figure()
ax = plt.gca()
# Plotting the data
ax.scatter(merged_df['GDP'],school_life_exp)
# plotting the prediciton model: log x and y scale
ax.plot(merged_df['GDP'], school_life_model, 'r', label='Model fitted to data')
ax.set_xlabel('GDP')
ax.set_ylabel('men')
ax.set_title('Linear x and y scale')
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()


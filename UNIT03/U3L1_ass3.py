# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:38:32 2015

@author: lorenzoperozzi
"""
# Why: Clean city Data bike
# Where: https://courses.thinkful.com/data-001v2/assignment/3.1.3

#--------------------------------------------------------------- PREP. DATA ----

import requests
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

r = requests.get('http://www.citibikenyc.com/stations/json')

# Append keys of json file into a list
key_list = [] 
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)

# create dataframe  
df = json_normalize(r.json()['stationBeanList'])

#--------------------------------------------------------- EXPLORING. DATA ----
# available Bikes histogram 
df['availableBikes'].hist()
df['availableBikes'].describe()

# total Docks histogram
df['totalDocks'].hist()
df['totalDocks'].describe()

# Notice how the distributions differ. Why might that be? #

# The most of the station have between 20 and 50 totalDocks (mean of 34). 
# If we look at the availableBikes histogram, the median is 7 bikes. T
# hat means there are more totalDocks than availabeBikes. This is obvious as 
# the programs aims to maximise/optimize the ratio between used bike and 
# available bikes (i.e., there is no sense to have too much availableBikes 
# and it is important to have enough availableDocks)

#--------------------------------------------------------------- CHALLENGE ----

# Question 1. Explore the other data variables.# 
# Are there any test stations? #

# Check dtype of each column
df.dtypes
# As the testStation variable is boolean I can simply check how many True 
# this variable has
pd.value_counts(df.testStation)
# All the testStation value return False, ther are no test station!


# How many stations are "in Service"? How many are "Not In Service"? #

pd.value_counts(df.statusValue)

# Any other interesting variables values that need to be accounted for? #

# The longitude and latitude could be interesting to see if there are map area 
# that are most in demand of bike. As well it will be important to monitor that 
# stations have availableDocks.

# Question 2. What is the mean number of bikes in a dock? What is the median?.# 
# Are there any test stations? #

df['totalDocks'].describe()
# The number of bikes in a dock correspond to the number of totalDocks. 
# The mean is almost 34 and the median is 33.

# How does this change if we remove the stations that aren't in service? #

in_service=df[(df.statusValue == 'In Service')]
in_service.totalDocks.describe()
# The mean is almst 35, the median increased of 1 to 34
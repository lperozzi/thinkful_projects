# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:56:39 2015

@author: lorenzoperozzi
"""

#  ## Using SQLite to store data and create the new table for analysis 
#  ####Why : Storing the data
#  
#  ####Where : https://courses.thinkful.com/data-001v2/assignment/3.3.3

# In[12]:

# Why : Storing the data
# Where : https://courses.thinkful.com/data-001v2/assignment/3.3.3

# I do have a dataframe already, I do not need a sql table creation.
# men = school_df.men.describe()
# women = school_df.women.describe()

# print(school_df.describe())
 
import sqlite3
import pandas as pd

school_df = pd.read_csv('data/school.csv', encoding = 'utf-8')
gdp_df = pd.read_csv('data/gdp.csv',encoding = 'utf-8')
# create and connect to a database
conn = sqlite3.connect('education.db')

# All interactions with the database are called querys
# And they require to be used through a cursor
c = conn.cursor()
# The queries are applied using the .execute() method
c.execute('DROP TABLE IF EXISTS school')
c.execute('DROP TABLE IF EXISTS gdp')
# Create a new table called school from pandas dataframe
school_df.to_sql('school', conn)
# Create a new table called gdp from pandas dataframe
gdp_df.to_sql('gdp', conn)

# Retrieve data merged in SQLITE (school table merged in SQLite with gdp table in order to keep only the GDP value 
# corresponding to the year of school expectancy)

merged_df = pd.read_sql_query('''SELECT school.country, gdp.year, gdp.GDP, total, men, women 
                FROM gdp 
                INNER JOIN school 
                ON gdp.year=school.year AND gdp.country=school.country;''',conn)
                
# save merged to csv
merged_df.to_csv('data/merged.csv',encoding='utf-8')
                

####### Comment LP ########
# I do not really have idea to how adjust automaticlly the countries that do not match.
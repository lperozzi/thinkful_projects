
# coding: utf-8

# ## Unit 03 Lesson 03
# ####Why : Do Welthier countries provide better education?
# ####Where : https://courses.thinkful.com/data-001v2/lesson/3.3


from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL with data
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

# Getting data from the web and storing for soup analysis
r = requests.get(url)
soup = BeautifulSoup(r.content)


# In[9]:

data = []
# I only consider the 7th table 
table = soup.findAll('table')[6]
# I take only the 2nd table within the table where I have data I want
table = table.findAll('table')[1]

rows = table.findAll('tr')
for row in rows:
    # Iterate over column. This scripte take account for blank space too
    cols = row.find_all('td')
    # This allow me to remove all the tag between <>
    cols = [ele.text.rstrip() for ele in cols]
    data.append([ele for ele in cols]) 

# drop first 6 row
data = data[5::]
# I obtain a list of of list with 12 elements each, blank spaces 
# included.

# Dataframe creation
col = ['country','year','','','total','','','men','','','women','']
school_df = pd.DataFrame(data,columns=col)
# Drop blank column
school_df.drop('', axis=1, inplace=True)
# Transform string to int
school_df.year = school_df['year'].apply(int)
school_df.total = school_df['total'].apply(int)
school_df.men = school_df['men'].apply(int)
school_df.women = school_df['women'].apply(int)
school_df = school_df.set_index('country')
# save school to csv
school_df.to_csv('data/school.csv',encoding='utf-8')

# ## Create a gdp dataframe for years 1999 to 2010
# Starting from world bank .csv data, extract data for GDP for each country, in year range 1999 to 2010 in order to compare the GDP value with the school expectancy.

# In[33]:

# Why : Compare GDP to Educational Attainment
# Where : https://courses.thinkful.com/data-001v2/project/3.3.4

# Read the csv data (skip the first 2 rows)
gdp_df_row = pd.read_csv('world bank data/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv',skiprows=2)
# Make a first dataframe for only Country name to indicator name column
gdp_df1 = gdp_df_row.ix[:, 'Country Name']
# Make a first dataframe for only years 1999 to 2010 (as the school life expectancy dataframe (school_df))
gdp_df2 = gdp_df_row.ix[:, '1999':'2010']
#  concatenate the two dataframe to create a unique dataframe
gdp_df = pd.concat([gdp_df1, gdp_df2], axis=1)
# rename the column 'Country Name' in 'country' to match the school_df
gdp_df = gdp_df.rename(columns = {'Country Name':'country'})


# Now gdp_df is a dataframe with following columns: country | 1999 | 2000 | ... | 2010 , where for each year we have a GDP value. I need to reshape the dataframe in order to have 3 columns: Country | Year | GDP to make analysis with the schhol_df.

# In[ ]:

# reshape the dataframe (using stack fonction) in order to have 3 columns (Year | GDP | Country)
id = gdp_df.ix[:, ['country']]
gdp_df = pd.merge(gdp_df.stack(0).reset_index(1), id, left_index=True, right_index=True)
gdp_df.columns = ['year','GDP','country']
# delete first line of each country
gdp_df = gdp_df[gdp_df.year != 'country']

gdp_df = gdp_df.set_index('country')
# Transform string to int
gdp_df.year = gdp_df['year'].apply(int)
gdp_df.GDP = gdp_df['GDP'].apply(int)
# save gdp to csv
gdp_df.to_csv('data/gdp.csv',encoding='utf-8')



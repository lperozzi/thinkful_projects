# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:18:30 2015

@author: lorenzoperozzi
"""
# Why: Store city Data bike
# Where: https://courses.thinkful.com/data-001v2/assignment/3.1.4

#--------------------------------------------------------------- PREP. DATA ----

import sqlite3 as lite
import time
import collections
# a package for parsing a string into a Python datetime object
from dateutil.parser import parse
import requests
from pandas.io.json import json_normalize

r = requests.get('http://www.citibikenyc.com/stations/json')
df = json_normalize(r.json()['stationBeanList'])

# initialize the database
con = lite.connect('citi_bike.db')
cur = con.cursor()

#--------------------------------------CITI BIKE REFERENCE TABLES CREATION ----
table1 = "CREATE TABLE citibike_reference \
(id INT PRIMARY KEY, totalDocks INT, city TEXT, \
altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, \
testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, \
latitude NUMERIC, location TEXT )"
with con:
    cur.execute(table1)

#a prepared SQL statement we're going to execute over and over again
sql = "INSERT INTO citibike_reference \
(id, totalDocks, city, altitude, stAddress2, longitude, postalCode, \
testStation, stAddress1, stationName, landMark, latitude, location) \
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"    

#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        cur.execute(sql,(station['id'],station['totalDocks'],\
                         station['city'],station['altitude'],\
                         station['stAddress2'],station['longitude'],\
                         station['postalCode'],station['testStation'],\
                         station['stAddress1'],station['stationName'],\
                         station['landMark'],station['latitude'],\
                         station['location']))
        
# LP ##
# To get multiple readings by minute, the id column need a "" 
# in front the number
        
#extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist() 
#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids] 


#----------------------------------------- AVAILABLE BIKES TABLES CREATION ----
#in this case, we're concatentating the string and joining all the station ids 
#(now with '_' and 'INT' added)

table2 = "CREATE TABLE available_bikes \
( execution_time INT, " +  ", ".join(station_ids) + ");"

with con:
    cur.execute(table2)
    
#------------------------------------------------  AVAILABLE BIKES UPDATE ----

#We create an entry for the execution time by inserting 
#it into the database:
sql2 = "INSERT INTO available_bikes \
(execution_time) \
VALUES (?)"

for t in range(60):
    r = requests.get('http://www.citibikenyc.com/stations/json')
    exec_time = parse(r.json()['executionTime'])
    cur.execute(sql2,(exec_time.strftime('%s'),))
    # Then we iterate through the stations in the "stationBeanList":
    id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station
    #loop through the stations in the station list
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']
    
    #iterate through the defaultdict to update the values in the database
    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" \
                    + str(k) + " = " + str(v) + \
                    " WHERE execution_time = " \
                    + exec_time.strftime('%s') + ";")
    con.commit()
    time.sleep(60)
con.close()

#------------------------------------------------   DATA ----


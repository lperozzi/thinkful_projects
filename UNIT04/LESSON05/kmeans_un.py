# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:14:29 2015

@author: lorenzoperozzi
"""

import numpy as np
import pandas as pd
from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('data/un.csv')

print('The rows in dataset are {0}\n'.format(df.shape[0]))
print('There are {0} non-nulls value in the dataset\n'.format(np.sum(df.count(axis = 0))))
print('The columns with the most of non-null values are {0} and {1}\n '.format(df.count(axis=0).index[0],df.count(axis=0).index[1]))
print('The data type of each columns are:')
print(df.dtypes)
print('\nThere are {0} countries\n'.format(df['country'].describe()[0]))

df = df.dropna()
data = df[['lifeMale', 'lifeFemale','infantMortality','GDPperCapita']].values
data = df.as_matrix(['lifeMale', 'lifeFemale','infantMortality','GDPperCapita'])
K = range(1,10)

# scipy.cluster.vq.kmeans
KM = [kmeans(data,k) for k in K] # apply kmeans 1 to 10
# cluster centroids
centroids = [cent for (cent,var) in KM]   # cluster centroids
#distance between each point and each cluster centroid
D_k = [cdist(data, cent, 'euclidean') for cent in centroids] # note dist = scipy.spatial.distance.cdist(a,b) 
#                                                                is equivalent to np.sqrt(np.sum((a-b)**2,axis=1) 
#Calculate the average within-cluster sum of squares for each centroid
dist = [np.min(D,axis=1) for D in D_k]
avgWCSS = [sum(d)/data.shape[0] for d in dist] 

# plotting
# plot elbow curve
plt.plot(K, avgWCSS, 'b*-')
plt.xlabel('Number of cluster')
plt.ylabel('Average within cluster sum of squares')
plt.plot(K[2], avgWCSS[2], marker='o', mec='r', ms=15, mew=2, mfc='None')
plt.show()


############################# Cluster UN data using K = 3 ######################
km = KMeans(3) # initialize
km.fit(data)
cluster = km.predict(data)

# GDP vs Infant mortality
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(5,10))

GDP = data[:,3]
infantMortality = data[:,2]
lifeFemale = data[:,1]
lifeMale = data[:,0]

ax1.scatter(GDP,infantMortality,c=cluster, cmap=plt.cm.Paired)
ax1.set_xlabel('GDP per Capita')
ax1.set_ylabel('Infant mortality')
ax1.set_xlim([0,np.max(GDP)])

ax2.scatter(GDP,lifeFemale,c=cluster, cmap=plt.cm.Paired)
ax2.set_xlabel('GDP per Capita')
ax2.set_ylabel('Female life expectancy')
ax2.set_xlim([0,np.max(GDP)])

ax3.scatter(GDP,lifeMale,c=cluster, cmap=plt.cm.Paired)
ax3.set_xlabel('GDP per Capita')
ax3.set_ylabel('Male life expenctancy')
ax3.set_xlim([0,np.max(GDP)])

f.tight_layout()
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:37:40 2015

@author: lorenzoperozzi
"""
# what: clustering
# where: https://courses.thinkful.com/data-001v2/assignment/4.5.2
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
Y = iris.target

# row and column sharing
f, ((ax1, ax2), (ax3, ax4), (ax5,ax6)) = plt.subplots(3, 2)
ax1.scatter(iris.data[:,0],iris.data[:,1],c=Y, cmap=plt.cm.Paired)
ax1.set_xlabel('sepal length')
ax1.set_ylabel('sepal width')

ax2.scatter(iris.data[:,2],iris.data[:,3],c=Y, cmap=plt.cm.Paired)
ax2.set_xlabel('petal length')
ax2.set_ylabel('petal width')

ax3.scatter(iris.data[:,2],iris.data[:,1],c=Y, cmap=plt.cm.Paired)
ax3.set_xlabel('petal length')
ax3.set_ylabel('sepal width')

ax4.scatter(iris.data[:,2],iris.data[:,0],c=Y, cmap=plt.cm.Paired)
ax4.set_xlabel('petal length')
ax4.set_ylabel('sepal length')

ax5.scatter(iris.data[:,0],iris.data[:,3],c=Y, cmap=plt.cm.Paired)
ax5.set_xlabel('sepal length')
ax5.set_ylabel('petal width')

ax6.scatter(iris.data[:,3],iris.data[:,1],c=Y, cmap=plt.cm.Paired)
ax6.set_xlabel('petal width')
ax6.set_ylabel('sepal width')
f.tight_layout()
plt.show()
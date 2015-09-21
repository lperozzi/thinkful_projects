# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:52:18 2015

@author: lorenzoperozzi
"""

from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np


from matplotlib.colors import ListedColormap
# Create color maps for 3-class classification problem, as with iris
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
  
def subplot_estimator(estimator,ax, X, y,title):
    estimator.fit(X, y)
    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
#    ax.figure()
    ax.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    ax.axis('tight')
    ax.axis('off')
    ax.set_title(title,fontsize=10)

     
iris = datasets.load_iris()
svc = svm.SVC(kernel='linear')

#_____________________________________________________  Two flower

y_SetVers = np.r_[iris.target[0:50],iris.target[50:100]]
y_SetVirg = np.r_[iris.target[0:50],iris.target[100:150]]
y_VersVirg = np.r_[iris.target[50:100],iris.target[100:150]]

X_SetVers = np.r_[iris.data[0:50],iris.data[50:100]]
X_SetVirg = np.r_[iris.data[0:50],iris.data[100:150]]
X_VersVirg = np.r_[iris.data[50:100],iris.data[100:150]]

#  Combination 1 setosa vs versicolor

y = y_SetVers
svc = svm.SVC(kernel='linear')

# classifying irises based on sepal length and width
X1 = X_SetVers[:,:2]

# classifying irises based on petal length and width
X2 = X_SetVers[:, 2:4]

# classifying irises based on sepal length and petal length 
X3 = np.c_[X_SetVers[:,0],X_SetVers[:,2]]

# classifying irises based on sepal width and petal width 
X4 = np.c_[X_SetVers[:,1],X_SetVers[:,3]]

# classifying irises based on sepal length and petal width
X5 = np.c_[X_SetVers[:,0],X_SetVers[:,3]]

# classifying irises based on sepal width and petal length
X6 = np.c_[X_SetVers[:,1],X_SetVers[:,2]]

# Plotting results
f, ((ax1, ax2), (ax3, ax4), (ax5,ax6)) = plt.subplots(3, 2, figsize=(10,10))
subplot_estimator(svc,ax1,X1,y,'classifying irises based on sepal length and width')
subplot_estimator(svc,ax2,X2,y,'classifying irises based on petal length and width')
subplot_estimator(svc,ax3,X3,y,'classifying  based on sepal length and petal length')
subplot_estimator(svc,ax4,X4,y,'classifying  based on sepal width and petal width')
subplot_estimator(svc,ax5,X5,y,'classifying  based on sepal length and petal width')
subplot_estimator(svc,ax6,X6,y,'classifying  based on sepal width and petal length')
f.suptitle("Setosa vs Versicolor", fontsize=16)
#f.tight_layout()
plt.show()

#  Combination 2 setosa vs virginica

y = y_SetVirg

# classifying irises based on sepal length and width
X1 = X_SetVirg[:,:2]

# classifying irises based on petal length and width
X2 = X_SetVirg[:, 2:4]

# classifying irises based on sepal length and petal length 
X3 = np.c_[X_SetVirg[:,0],X_SetVirg[:,2]]

# classifying irises based on sepal width and petal width 
X4 = np.c_[X_SetVirg[:,1],X_SetVirg[:,3]]

# classifying irises based on sepal length and petal width
X5 = np.c_[X_SetVirg[:,0],X_SetVirg[:,3]]

# classifying irises based on sepal width and petal length
X6 = np.c_[X_SetVirg[:,1],X_SetVirg[:,2]]

# Plotting results
f, ((ax1, ax2), (ax3, ax4), (ax5,ax6)) = plt.subplots(3, 2, figsize=(10,10))
subplot_estimator(svc,ax1,X1,y,'classifying irises based on sepal length and width')
subplot_estimator(svc,ax2,X2,y,'classifying irises based on petal length and width')
subplot_estimator(svc,ax3,X3,y,'classifying  based on sepal length and petal length')
subplot_estimator(svc,ax4,X4,y,'classifying  based on sepal width and petal width')
subplot_estimator(svc,ax5,X5,y,'classifying  based on sepal length and petal width')
subplot_estimator(svc,ax6,X6,y,'classifying  based on sepal width and petal length')
f.suptitle("Setosa vs Virginica", fontsize=16)
plt.show()

#  Combination 3 versicolor vs virginica

y = y_VersVirg

# classifying irises based on sepal length and width
X1 = X_VersVirg[:,:2]

# classifying irises based on petal length and width
X2 = X_VersVirg[:, 2:4]

# classifying irises based on sepal length and petal length 
X3 = np.c_[X_VersVirg[:,0],X_VersVirg[:,2]]

# classifying irises based on sepal width and petal width 
X4 = np.c_[X_VersVirg[:,1],X_VersVirg[:,3]]

# classifying irises based on sepal length and petal width
X5 = np.c_[X_VersVirg[:,0],X_VersVirg[:,3]]

# classifying irises based on sepal width and petal length
X6 = np.c_[X_VersVirg[:,1],X_VersVirg[:,2]]

# Plotting results
f, ((ax1, ax2), (ax3, ax4), (ax5,ax6)) = plt.subplots(3, 2, figsize=(10,10))
subplot_estimator(svc,ax1,X1,y,'classifying irises based on sepal length and width')
subplot_estimator(svc,ax2,X2,y,'classifying irises based on petal length and width')
subplot_estimator(svc,ax3,X3,y,'classifying  based on sepal length and petal length')
subplot_estimator(svc,ax4,X4,y,'classifying  based on sepal width and petal width')
subplot_estimator(svc,ax5,X5,y,'classifying  based on sepal length and petal width')
subplot_estimator(svc,ax6,X6,y,'classifying  based on sepal width and petal length')
f.suptitle("Versicolor vs Virgicolor", fontsize=16)
plt.show()

print('Each combination separates almost Setosa from Versicolor and Setosa from Virgicolor clean\n')
print('However, the boundaries between Versicolor and Virgicolor is fuzzy\n')
print('Classifying based on petal lenght and width seems to give the best boundary')

#_____________________________________________________  Two flower

y = iris.target

# classifying irises based on sepal length and width
X1 = iris.data[:, :2]

# classifying irises based on petal length and width
X2 = iris.data[:, 2:4]

# classifying irises based on sepal length and petal length 
X3 = np.c_[iris.data[:,0],iris.data[:,2]]

# classifying irises based on sepal width and petal width 
X4 = np.c_[iris.data[:,1],iris.data[:,3]]

# classifying irises based on sepal length and petal width
X5 = np.c_[iris.data[:,0],iris.data[:,3]]

# classifying irises based on sepal width and petal length
X6 = np.c_[iris.data[:,1],iris.data[:,2]]

# Plotting results
f, ((ax1, ax2), (ax3, ax4), (ax5,ax6)) = plt.subplots(3, 2, figsize=(10,10))
subplot_estimator(svc,ax1,X1,y,'classifying irises based on sepal length and width')
subplot_estimator(svc,ax2,X2,y,'classifying irises based on petal length and width')
subplot_estimator(svc,ax3,X3,y,'classifying  based on sepal length and petal length')
subplot_estimator(svc,ax4,X4,y,'classifying  based on sepal width and petal width')
subplot_estimator(svc,ax5,X5,y,'classifying  based on sepal length and petal width')
subplot_estimator(svc,ax6,X6,y,'classifying  based on sepal width and petal length')
f.suptitle("The 3 iris types together", fontsize=16)
plt.show()

print('With 3 classes the boundary between setosa and versicolor is narrower\n')


#_____________________________________________________  Tuning the regularization (C) parameter
svc1 = svm.SVC(kernel='linear', C=1000)
svc2 = svm.SVC(kernel='linear', C=0.1)

y = iris.target

# classifying irises based on sepal width and petal width 
X4 = np.c_[iris.data[:,1],iris.data[:,3]]

# Plotting results
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
subplot_estimator(svc1,ax1,X4,y,'High C value : small number of support vectors')
ax1.scatter(svc1.support_vectors_[:, 0], svc1.support_vectors_[:, 1], s=80, facecolors='none', zorder=10)
subplot_estimator(svc2,ax2,X4,y,'Small C value : high number of support vectors')
ax2.scatter(svc2.support_vectors_[:, 0], svc2.support_vectors_[:, 1], s=80, facecolors='none', zorder=10)
plt.show()

print('''Depending on the C values the shapes on the boundaries between classes
change. Here a small C values (< 1) seems to be inappropriate''')

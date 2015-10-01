# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:09:08 2015

@author: lorenzoperozzi
"""
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.lda import LDA
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# Load the datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# original plot
n,m = 2,3
X_orig = X[:,np.array([n,m])]

# Standardizing
X_std = StandardScaler().fit_transform(X)

# Covariance matrix
cov_mat = np.cov(X_std.T)
print('Covariance matrix: \n{0:s}'.format(cov_mat))

# eigendecomposition on the covariance matrix
eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('Eigenvectors: \n{0:s}'.format(eig_vecs))
print('\nEigenvalues: \n{0:s}'.format(eig_vals))

# rank the eigenvalues from highest to lowest in order choose the top k eigenvectors
# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i[0])
    
    
# Explained variance
tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

print('''The most of the variance can be explained by first and second component: \n
First conponent: {0:.2f}%\n
Second component: {1:.2f}%'''.format(var_exp[0],var_exp[1]))
        
        
# PCA in scikit-learn
sklearn_pca = sklearnPCA(n_components=2) 
X_pca = sklearn_pca.fit_transform(X_std)

def knn_classifier(X,y,split,metric):
#    split data set into training and testing data set
    X_train , X_test, y_train, y_test = train_test_split(X,y, test_size=split, random_state=42)
    
    min_misclassification = 1.0
    for k in range(1,20):
        model = KNeighborsClassifier(n_neighbors=k, metric=metric) # using euclidean distance
        model.fit(X_train, y_train)
        misclassification = (model.predict(X_test) != y_test).mean()
        print('k = {0} has misclassification error {1:.5f}'.format(k, misclassification))
        if misclassification < min_misclassification:
            min_misclassification = misclassification
            min_k = k
    return min_k
    
# k nearest neighbour on original iris data set component
print('Minkowski distance')
knn_classifier(X,y,0.3,'minkowski')
print('Manahttan distance')
knn_classifier(X,y,0.3,'manhattan')
print('Chebyshev distance')
knn_classifier(X,y,0.3,'chebyshev')
print('''\nkNN in original component is always correctly classified except 
if we use Chebyshev or Manhattan metric distance\n''')

# k nearest neighbour on PCA decomposed data set
print('Euclidean distance')
print('\nThe minimum misclassification in train set is obtained for k={0}\n'.format(knn_classifier(X_pca,y,0.3,'euclidean')))
print('Manahttan distance')
#knn_classifier(X_pca,y,0.3,'manhattan')
print('\nThe minimum misclassification in train set is obtained for k={0}\n'.format(knn_classifier(X_pca,y,0.3,'manhattan')))

# LDA in scikit-learn
sklearn_lda = LDA(n_components=2)
X_lda = sklearn_lda.fit_transform(X, y)

titles = ['Original plot','PCA plot','LDA plot']
def plot_comparing(X1,X2,X3,y):
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,5))
    subplots_comparing(ax1,X1,y,titles[0])
    subplots_comparing(ax2,X2,y,titles[1])
    subplots_comparing(ax3,X3,y,titles[2])

    
 
def subplots_comparing(ax,X,y,title):
    for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
        ax.scatter(X[y == i, 0], X[y == i, 1], c=c, label=target_name, alpha=0.5)
        ax.legend()
        ax.set_title('{0} of IRIS dataset'.format(title))


# plotting comparing original vs PCA vs LDA iris data set
plot_comparing(X_orig,X_pca,X_lda,y)
plt.show()
    

# Kmeans on origina datas set

km = KMeans(3) # initialize
km.fit(X_orig)
y_kmeans_orig = km.predict(X_orig)

# plotting comparing original vs PCA vs LDA iris data set with cluster kmeans on original data set
plot_comparing(X_orig,X_pca,X_lda,y_kmeans_orig)
plt.show()

# Kmeans on origina datas set
km = KMeans(3) # initialize
km.fit(X_lda)
y_kmeans_lda = km.predict(X_lda)

# plotting comparing original vs PCA vs LDA iris data set with cluster kmeans on original data set
plot_comparing(X_orig,X_pca,X_lda,y_kmeans_lda)
plt.show()


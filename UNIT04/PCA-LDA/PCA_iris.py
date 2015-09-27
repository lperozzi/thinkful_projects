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

# Load the datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
n,m = 2,3
plt.scatter(X[:,n], X[:,m], c=y)

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
y_sklearn = sklearn_pca.fit_transform(X_std)

# Compare original plot with PCA plot

n,m = 2,3
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,10))
ax1.scatter(X[:,n], X[:,m], c=y)
ax2.scatter(X_std[:,n],X_std[:,m], c=y_sklearn)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:53:14 2015

@author: lorenzoperozzi
"""
from sklearn import datasets
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import cross_val_score

# Load the datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target


def svc_comparing(X,y,size,kernel):
    '''Comparing accuracy score on whole data set vs 
    splitted trining and testing data set based on test_size '''
    
    svc = svm.SVC(kernel=kernel)
    
    model1 = svc.fit(X,y)
    y_pred1 = model1.predict(X)
    pred1 = accuracy_score(y,y_pred1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = size, random_state=0)
    print('The training set as {0} points and the test set has {1} points\n'.format(len(X_train),(len(X)-len(X_train))))
    
    model2 = svc.fit(X_train,y_train)
    y_pred2 = model2.predict(X_test)
    pred2 = accuracy_score(y_test,y_pred2)
    
    print('''The original data set give a score of {0:.2f}% and the 
    splitted data set give a score of {1:.2f}%'''.format(pred1,pred2))
    

svc_comparing(X,y,0.4,'linear')


# cross-validation with SVM classifier

def svc_crossValidation(X,y,fold,scoring,kernel):
    '''Compute the score at each cross-validation iteration (fold)'''
    svc = svm.SVC(kernel=kernel)
    if scoring == 'accuracy' or 'f1_weighted':
        scores = cross_val_score(svc, X, y, cv=fold, scoring=scoring)
    else:
        average = 'weighted'
        scores = cross_val_score(svc, X, y, cv=fold, scoring=scoring, average=average)
        
    print('Accuracy: {0:.4f} (+/- {1:.4f})'.format(scores.mean(),scores.std()*2))
    

svc_crossValidation(X,y,5,'accuracy','linear')
svc_crossValidation(X,y,5,'f1_weighted','linear')
svc_crossValidation(X,y,5,'accuracy','poly')
svc_crossValidation(X,y,5,'f1_weighted','poly')
svc_crossValidation(X,y,5,'accuracy','rbf')
svc_crossValidation(X,y,5,'f1_weighted','rbf')

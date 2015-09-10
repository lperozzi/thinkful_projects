# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:50:20 2015

@author: lorenzoperozzi
"""
# tutorial on http://radimrehurek.com/data_science_python/
import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import glob
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

###########################################  FUNCTIONS ########################
# split body into its individual words    
def split_into_lemmas(body):
    body = unicode(body, 'utf8')
    words = TextBlob(body).words
    # for each word, take its "base form" = lemma except for stopwords
    return [word.lemma for word in words if not word in stopwords.words('english')]
    
def reader(f):
    d = pd.read_csv(f)
    d.columns = range(d.shape[1])
    return d

##############################################################################
# concat every section_final_csv to a unique dataframe
files = glob.glob("data/*_final.csv")
df = pd.concat([reader(f) for f in files], keys=files)
# naming columns
df.columns = ['body', 'section']

# split data into training and test dataset
art_train, art_test, label_train, label_test = train_test_split(df['body'], df['section'], test_size=0.2)

#df.body.apply(split_into_lemmas)
###############################  TRAINING DATA ################################

# Bag of words transformer of the training dataset using split into lemma analyzer
bow_transformer_train = CountVectorizer(analyzer=split_into_lemmas).fit(art_train)

# Transform for the test data set using the bow_transformer
articles_bow_train = bow_transformer_train.transform(art_train)
print 'sparse matrix shape: {0}'.format(articles_bow_train.shape)
print 'number of non-zeros: {0}'.format(articles_bow_train.nnz)
print 'sparsity: {0:.2f} %'.format(100.0 * articles_bow_train.nnz / (articles_bow_train.shape[0] * articles_bow_train.shape[1]))

# term weighting and normalization using TF-IDF (term frequency–inverse document frequency) 
# for the training dataset
tfidf_transformer_train = TfidfTransformer().fit(articles_bow_train)
articles_tfidf_train = tfidf_transformer_train.transform(articles_bow_train)

# Multinomial NB classifier 
section_detector = MultinomialNB().fit(articles_tfidf_train, label_train)


####################################  TEST DATA ###############################
# Transform for the test data set using the same bow_transformer as for the train dataset
articles_bow_test = bow_transformer_train.transform(art_test)
print 'sparse matrix shape: {0}'.format(articles_bow_test.shape)
print 'number of non-zeros: {0}'.format(articles_bow_test.nnz)
print 'sparsity: {0:.2f} %'.format(100.0 * articles_bow_test.nnz / (articles_bow_test.shape[0] * articles_bow_test.shape[1]))

# term weighting and normalization using TF-IDF (term frequency–inverse document frequency) 
# for the test dataset
tfidf_transformer_test = TfidfTransformer().fit(articles_bow_test)
articles_tfidf_test = tfidf_transformer_test.transform(articles_bow_test)


# how many article of the test dataset do we classify correctly?
articles_predictions = section_detector.predict(articles_tfidf_test)

# Printing the accuracy results
print 'accuracy: {0}'.format(accuracy_score(label_test, articles_predictions))
print 'confusion matrix:\n {0}'.format(confusion_matrix(label_test, articles_predictions))
print '(row=expected, col=predicted)'

# Plotting the confusion matrix
plt.matshow(confusion_matrix(label_test, articles_predictions), cmap=plt.cm.binary, interpolation='nearest')
plt.title('confusion matrix')
plt.colorbar()
plt.ylabel('expected label')
plt.xlabel('predicted label')
plt.show()













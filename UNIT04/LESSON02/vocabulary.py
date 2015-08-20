# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:39:38 2015

@author: lorenzoperozzi
"""

from collections import Counter
from glob import iglob
import re
import os
from nltk.corpus import stopwords
import csv


# writing a vacabulary with words and their frequency for all the spam folder
topwords = 10
folderpath1 = 'data/enron1/spam/'
counter_spam = Counter()
for filepath in iglob(os.path.join(folderpath1, '*.txt')):
    with open(filepath) as filehandle:
            f = filehandle.read()
            # preprocessing the file to keep only letters
            letters_only = re.sub("[^a-zA-Z]"," ",f)
            lower_case = letters_only.lower()
            words = lower_case.split()
            # remove stopwords form the words
            words = [w for w in words if w not in stopwords.words("english")]
            counter_spam.update(words)
        
print 'Spam counter (10 most frequent words)\n'
for word, count in counter_spam.most_common(topwords):
    print '{}: {}'.format(count, word)

# saving th spam vocabulary to a csv file
with open('data/spam_vocabulary.csv','wb') as csvfile:
    count_spam_writer = csv.writer(csvfile)
    for word, count in counter_spam.items():
        count_spam_writer.writerow([word, count])
        
        

# writing a vacabulary with words and their frequency for all the ham folder
topwords = 10
folderpath2 = 'data/enron1/ham/'
counter_ham = Counter()
for filepath in iglob(os.path.join(folderpath2, '*.txt')):
    with open(filepath) as filehandle:
            f = filehandle.read()
            # preprocessing the file to keep only letters
            letters_only = re.sub("[^a-zA-Z]"," ",f)
            lower_case = letters_only.lower()
            words = lower_case.split()
            # remove stopwords form the words
            words = [w for w in words if w not in stopwords.words("english")]
            counter_ham.update(words)
        

print '\nHam counter (10 most frequent words)\n'
for word, count in counter_ham.most_common(topwords):
    print '{}: {}'.format(count, word)

# saving the ham vocabulary to a csv file
with open('data/ham_vocabulary.csv','wb') as csvfile:
    count_ham_writer = csv.writer(csvfile)
    for word, count in counter_ham.items():
        count_ham_writer.writerow([word, count])
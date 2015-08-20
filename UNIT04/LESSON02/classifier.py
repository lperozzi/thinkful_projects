# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:42:55 2015

@author: lorenzoperozzi
"""
from commands import getstatusoutput as system
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
import re

# Count files in folder
folder = "data/enron1"
order_template = "ls {0}/{1} | wc -l"
status, output = system(order_template.format(folder, "spam"))
spam_count = float(output)
status, output = system(order_template.format(folder, "ham"))
ham_count = float(output)

# Compute the probabilities of spam and ham
P_spam = spam_count / (spam_count + ham_count)
P_ham = ham_count / (spam_count + ham_count)

df_spam = pd.read_csv('data/spam_vocabulary.csv',names=['word', 'frequency'])
df_ham = pd.read_csv('data/ham_vocabulary.csv', names=['word','frequency'])

# calculate theta (probability that an individual word is present in a ham email)
df_ham['theta'] = df_ham['frequency'] / (spam_count + ham_count)
# calculate theta (probability that an individual word is present in a spam email)
df_spam['theta'] = df_spam['frequency'] / (spam_count + ham_count)
# calculate wj (log(theta/(1-theta)))
df_spam['wj'] = np.log(df_spam['theta'] / (1 - df_spam['theta']))
# calculate log(1-theta) 
df_spam['log(1-theta)'] = np.log(1 - df_spam['theta'])

# calculate xi (email vector for those entries are 1 or 0) 
folder = 'data/enron1/spam/'
f = open(folder+'0008.2003-12-18.GP.spam.txt')
raw = f.read()
letters_only = re.sub("[^a-zA-Z]"," ",raw)
lower_case = letters_only.lower()
words = lower_case.split()            
words = [w for w in words if w not in stopwords.words("english")]
# find words that are in spam vocabulary
words = '|'.join(words)
df_spam['xi'] = df_spam['word'].str.contains(words)
df_spam['xi'] = df_spam['xi'].astype('bool')
# convert xi column in 0 or 1 value
df_spam['xi'] = df_spam['xi'].astype(int)

# it xi must be multiplied with the theta?
#df_spam['xi_2'] = df_spam['theta'] * df_spam['xi']

# calculate w0
w0 = df_spam['log(1-theta)'].sum()
# calculate (xi * wj)
df_spam['xi*wj'] = df_spam['wj'] * df_spam['xi'] 



# calculate sum (xi*wj)
a = df_spam['xi_2*wj'].sum()

#b = a + w0

#b * np.log(P_spam) / (np.log(df_spam['theta'] + df_ham['theta']))








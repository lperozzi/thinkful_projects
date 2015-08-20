# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:42:55 2015

@author: lorenzoperozzi
"""
from commands import getstatusoutput as system
import numpy as np
import pandas as pd

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
df_spam['probailities'] = df_spam['frequency'] / spam_count

P_word_given_spam = np.zeros(len(word1))
P_word_given_ham = np.zeros(len(word1))
for i in range(len(word1)):
    # Compute the conditional probabilities of word given spam
    P_word_given_spam[i] = word_in_spam_count[i] / spam_count
    # Compute the conditional probabilities of word given ham
    P_word_given_ham[i] = word_in_ham_count[i] / ham_count
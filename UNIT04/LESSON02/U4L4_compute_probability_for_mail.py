#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import math

#from IPython import embed

spam = pd.read_csv('data/spam_big.csv', header = 0, dtype=float)
ham = pd.read_csv('data/ham_big.csv', header = 0, dtype=float)

all_words = sorted(list(set(spam) | set(ham)))
spam = spam.reindex(columns=all_words, fill_value=1.)
ham = ham.reindex(columns=all_words, fill_value=1.)

# Binarize the data
spam[spam>=1] = 1
ham[ham>=1] = 1

# Count emails
spam_count = float(len(list(spam.index)))
ham_count = float(len(list(ham.index)))

# Compute the probabilities of spam and ham
P_spam = spam_count / (spam_count + ham_count)
P_ham = ham_count / (spam_count + ham_count)

# Count words in spam and in ham
word_in_spam_count = spam.sum()
word_in_ham_count = ham.sum()

# without laplacian smoothing
# Compute the conditional probabilities of word given spam
P_word_given_spam = word_in_spam_count / spam_count
# Compute the conditional probabilities of word given ham
P_word_given_ham = word_in_ham_count / ham_count

# Compute the join probabilities
P_spam_and_word = P_word_given_spam * P_spam
P_ham_and_word = P_word_given_ham * P_ham

# Compute the conditional probabilities of word given spam
P_spam_given_word = P_spam_and_word / (P_spam_and_word + P_ham_and_word)
P_ham_given_word = P_ham_and_word / (P_spam_and_word + P_ham_and_word)

# Save to disk
P_spam_given_word.to_csv("data/Probability_of_spam_given_word.csv", header=False)
P_ham_given_word.to_csv("data/Probability_of_ham_given_word.csv", header=False)

# Check how it behaves on our training set
# I work here with numpy arrays because indexing is easier
P_spam_given_word = P_spam_given_word.as_matrix()
P_ham_given_word = P_ham_given_word.as_matrix()

# Check on spam mails
spam_detected = 0
for mail in spam.values:
    ind_words = (mail>0)#np.logical_and( (mail>0) , (P_spam_given_word>0))
    Score_spam_given_mail = P_spam * np.exp( np.log(P_spam_given_word[ind_words]).sum() )
    ind_words = (mail>0) #np.logical_and( (mail>0) , (P_ham_given_word>0))
    Score_ham_given_mail = P_ham * np.exp(np.log(P_ham_given_word[ind_words]).sum())
    if (Score_spam_given_mail > Score_ham_given_mail):
        spam_detected += 1

print "Detected {0} spams in a set of {1} spam emails".format(spam_detected, spam_count)
print "Error: {0:.2f} ".format(100.*(spam_count-spam_detected)/spam_count)
# Check on ham mails
ham_detected = 0
for mail in ham.values:
    ind_words = (mail>0)
    Score_spam_given_mail = P_spam * np.exp(np.log(P_spam_given_word[ind_words]).sum())
    ind_words = (mail>0)
    Score_ham_given_mail = P_ham * np.exp(np.log(P_ham_given_word[ind_words]).sum())
    if (Score_spam_given_mail > Score_ham_given_mail):
        ham_detected += 1

print "Detected {0} spams in a set of {1} ham emails".format(ham_detected, ham_count)
print "Error: {0:.2f} ".format(100.*ham_detected/ham_count)


# LP
# with laplacian smoothing
alpha = 1
beta = len(P_word_given_spam)
# Compute the conditional probabilities of word given spam
P_word_given_spam = (word_in_spam_count + alpha) / (spam_count + beta)
# Compute the conditional probabilities of word given ham
P_word_given_ham = (word_in_ham_count + alpha) / (ham_count + beta)

# Compute the join probabilities
P_spam_and_word = P_word_given_spam * P_spam
P_ham_and_word = P_word_given_ham * P_ham

# Compute the conditional probabilities of word given spam
P_spam_given_word = P_spam_and_word / (P_spam_and_word + P_ham_and_word)
P_ham_given_word = P_ham_and_word / (P_spam_and_word + P_ham_and_word)

# Save to disk
P_spam_given_word.to_csv("data/Probability_of_spam_given_word.csv", header=False)
P_ham_given_word.to_csv("data/Probability_of_ham_given_word.csv", header=False)

# Check how it behaves on our training set
# I work here with numpy arrays because indexing is easier
P_spam_given_word = P_spam_given_word.as_matrix()
P_ham_given_word = P_ham_given_word.as_matrix()

# Check on spam mails
spam_detected_ls = 0
for mail in spam.values:
    ind_words = (mail>0)#np.logical_and( (mail>0) , (P_spam_given_word>0))
    Score_spam_given_mail = P_spam * np.exp( np.log(P_spam_given_word[ind_words]).sum() )
    ind_words = (mail>0) #np.logical_and( (mail>0) , (P_ham_given_word>0))
    Score_ham_given_mail = P_ham * np.exp(np.log(P_ham_given_word[ind_words]).sum())
    if (Score_spam_given_mail > Score_ham_given_mail):
        spam_detected_ls += 1

print "Detected {0} spams in a set of {1} spam emails with Laplace smoothing".format(spam_detected_ls, spam_count)
print "Error: {0:.2f} ".format(100.*(spam_count-spam_detected)/spam_count)
# Check on ham mails
ham_detected_ls = 0
for mail in ham.values:
    ind_words = (mail>0)
    Score_spam_given_mail = P_spam * np.exp(np.log(P_spam_given_word[ind_words]).sum())
    ind_words = (mail>0)
    Score_ham_given_mail = P_ham * np.exp(np.log(P_ham_given_word[ind_words]).sum())
    if (Score_spam_given_mail > Score_ham_given_mail):
        ham_detected_ls += 1

print "Detected {0} spams in a set of {1} ham emails with Laplace smoothing".format(ham_detected_ls, ham_count)
print "Error: {0:.2f} \n".format(100.*ham_detected/ham_count)
print "Detection of spam improved by {0} emails with Lapalce smoothing".format(spam_detected_ls-spam_detected)



#!/usr/bin/env python
# coding: utf-8

from commands import getstatusoutput as system
import numpy as np

folder = "data/enron1"
word = "meeting" # meeting, money, viagra, enron

word1 = ['meeting','money','viagra','enron']
# Count files in folder
order_template = "ls {0}/{1} | wc -l"
status, output = system(order_template.format(folder, "spam"))
spam_count = float(output)
status, output = system(order_template.format(folder, "ham"))
ham_count = float(output)

# Count words in files in folder
order_template = "grep -il {0} {1}/{2}/*.txt | wc -l"
word_in_spam_count = np.zeros(len(word1))
word_in_ham_count = np.zeros(len(word1))
for i in range(len(word1)):
    status, output = system(order_template.format(word1[i], folder, "spam"))
    word_in_spam_count[i] = float(output)
    status, output = system(order_template.format(word1[i], folder, "ham"))
    word_in_ham_count[i] = float(output)

# Compute the probabilities of spam and ham
P_spam = spam_count / (spam_count + ham_count)
P_ham = ham_count / (spam_count + ham_count)

P_word_given_spam = np.zeros(len(word1))
P_word_given_ham = np.zeros(len(word1))
for i in range(len(word1)):
    # Compute the conditional probabilities of word given spam
    P_word_given_spam[i] = word_in_spam_count[i] / spam_count
    # Compute the conditional probabilities of word given ham
    P_word_given_ham[i] = word_in_ham_count[i] / ham_count

P_spam_and_word = np.zeros(len(word1))
P_ham_and_word = np.zeros(len(word1))
for i in range(len(word1)):
    # Compute the join probabilities
    P_spam_and_word[i] = P_word_given_spam[i] * P_spam
    P_ham_and_word[i] = P_word_given_ham[i] * P_ham

# Phi spam is the probability that an individual word is present in a spam email
phi_spam = P_spam_and_word

w_j = np.log(phi_spam[i]/(1 - phi_spam[i]))
w_o = np.log

# Probabilities of word given spam


# Compute the conditional probabilities of word given spam
P_spam_given_word = P_spam_and_word / (P_spam_and_word + P_ham_and_word)
P_ham_given_word = P_ham_and_word / (P_spam_and_word + P_ham_and_word)

# Output the probabilities
print("The probability of mail being SPAM when it contains the word %s is %.5f" %(word, P_spam_given_word))
print("The probability of mail being  HAM when it contains the word %s is %.5f" %(word, P_ham_given_word))



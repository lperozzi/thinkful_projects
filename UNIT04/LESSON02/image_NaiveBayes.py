# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:19:28 2015

@author: lorenzoperozzi
"""

import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from IPython import embed

filename = "data/images.csv"
df = pd.read_csv(filename)

threshold = 0.20
NPixels = 160 * 240
df_landscape = df[df["image"]=="landscape"]
df_landscape  = ( df_landscape[list(df)[1:-1]] / NPixels ) < threshold
df_headshot = df[df["image"]=="headshot"][list(df)[1:-1]]
df_headshot  = ( df_headshot[list(df)[1:-1]] / NPixels ) < threshold
# Binarize the data
df_landscape = df_landscape.astype(int)
df_headshot = df_headshot.astype(int)

# Count images
landscape_count = float(len(list(df_landscape.index)))
headshot_count = float(len(list(df_headshot.index)))

# Compute the probabilities of headshot and landscape
P_landscape = landscape_count / (landscape_count + headshot_count)
P_headshot = headshot_count / (landscape_count + headshot_count)

# Count 'rgbs' in landscape and in headshot
rgb_in_landscape_count = df_landscape.sum()
rgb_in_headshot_count = df_headshot.sum()

# with laplacian smoothing
alpha = 1
beta = len(rgb_in_landscape_count)
# Compute the conditional probabilities of word given spam
P_rgb_given_landscape = (rgb_in_landscape_count + alpha) / (landscape_count + beta)
# Compute the conditional probabilities of word given ham
P_rgb_given_headshot = (rgb_in_headshot_count + alpha) / (headshot_count + beta)

## without laplacian smoothing
## Compute the conditional probabilities of word given spam
#P_rgb_given_landscape = rgb_in_landscape_count / landscape_count
## Compute the conditional probabilities of word given ham
#P_rgb_given_headshot = rgb_in_headshot_count / headshot_count

# Compute the join probabilities
P_landscape_and_rgb = P_rgb_given_landscape * P_landscape
P_headshot_and_rgb = P_rgb_given_headshot * P_headshot

# Compute the conditional probabilities of word given spam
P_landscape_given_rgb = P_landscape_and_rgb / (P_landscape_and_rgb + P_headshot_and_rgb)
P_headshot_given_rgb = P_headshot_and_rgb / (P_landscape_and_rgb + P_headshot_and_rgb)

# Save to disk
P_landscape_given_rgb.to_csv("data/Probability_of_landscape_given_rgb.csv", header=False)
P_headshot_given_rgb.to_csv("data/Probability_of_headshot_given_rgb.csv", header=False)


# Check how it behaves on our training set
# I work here with numpy arrays because indexing is easier
P_landscape_given_rgb = P_landscape_given_rgb.as_matrix()
P_headshot_given_rgb = P_headshot_given_rgb.as_matrix()

# Check on landscape
landscape_detected = 0
for images in df_landscape.values:
    ind_words = (images>0)  #np.logical_and( (mail>0) , (P_spam_given_word>0))
#    print(ind_words)  
    Score_landscape_given_image = P_landscape * np.exp( np.log(P_landscape_given_rgb[ind_words]).sum() )
    ind_words = (images>0) #np.logical_and( (mail>0) , (P_ham_given_word>0))
    Score_headshot_given_image = P_headshot * np.exp(np.log(P_headshot_given_rgb[ind_words]).sum())
    if (Score_landscape_given_image > Score_headshot_given_image):
        landscape_detected += 1

print( "Detected {0} landscape in a set of {1} landscape images".format(landscape_detected, landscape_count))
print( "Error: {0:.2f} ".format(100.*(landscape_count-landscape_detected)/landscape_count))


# Check on ham mails
headshot_detected = 0
for images in df_headshot.values:
    ind_words = (images>0)
    Score_landscape_given_image = P_landscape * np.exp(np.log(P_landscape_given_rgb[ind_words]).sum())
    ind_words = (images>0)
    Score_headshot_given_image = P_headshot * np.exp(np.log(P_headshot_given_rgb[ind_words]).sum())
    if (Score_landscape_given_image > Score_headshot_given_image):
        headshot_detected += 1

print ("Detected {0} landscape in a set of {1} headshot images".format(headshot_detected, headshot_count))
print ("Error: {0:.2f} ".format(100.*headshot_detected/headshot_count))



# Or do a more advanced work
# http://inst.eecs.berkeley.edu/~cs188/fa06/projects/classification/4/writeup/index.html

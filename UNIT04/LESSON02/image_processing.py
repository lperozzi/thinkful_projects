# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:35:15 2015

@author: lorenzoperozzi
"""
import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#setup a standard image size; this will distort some images but will get everything into the same shape
STANDARD_SIZE = (240, 160)

landscape = glob.glob("data/flickr/landscape/*.jpg") # ["all the .jpg files in the folder", ]
features_l = []
for i, image in enumerate(landscape):
    img = Image.open(image)
    img = img.resize(STANDARD_SIZE)
    img = list(img.getdata())
    img = map(list, img)
    img = np.array(img)
#    Take 5 bins for RGB
    hist_r=np.histogram(img[:,0],bins=5)   
    hist_g=np.histogram(img[:,1],bins=5)
    hist_b=np.histogram(img[:,2],bins=5)
    features_l.append([hist_r[0], hist_g[0], hist_b[0]])
    
# here i have a (50, 3, 5) array (#images, #colors(rgb), #bins)
features_l = np.array(features_l)
# i want a (50,15) array
s = features_l.shape[1] * features_l.shape[2]
features_l_wide = features_l.reshape(50,s)
    
# doing the same for headshot set
headshot = glob.glob("data/flickr/headshot/*.jpg") # ["all the .jpg files in the folder", ]
features_h = []
for i, image in enumerate(headshot):
    img = Image.open(image)
    img = img.resize(STANDARD_SIZE)
    img = list(img.getdata())
    img = map(list, img)
    img = np.array(img)
#    Take 5 bins for RGB
    hist_r=np.histogram(img[:,0],bins=5)    
    hist_g=np.histogram(img[:,1],bins=5)
    hist_b=np.histogram(img[:,2],bins=5)
    features_h.append([hist_r[0], hist_g[0], hist_b[0]])
    
# here i have a (50, 3, 5) array (#images, #colors(rgb), #bins)
features_h = np.array(features_l)
# i want a (50,15) array
s = features_h.shape[1] * features_h.shape[2]
features_h_wide = features_h.reshape(50,s)
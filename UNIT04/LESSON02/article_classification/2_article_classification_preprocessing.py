# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:33:49 2015

@author: lorenzoperozzi
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

sections = ['Arts','Business','Obituaries','Sports','World']


for s in range(len(sections)):
    df = pd.read_csv('data/'+sections[s]+'.csv')
    urls = list(df['url'])
    text = []
    for i in range(len(urls)):
        article = requests.get(urls[i])
        data = BeautifulSoup(article.content)
        # isolating only body text
        if sections[s] == 'Business':
            body =[''.join(d.findAll(text=True)) for d in data.findAll("p", {"itemprop":"articleBody"})]
        else:
            body =[''.join(d.findAll(text=True)) for d in data.findAll("p", {"class":"story-body-text story-content"})]         
        # remove line
        body = ''.join(line.strip() for line in body)
        body = re.sub("[^a-zA-Z]",           # The pattern to search for characters
                      " ",                   # The pattern to replace it with blank space
                      body )
        # lower case
        body = body.lower()
        text.append(body)
        # savinf to dataframe and csv
        data = {'body': text}
        df = pd.DataFrame(data) 
        # delate blank space (from articles that are video (empty text))
        df = df[df.body != '']
        df['section'] = sections[s]
#        save to csv
        df.to_csv('data/'+sections[s]+'_final.csv',mode = 'w', index=False)
        


        

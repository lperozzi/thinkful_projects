# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:33:49 2015

@author: lorenzoperozzi
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup


sections = ['Arts','Business','Obituaries','Sports','World']
data = pd.DataFrame({"url" : range(1000),
                     "title" : range(1000),
                     "body" : range(1000)})
df_final = pd.DataFrame(data)

for s in range(len(sections)):
    s=1
    df = pd.read_csv('data/'+sections[s]+'.csv')
    urls = list(df['url'])
    text = []
    for i in range(len(urls)):
        article = requests.get(urls[i])
        data = BeautifulSoup(article.content)
#       isolating only body text
        body =[''.join(d.findAll(text=True)) for d in data.findAll("p", {"class":"story-body-text story-content"})]    
#       remove line
        body = ''.join(line.strip() for line in body)
        text.append(body)

    df_final['url'] = df['url']
    df_final['title'] = df['headline']
    df_final['body'] = text
    df_final.to_csv('data/'+sections[s]+'_final.csv')
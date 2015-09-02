# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:39:32 2015

@author: lorenzoperozzi
"""
import pandas as pd
from nytimesarticle import articleAPI


def search_articles_by_section(section):
    '''
    This function takes a section name of nyt and save the most recent 1000 entries
    (date,headline,section,url,word_count) to a csv file
    '''
    # defining API key 
    api = articleAPI('''APIkeynumber''')
    df = pd.DataFrame()
    for i in range(1,101): # nyt api search not alllow to search behind page 10
        articles = api.search(fq = {'source':['The New York Times'],
                                    'section_name':[section]},
                              page = str(i))
        df = df.append(parse_articles(articles))
        df.to_csv('data/'+section+'.csv',mode = 'w', index=False)
    return(df)

def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['url'] = i['web_url']
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        dic['section'] = i['section_name']
        dic['word_count'] = i['word_count']
        news.append(dic)
    return(news) 

# save entries for Arts, Business, Obituaries, Sports, and World sections
# in a csv file (one file for each section)
search_articles_by_section('Arts')
search_articles_by_section('Business')
search_articles_by_section('Obituaries')
search_articles_by_section('Sports')
search_articles_by_section('World')
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:50:20 2015

@author: lorenzoperozzi
"""
# tutorial on http://radimrehurek.com/data_science_python/
import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import glob

# split body into its individual words    
def split_into_lemmas(body):
    body = unicode(body, 'utf8')
    words = TextBlob(body).words
    # for each word, take its "base form" = lemma except for stopwords
    return [word.lemma for word in words if not word in stopwords.words('english')]

sections = ['Arts','Business','Obituaries','Sports','World']


appended_data = []
for infile in glob.glob("data/*_final.csv"):
    print infile
    data = pd.read_csv(infile)
    data = data['body'].values.tolist()
    appended_data.append(data) ## store dataframes in list

appended_data = pd.concat(appended_data, axis=1) ## see documentation for more info

appended_data .to_excel('appedned.xlsx')

    
    
df_arts = pd.read_csv('data/Arts_final.csv')
df_arts['section'] = 'Arts'
df_business = pd.read_csv('data/Business_final.csv')
df_business['section'] = 'Business'
df_obituaries = pd.read_csv('data/Obituaries_final.csv')
df_obituaries['section'] = 'Obituaries'
df_sports = pd.read_csv('data/Sports_final.csv')
df_sports['section'] = 'Sports'
df_world = pd.read_csv('data/World_final.csv')
df_world['section'] = 'World'

df = pd.concat([df_arts,df_business,df_obituaries,df_sports,df_world], axis=1) ## see documentation for more info


df.body.apply(split_into_lemmas)

bow_transformer = CountVectorizer(analyzer=split_into_lemmas).fit(df['body'])

#message4 = df['body'][3]
#print message4
#
bow4 = bow_transformer.transform([message4])
print bow4
print bow4.shape
#
#print bow_transformer.get_feature_names()[55]
#print bow_transformer.get_feature_names()[1221]

messages_bow = bow_transformer.transform(df['body'])
print 'sparse matrix shape:', messages_bow.shape
print 'number of non-zeros:', messages_bow.nnz
print 'sparsity: %.2f%%' % (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1]))

tfidf_transformer = TfidfTransformer().fit(messages_bow)
tfidf4 = tfidf_transformer.transform(bow4)
print tfidf4

messages_tfidf = tfidf_transformer.transform(messages_bow)
print messages_tfidf.shape



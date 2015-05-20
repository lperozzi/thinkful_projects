
# coding: utf-8¨rR

# In[1]:

import pandas as pd
# remind: the column seems to be ordered alphabetically
df = pd.DataFrame({'Bear Market': [.8, .15, .05], 
                   'Bull Market': [.075, .9,.025],
                    'Stagnant Market':[.25,.25 ,.5]
                  }, 
                  index=["Bear Market", "Bull Market","Stagnant Market"])


# In[20]:

# LP # After 47 transition we have steady state probabilities 
n=47  # number of transition
for i in range(n-1):
    if i < 1:
        df1=df.dot(df)
        i=i+1
    else:
        df1=df1.dot(df)
        
print df1


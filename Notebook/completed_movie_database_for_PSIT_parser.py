#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import ast
import os
os.listdir(os.getcwd())


# In[2]:


director = pd.read_csv('directorparsed.csv')
meta = pd.read_csv('movies_metadata_small.csv')


# In[3]:


meta


# In[4]:


director


# In[5]:


list_o_tuples = []
numcount = 1
used_id = []

for i in range(len(director.index)):
    b_id = director.iloc[i]['id']
    for j in range(len(meta.index)):
        a_id = meta.iloc[j]['id']
        if a_id == b_id and a_id not in used_id:
            used_id.append(a_id)
            new_director = director.iloc[i]['director']
            genres = meta.iloc[j]['genres']
            title = meta.iloc[j]['title']
            revenue = meta.iloc[j]['revenue']
            vote_count = meta.iloc[j]['vote_count']
            vote_average = meta.iloc[j]['vote_average']
            list_o_tuples.append([b_id, new_director, title, genres, revenue, vote_count, vote_average])
            print(numcount)
            numcount += 1
            break
print("It's done bruh!")
            


# In[7]:


list_o_tuples


# In[6]:


cl = ["id", "director", "title", "genres", "revenue", "vote_count", "vote_average"]
ultimate = pd.DataFrame(list_o_tuples, columns=cl)
ultimate.to_csv('finalparsed.csv')


# In[4]:





# In[7]:


test = pd.read_csv('completed_movie_database_for_PSIT.csv')


# In[18]:


sample = {}
already = []
for x in range(len(test.index)):
    name = test.iloc[x]['director']
    networth = test.iloc[x]['revenue']
    if name not in already:
        sample[name] = networth
    else:
        sample[name] += networth
    print(sample.get(name))
print("yay")


# In[30]:


sorted_d = sorted(sample.items(), key=lambda x: x[1], reverse=True)
sorted_d


# In[38]:


test.loc[test['director'] == 'James Cameron', ['title', 'revenue', "vote_count", "vote_average"]]


# In[39]:


test.loc[test['director'] == 'J.J. Abrams', ['title', 'revenue', "vote_count", "vote_average"]]


# In[42]:


test.loc[test['director'] == 'Joss Whedon', ['title', 'revenue', "vote_count", "vote_average"]]


# In[43]:


test.loc[test['director'] == 'Jennifer Lee', ['title', 'revenue', "vote_count", "vote_average"]]


# In[52]:


test.loc[test['director'] == 'Bill Condon', ['title', 'revenue', "vote_count", "vote_average"]]


# In[53]:


test.loc[test['director'] == 'F. Gary Gray', ['title', 'revenue', "vote_count", "vote_average"]]


# In[54]:


test.loc[test['director'] == 'Joe Russo', ['title', 'revenue', "vote_count", "vote_average"]]


# In[55]:


test.loc[test['director'] == 'Lee Unkrich', ['title', 'revenue', "vote_count", "vote_average"]]


# In[56]:


test.loc[test['director'] == 'Gareth Edwards', ['title', 'revenue', "vote_count", "vote_average"]]


# In[57]:


test.loc[test['director'] == 'Angus MacLane', ['title', 'revenue', "vote_count", "vote_average"]]


# In[58]:


test.loc[test['director'] == 'Jared Bush', ['title', 'revenue', "vote_count", "vote_average"]]
# 11th


# In[51]:


test.loc[test['director'] == 'Jennifer Lee', ['title', 'revenue', "vote_count", "vote_average"]]
# 12th


# In[59]:


test


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
os.getcwd()


# In[ ]:





# In[2]:


os.listdir(os.getcwd())


# In[3]:


pd.read_csv('credits.csv')


# In[4]:


csvdf = pd.read_csv('credits.csv')


# In[5]:


csvdf.sample()


# In[6]:


csvdf.info()


# In[7]:


csvdf.drop(['cast'], axis=1, inplace=True)


# In[8]:


csvdf.sample()


# In[9]:


csvdf.to_csv('credit_lite.csv')


# In[10]:


newcsv = pd.read_csv('credits_lite.csv')


# In[11]:


newcsv


# In[12]:


import ast
cell_as_list = ast.literal_eval(newcsv.iloc[1]['crew'])
print(cell_as_list)


# In[22]:


testlist = []
mydict = {}
import numpy as np
for i in range(len(newcsv.index)):
    for j in ast.literal_eval(newcsv.iloc[i]['crew']):
        if j['job'] in ('Director', 'director'):
            print(j['name'], newcsv.iloc[i]['id'])
            mydict[newcsv.iloc[i]['id']] = j['name']
print("It's done Bruh")


# In[ ]:





# In[27]:


final = pd.DataFrame(list(mydict.items()), columns=['id', 'director'])


# In[28]:


final


# In[30]:


final.to_csv('directorparsed.csv')


# In[ ]:





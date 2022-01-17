#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)


# In[11]:


cpd = pd.read_excel(r"D:\Learnerea\Tables\diwali_spends_on_card.xlsx",sheet_name='data')
cpdMmb = cpd[cpd['city']=='Mumbai']


# In[12]:


scores = [88,89,90,92,95,98,99]
yourScore = 90
PercentileNeeded = 90


# In[39]:


def pRank(yourScore,socres):
    count=0
    for score in scores:
        if score <= yourScore:
            count+=1
        rank = count/len(scores)*100
    return rank


# In[40]:


pRank(yourScore,scores)


# In[42]:


def valueP(rank,scores):
    index = rank*len(scores)//100
    return scores[index-1]


# In[43]:


valueP(90,scores)


# In[44]:


cpd.head()


# In[47]:


sns.boxplot(data=cpd,y='tran_amt',x='city')


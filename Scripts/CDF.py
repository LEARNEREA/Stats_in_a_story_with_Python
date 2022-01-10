#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)


# In[65]:


cpd = pd.read_excel(r"D:\Learnerea\Tables\diwali_spends_on_card.xlsx",sheet_name='data')
cpdMmb = cpd[cpd['city']=='Mumbai']


# In[66]:


cpdMmb.head()


# In[67]:


cpdMmb.tran_amt.agg(['min','median','max','count'])


# In[68]:


def CheckCDF(sample,x):
    count=0.0
    for item in x:
        for value in sample:
            if value<=item:
                count+=1
        prob = count/len(sample)
        # return prob
        print("the Proportation of transaction amt <=", item, "is", prob)


# In[69]:


CheckCDF(cpdMmb.tran_amt,[6500])


# In[71]:


plt.figure(figsize=(15,5))

sns.ecdfplot(data=cpdMmb)


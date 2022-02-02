#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)


# In[10]:


cpd = pd.read_excel(r"D:\Learnerea\Tables\diwali_spends_on_card.xlsx",sheet_name='pyData')
cpd.head()


# In[24]:


cpd.groupby('city')['tran_amt2'].agg(['median'])


# In[25]:


plt.figure(figsize=(8,5))

sns.boxplot(data=cpd,y='tran_amt2',x='city',showmeans=True,meanprops={"markerfacecolor":'white'})


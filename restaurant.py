#!/usr/bin/env python
# coding: utf-8

# # To prepare the data Restaurant

# In[45]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[46]:


collected_data=pd.read_csv('work sheet for hotel suresh.csv')


# In[47]:


print(collected_data)


# In[48]:


print(collected_data.head())


# In[49]:


print(collected_data.tail())


# In[50]:


print(collected_data.shape)


# In[51]:


print(collected_data.info())


# In[52]:


print(collected_data.columns)


# In[53]:


print(collected_data.describe())


# In[54]:


print(collected_data.isnull())


# In[55]:


mean1=collected_data["Payment bill"].mean()


# In[56]:


print(mean1)


# In[57]:


mean2=collected_data["Tip"].mean()


# In[58]:


print(mean2)


# In[59]:


mean3=collected_data["Actual food bill"].mean()


# In[60]:


print(mean3)


# In[61]:


collected_data["Payment bill"].fillna(mean1,inplace=True)


# In[62]:


collected_data["Tip"].fillna(mean2,inplace=True)


# In[63]:


collected_data["Actual food bill"].fillna(mean3,inplace=True)


# In[64]:


print(collected_data)


# In[65]:


print(collected_data.info())


# In[66]:


print(collected_data.describe())


# In[67]:


print(collected_data.isnull())


# In[68]:


prepared_data=collected_data


# In[69]:


print(prepared_data)


# In[70]:


print(prepared_data.corr())


# In[71]:


print(sns.pairplot(data=prepared_data))


# In[72]:


print(prepared_data.head)


# In[73]:


predict_variable=prepared_data["Payment bill"]
print(predict_variable)


# In[74]:


print(predict_variable.head)


# In[75]:


tp=prepared_data["Tip"]
print(tp)


# In[76]:


print(tp.head)


# In[77]:


print(prepared_data.plot(kind='line',x='Payment bill',y='Tip',title='Payment bill vs Tip'))


# In[78]:


print(prepared_data.plot(kind='scatter',x='Payment bill',y='Tip',title='Payment bill vs Tip'))


# In[80]:


print(prepared_data.plot(kind='bar',x='item',y='Actual food bill',figsize=(10,10)))


# In[82]:


print(prepared_data.plot(kind='area',x='Payment bill',y='Actual food bill',title='Payment bill vs Actual food bill'))


# In[83]:


print(prepared_data.plot(kind='box',x='item',y='Actual food bill',title='item vs Actual food bill'))


# In[84]:


print(prepared_data.plot(kind='hist'))


# In[ ]:





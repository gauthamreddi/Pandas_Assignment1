#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[6]:


df


# In[14]:


df.fillna(0) inplace=True


# In[32]:


df["FlightNumber"].fillna(value=df["FlightNumber"] [0]+10, limit=1, inplace=True)
df["FlightNumber"].fillna(value=df["FlightNumber"] [2]+20, limit=1, inplace=True)


# In[31]:


df


# In[38]:


df["FlightNumber"].fillna(value=df["FlightNumber"] [0]+10, limit=1, inplace=True)
df["FlightNumber"].fillna(value=df["FlightNumber"] [2]+10, limit=1, inplace=True)


# In[39]:


df


# In[42]:


df[("FlightNumber")] = df[("FlightNumber")].astype(int)
df


# In[64]:


df[['To']] = df['From_To'].str.split(' ',expand=True)
df


# In[57]:


df['From_To'].str.split(' ',expand=True)
df


# In[69]:


df.drop(['FromTo','To'],axis=1)


# In[73]:


df.drop(columns=['FromTo', 'To'], inplace=True)


# In[74]:


df


# In[113]:


df['From_To'].str.split('_',1,expand=True)


# In[116]:


temp_data = pd.DataFrame(df['From_To'].str.split('_',n= 1).tolist(), columns = ['From','To'])
temp_data


# In[118]:


temp_data['From'] = temp_data['From'].str.capitalize()
temp_data['To'] = temp_data['To'].str.capitalize()
temp_data


# In[121]:


df.drop(columns=['From', 'To','From_To'], inplace=True)


# In[122]:


df


# In[123]:


temp_data


# In[135]:


data=pd.concat([temp_data,df],axis=1)
data


# In[143]:


Recent_delays = pd.DataFrame(data['RecentDelays'].tolist(),columns = ['delay_1', 'delay_2', 'delay_3'])
Recent_delays


# In[147]:


data.drop(['RecentDelays'], inplace=True,axis=1)
data


# In[149]:


data.insert(loc = 3, column='delay_1' , value=Recent_delays['delay_1'])
data.insert(loc = 4, column='delay_2' , value=Recent_delays['delay_2'])
data.insert(loc = 5, column='delay_3' , value=Recent_delays['delay_3'])
data


# In[ ]:





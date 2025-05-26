#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


df=pd.read_csv('../DataSets/Fleet Data.csv')
df


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


df=df.rename(columns={'Parent Airline':'Parent_Airline'})
df=df.rename(columns={'Aircraft Type':'Aircraft_Type'})
df=df.rename(columns={'Average Age':'Average_Age'})
df=df.rename(columns={'Unit Cost':'Unit_Cost'})
df=df.rename(columns={'Total Cost (Current)':'Total_Cost'})


# In[6]:


df


# In[7]:


df.Unit_Cost=df.Unit_Cost.replace("[$,]","",regex=True)
df.Total_Cost=df.Total_Cost.replace("[$,]","",regex=True)


# In[8]:


df


# In[9]:


cols = [var for var in df.columns if df[var].isnull().mean() >0.05 and df[var].isnull().mean() > 0]
cols


# In[10]:


df.isnull().mean()*100


# In[12]:


df['Current']=df.Current.fillna(value=df['Current'].mean())
df['Future']=df.Future.fillna(value=df['Future'].mean())
df['Historic']=df.Historic.fillna(value=df['Historic'].mean())
df['Total']=df.Total.fillna(value=df['Total'].mean())
df['Orders']=df.Orders.fillna(value=df['Orders'].mean())
df['Average_Age']=df.Average_Age.fillna(value=df['Average_Age'].mean())


# In[13]:


df.isnull().sum()


# In[14]:


df=df.dropna()


# In[15]:


df.isnull().sum()


# In[16]:


df['Unit_Cost']=df.Unit_Cost.astype("int64")


# In[17]:


df['Total_Cost']=df.Total_Cost.astype("int64")


# In[20]:


df.dtypes


# In[21]:


df.drop_duplicates()


# In[ ]:





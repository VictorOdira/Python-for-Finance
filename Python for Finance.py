#!/usr/bin/env python
# coding: utf-8

# ### Python for Finance: Get Stock Market Data

# Install pandas_datareader 

# In[28]:


get_ipython().system('pip install pandas_datareader')
get_ipython().system('pip install yfinance')
get_ipython().system('pip install plotly')


# Import modules that you are going to use

# In[1]:


import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt
import yfinance as yf


# In[2]:


end_date = dt.datetime.now()
start_date = dt.datetime(2000, 1, 1)        
end_date, start_date


# Select the stocks/ticker you like to analyse

# In[3]:


stocklist = ["CBA","NAB", "WBC", "ANZ" ]
stocks = [i +".AX" for i in stocklist]
stocks


# Call pandas_datareader module # 2 ways pdr.DataReader(stocks, "yahoo", start_date, end_date) or pdr.get_data_yahoo(stocks, start_date,end_date)

# In[4]:


yf.pdr_override()
df = pdr.get_data_yahoo(stocks, start_date,end_date)
df


# In[6]:


pd.set_option("display.max_rows", 5880)
pd.set_option("display.max_columns", 24)


# In[5]:


df.index


# In[11]:


df.describe()


# In[12]:


df.head()


# In[14]:


df.tail()


# In[15]:


df.columns


# In[17]:


df.info()


# In[9]:


Close =df.Close
Close.head()


# In[19]:


Close.tail()


# In[20]:


Close.describe()


# In[21]:


Close.describe(percentiles = [0.1, 0.5, 0.9])


# In[23]:


Close[Close.index > end_date - dt.timedelta(days = 500)].describe(percentiles = [0.1, 0.5, 0.9])


# In[27]:


Close.plot(figsize=(12,8))


# In[7]:


import plotly.offline as pyo
pyo.init_notebook_mode(connected = True)
pd.options.plotting.backend = "plotly"


# In[10]:


Close.plot()


# In[36]:


Close["CBA.AX"]


# In[37]:


Close["CBA.AX"].pct_change()


# In[11]:


Close["CBA.AX"].pct_change().plot(kind="hist")


# In[ ]:





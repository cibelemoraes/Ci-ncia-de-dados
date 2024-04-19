#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

from pandas import Serie, DataFrame


# In[4]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# In[7]:


dados = np.arange(8)


# In[8]:


dados


# In[9]:


dados.reshape((4,2))


# In[11]:


indice =['linnha 1','linha 2',,'linha 3','linha 4', 'linha 5','linha 6','linha 7','linha 8']
serie = Series(dados, index=indice)


# In[12]:


serie


# In[13]:


serie['linha 7']


# In[17]:


np.random.seed(25)
indice = ['linnha 1','linha 2','linha 3','linha 4','linha 5','linha 6']
colunas = ['coluna 1', 'coluna 2', 'coluna 3','coluna 4','coluna 5','coluna 6', ]
df = DataFrame(np.random.rand(36).reshape((6,6)),
index=indice,
columns=colunas)
df


# In[18]:


df.loc[['linha 2', 'linha 4'],['coluna 3', 'coluna 5']]


# In[ ]:





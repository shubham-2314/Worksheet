#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cmath

a = 1
b = 5
c = 6


# In[11]:


d = (b**2) - (4*a*c)


# In[12]:


sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# In[ ]:





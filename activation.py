#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

def sigmoid(z):
    """Compute sigmoid function of input z"""
    return 1.0 / (1.0 + np.exp(-z))

def tanh(z):
    """Compute hyperbolic tangent function of input z"""
    return np.tanh(z)
#testing function
z = np.array([4,5,6,7])
print(sigmoid(z))
print(tanh(z))


# In[ ]:





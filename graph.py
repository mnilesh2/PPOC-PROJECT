#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    """Compute sigmoid function of input z"""
    return 1.0 / (1.0 + np.exp(-z))

def tanh(z):
    """Compute hyperbolic tangent function of input z"""
    return np.tanh(z)

z = np.linspace(-10, 10, 100)

sigmoid_z = sigmoid(z)
tanh_z = tanh(z)

plt.plot(z, sigmoid_z, label='sigmoid')
plt.plot(z, tanh_z, label='tanh')
plt.legend()
plt.title('Graphs of sigmoid(z) and tanh(z) functions')
plt.xlabel('z')
plt.ylabel('Output')
plt.show()


# In[ ]:





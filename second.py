#!/usr/bin/env python
# coding: utf-8

# In[6]:



my_array = [1, 2, 5, 3]
# question no 04
addition = sum(my_array) 
subtraction = my_array[2] - my_array[1]  
multiplication = my_array[0] * my_array[3] 

print("Array:", my_array)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)


# In[1]:


import matplotlib.pyplot as plt
#question no 1
features = ['A', 'B', 'C']
values = [2, 3, 4]
colors = ['red', 'blue', 'green']

plt.bar(features, values, color=colors)

plt.xlabel('Features')
plt.ylabel('Values')
plt.title('Bar Graph')


plt.show()


# In[3]:


import matplotlib.pyplot as plt
#question no 03
points = [(0, 0), (1, 1), (2, 3), (3, 2)]
          
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]
plt.scatter(x_values, y_values, color='red')
for i in range(len(points) - 1):
    x_values = [points[i][0], points[i+1][0]]
    y_values = [points[i][1], points[i+1][1]]
    plt.plot(x_values, y_values, color='black')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Lines')
plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
data = {'features1':15,'features2':20,'features3':30}

# Create a bar chart of the data
ax = data.plot(kind='bar')

# Set the chart title and axis labels
ax.set_title('Sample Dataset')
ax.set_xlabel('Features')
ax.set_ylabel('Values')

# Show the plot
plt.show()


# In[ ]:





# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
data = {'features1':15,'features2':20,'features3':30}

# Create a bar chart of the data
ax = data.plot(kind='bar')

# Set the chart title and axis labels
ax.set_title('Sample Dataset')
ax.set_xlabel('Features')
ax.set_ylabel('Values')

# Show the plot
plt.show()


# In[10]:


import matplotlib.pyplot as plt

#Question no 02
data = {'features1': 10, 'features2': 15, 'features3': 7, 'features4': 20}

names = list(data.keys())
values = list(data.values())

plt.bar(names, values)
plt.xlabel('Values')
plt.ylabel('Features')
plt.title('Sample dataset')

plt.show()


# In[ ]:





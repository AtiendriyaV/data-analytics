#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[19]:


cars= pd.read_csv('C:/Users/student/Desktop/toyota.csv' , index_col=0 , na_values = ['??','???'])


# In[20]:


cars


# In[21]:


cars.columns


# In[12]:


cars.info


# In[22]:



from matplotlib import pyplot as plt 


# In[27]:


#using matlab

#create a figure and axis
fig,ax=plt.subplots()

#create a scatterplot
ax.scatter(cars['Age'],cars['Price'])
ax.set_title('Age vs Price')
ax.set_xlabel('Age')
ax.set_xlabel('Price')


# In[58]:


#use python library

plt.scatter(cars['Age'],cars['Price'])
plt.title('Age vs Price')
plt.xlabel('Age')
plt.ylabel('Price')


# In[61]:


colors={'Petrol':'r','Diesel':'b','CNG':'g'}

fig,ax=plt.subplots()
for i in range(len(cars['Age'])):
    ax.scatter(cars['Age'][i],cars['Price'][i],color=colors[cars['FuelType'][i]])
ax.set_title('Age vs Position')
ax.set_xlabel('Age')
ax.set_ylabel('Price')


# In[29]:


pd.value_counts(cars['FuelType'])


# In[38]:


#drops the value with NA from the database and resets the database index

cars.dropna(inplace=True)
cars.reset_index(drop=True, inplace=True)


# In[39]:


#showcase the dataset of the of the dataset uploaded

cars.info


# In[40]:


#used to display first five rows of the dataset

cars.head()


# In[42]:


cars.head(3)


# In[109]:


#bar chart

data = cars['FuelType'].value_counts()
x=data.index
y=data.values

plt.bar(x, y,)
plt.title("Fuel vs Price")
plt.xlabel("Fuel")
plt.ylabel("Price")

plt.show()


# In[90]:


X = list(cars['Age'])
Y = list(cars['Price'])


# In[91]:


plt.bar(X, Y, color='b')
plt.title("Age vs Price")
plt.xlabel("Age")
plt.ylabel("Price")

plt.show()


# In[92]:


colors={'Petrol':'r','Diesel':'b','CNG':'g'}


fig,ax=plt.subplots()
for i in range(len(cars['FuelType'])):
    ax.bar(cars['FuelType'][i],cars['Price'][i],color=colors[cars['FuelType'][i]])
    
    
Fuel = list(cars['FuelType'])
Charge = list(cars['Price'])

ax.set_title('FuelType vs Price')
ax.set_xlabel('FuelType')
ax.set_ylabel('Price')


# In[103]:


my = cars['FuelType'].value_counts()
my.index

x= my.index
y = my.values

plt.bar(X, Y)

plt.title("Fuel vs Price")
plt.xlabel("Fuel")
plt.ylabel("Price")

plt.show()


# In[107]:


c =['KM' , ['Price']]

x=range(50)
for i in c:
    plt.plot(x,cars[i].head(50))


# In[102]:


plt.hist(cars['Age'])
plt.title('frequence vs age')
plt.xlabel('Age')
plt.ylabel('frequency')


# In[ ]:





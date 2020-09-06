#!/usr/bin/env python
# coding: utf-8

# In[1]:


altitude=int(input("Please enter Altitude"))
print("altitude")


# In[2]:


if altitude==1000:
    print("Safe to land")
elif altitude>1000 and altitude<5000:
    print("Bring down to 1000")
else:
    print("Turn around")


# In[3]:


r=int(input("Enter range: "))
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)


# In[ ]:





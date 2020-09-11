#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Print the first ArmStrong number in the range of 1042000 to 702648265 and exit the loop as soon 
#as you encounter the first armstrong number.


# In[1]:


for n in range(1042000, 702648265):
  l = len(str(n))
  sum = 0
  temp = n
  
  while temp > 0:
    d = temp % 10
    sum += d ** l
    temp //= 10

  if n == sum:
    print(n)
    break


# In[ ]:





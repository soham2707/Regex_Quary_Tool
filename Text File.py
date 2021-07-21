#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[13]:


df=pd.read_csv('C:\\Users\\Randrita s\\Downloads\\cow1.txt')


# In[34]:


with open("C:\\Users\\Randrita s\\Downloads\\cow1.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
#print(content)
pattern = input('Enter word you want to change:')

# empty string
replace = input('Enter the new word:')
for i in content:
    #if i==pattern:
    new_string= re.sub(pattern,replace,i) 
    print(new_string)
   


# In[103]:


with open("C:\\Users\\Randrita s\\Downloads\\cow1.txt") as f:
    strs = f.readlines()
    #print(content)
#a=input('Enter the word : ')
a=input()
#x=r'{}'.format(a)
for i in strs:
    re.search(r'',i)
    match = re.search(r'\b{}\b'.format(a),i)
if match:
    print ("Found")
else:
    print ("Not Found")
    


# In[ ]:





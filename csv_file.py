#!/usr/bin/env python
# coding: utf-8

# In[30]:


import csv


# In[31]:


text = open("username.csv", "r")


# In[32]:


with open('username.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        print(line)


# In[33]:


#join() method combines all contents of  
# csvfile.csv and formed as a string 
text = ''.join([i for i in text])  
  


# In[52]:


# search and replace the contents 
origin_word=input('Enter the origin word :')
replaced_word=input('Enter the replaced word :')
text = text.replace('{}'.format(origin_word),'{}'.format(replaced_word))  
#text = text.replace("grey07", "grey")  
#text = text.replace("Grey", "White") 


# In[53]:


x = open("output.csv","w")
x.writelines(text)
x.close()


# In[54]:


with open('output.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        print(line)


# In[136]:


search_word =input('Enter the word you want to search : ')
flag=0
ls=[]
with open('username.csv','r') as csv_file:
    csv_reader1=csv.reader(csv_file)
    for line in csv_reader1:
        for word in line:
            a=word.split(';')
            #a=str(a)
            ls=ls+a
for item in ls:
    if item in search_word:
        print ('Found')
        break
else:
    print('Not Found')
        
    


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[16]:


#to find any string starting with x and ending with y.
x,y=input().split()
test_string = input()
n=len(test_string)
pattern ='^'+x+'.'*(n-2)+y+'$'
print(pattern)

result = re.match(pattern, test_string)


if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")


# In[17]:


# Program to extract numbers from a string

string = input('Enter Your text to print all the numbers in your text:')
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)


# In[18]:


#The re.split method splits the string where there is a match 
#and returns a list of strings where the splits have occurred.

string = input()
pattern = '\d+'

result = re.split(pattern, string) 
print(result)


# In[23]:


#replace:
import re
# multiline string
string =input()

# matches all whitespace characters
pattern = input('Enter word you want to change:')

# empty string
replace = input('Enter the new word:')

new_string = re.sub(pattern,replace, string) 
print(new_string)



# In[24]:


# url link 
s =input()
  
# finding the protocol  
obj1 = re.findall('(\w+)://',s) 
print('Protocol:',obj1) 
  
# finding the hostname which may 
# contain dash or dots 
obj2 = re.findall('://([\w\-\.]+)',s) 
print('Host:',obj2)


# In[29]:


#validating IP
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
Ip=input('Enter a IP address: ')
if(re.search(regex, Ip)): 
    print("Valid Ip address")  
          
else:
    print("Invalid Ip address") 


# In[30]:


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email=input('Enter a mail id: ')
if(re.search(regex,email)):
    print("Valid Email")  
          
else:
    print("Invalid Email")  


# In[32]:


string =input('Enter your text : ')
print(re.findall(r'"(.*?)"', string))


# In[33]:


#Search for the first white-space character in the string:

import re

txt = input()
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# In[39]:


#Make a search that returns no match:



txt = input()
k=input('enter the word you want to search : ')
x=re.search(k, txt)
if x:
    print('The word is in the text at position :',x.span())
else:
    print("The word is not found")


# In[2]:


#Text


# In[ ]:


#replace
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
   


# In[ ]:


#search
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
   


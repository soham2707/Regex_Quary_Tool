```python
import re
```


```python
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
```

    a b
    alsb
    ^a..b$
    <re.Match object; span=(0, 4), match='alsb'>
    Search successful.
    


```python
# Program to extract numbers from a string

string = input('Enter Your text to print all the numbers in your text:')
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)


```

    Enter Your text to print all the numbers in your text:I am 20 year's old.
    ['20']
    


```python
#The re.split method splits the string where there is a match 
#and returns a list of strings where the splits have occurred.

string = input()
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

```

    I am a good girl 20
    ['I am a good girl ', '']
    


```python
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



```

    I am a good girl
    Enter word you want to change:girl
    Enter the new word:boy
    I am a good boy
    


```python
# url link 
s =input()
  
# finding the protocol  
obj1 = re.findall('(\w+)://',s) 
print('Protocol:',obj1) 
  
# finding the hostname which may 
# contain dash or dots 
obj2 = re.findall('://([\w\-\.]+)',s) 
print('Host:',obj2)

```

    https://web.whatsapp.com/
    Protocol: ['https']
    Host: ['web.whatsapp.com']
    


```python
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
```

    Enter a IP address: 110.234.52.124
    Valid Ip address
    


```python
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email=input('Enter a mail id: ')
if(re.search(regex,email)):
    print("Valid Email")  
          
else:
    print("Invalid Email")  
```

    Enter a mail id: error@gmail.com
    Valid Email
    


```python
string =input('Enter your text : ')
print(re.findall(r'"(.*?)"', string))

```

    Enter your text : Coders "never" give up
    ['never']
    


```python
#Search for the first white-space character in the string:

import re

txt = input()
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
```

    be the best version of yourself
    The first white-space character is located in position: 2
    


```python
#Make a search that returns no match:



txt = input()
k=input('enter the word you want to search : ')
x=re.search(k, txt)
if x:
    print('The word is in the text at position :',x.span())
else:
    print("The word is not found")
```

    He is a good musician as well as good person
    enter the word you want to search : good
    The word is in the text at position : (8, 12)
    


```python
#Text
```


```python
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
   
```


```python
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
   
```

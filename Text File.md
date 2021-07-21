```python
import pandas as pd
```


```python
df=pd.read_csv('C:\\Users\\Randrita s\\Downloads\\cow1.txt')

```


```python
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

    Enter word you want to change:Cows
    Enter the new word:Dogs
    Dogs are herbivorous animals that feed on grasses and plants. Their bodies are large because of which they have enormous weights. To support this weight cowsÃ¢â‚¬â„¢ legs have hooves that have been made secure due to keratin in them. This allows them to walk correctly. We need cows for many purposes like food clothes and cosmetics. In food cows provide us with milk cheese butter and meat. They are terrestrial mammals and give birth to young ones known as calves. Dogs are diurnal animals and usually sleep at night. They have a great metabolism and require a lot of nutrition per day. The food of cows is referred to as fodder. Dogs are kept in farms where they are needed for providing milk. These are sensitive animals and need a clean and dry place for staying. Plenty of large farms provide them with proper hygienic conditions to live in and take care of their nutrition.
    


```python
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
    
```

    randrita
    Not Found
    


```python

```

#%% md

# ENPM 661 - Planning for Autonomous Robots

#%% md

## Project 0 - Introduction to Python

#%% md

### 1.0 Lists

#%% md

A list is a sequence of values. Lists need not be homogeneous always which makes it a most powerful tool in Python. Lists are mutable, and hence, they can be altered even after their creation. Lists in Python are ordered and have a definite count.The values in the list, also known as elements are enclosed in square brackets.For example : [25, 40, 50, 80]

#%% md

#### 1.1 Creating a List

#%%

#Creating a list of numbers and printing the second element:
num_list = [0, 1, 2, 3, 4, 5]

# Accessing and printing the second element
print(num_list[1])
# Indexing starts with 0!

#%% md

#### 1.2 Modifying the List

#%%

#Modifying the first element and printing the updating list
num_list[0] = 100
print(num_list)

#%% md

#### 1.3 Adding a new element to the List

#%%

# Adding number 10
num_list.append(10)
print(num_list)

#%% md

#### 1.4 Removing an element from the List

#%%

#Removing the last element
# Method 1 using the in-built pop function and accessing the last element with negative index:
num_list.pop(-1)
print(num_list)

#%%

# Method 2 by finding the index of the last element and deleting it:
del num_list[len(num_list)-1]
print(num_list)

#%% md

#### 1.5 Sorting the list

#%%

num_list.sort()
print(num_list)

#%% md

#### 1.6 Slicing the list
Lets print the second and third element

#%%

print(num_list[1:3])

#%% md

### Practice :
Create an empty list.\
Append the list using a for-loop with squares of numbers from 1 to 10.\
Sort and reverse the list.\
Delete the 7th and 8th element and print the list.


#%%
list = []
i=0
for i  in range(0,9):
    z= (i+1)^2
    list.append(z)
list.sort()
list.reverse()
del list[6]
del list[7]
print(list)


#%%



#%% md

### 2.0  Tuples
A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.

#### 2.1 Creating tuples

#%%

# An empty tuple 
empty_tuple = () 
print (empty_tuple) 

#%%

# Creating non-empty tuples 
  
# One way of creation 
tup = 'python', 'geeks'
print(tup) 
  
# Another for doing the same 
tup = ('python', 'geeks') 
print(tup)

#%% md

#### 2.2 Concatenation of Tuples

#%%

# Code for concatenating 2 tuples 
  
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
  
# Concatenating above two 
print(tuple1 + tuple2) 

#%% md

#### 2.3 Nesting of Tuples

#%%

# Code for creating nested tuples 
  
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
tuple3 = (tuple1, tuple2) 
print(tuple3) 

#%% md

#### 2.4 Repetition in Tuples

#%%

# Code to create a tuple with repetition 
  
tuple3 = ('python',)*3
print(tuple3)

#%% md

#### 2.5 Immutable Tuples

#%%

# Code to test that tuples are immutable (You will be getting an error message)
  
tuple1 = (0, 1, 2, 3) 
tuple1[0] = 4
print(tuple1)

#%% md

#### 2.6 Slicing in Tuples

#%%

# Code to test slicing 
  
tuple1 = (0 ,1, 2, 3) 
print(tuple1[1:]) 
print(tuple1[::-1]) 
print(tuple1[2:4])

#%% md

#### 2.7 Deleting a Tuple

#%%

# Code for deleting a tuple 
  
tuple3 = (0, 1) 
del tuple3 
print(tuple3)

#%% md

#### 2.8 Finding Length of a Tuple

#%%

# Code for printing the length of a tuple 
  
tuple2 = ('python', 'geek') 
print(len(tuple2))

#%% md

#### 2.9 Converting list to a Tuple

#%%

# Code for converting a list and a string into a tuple 
  
list1 = [0, 1, 2] 
print(tuple(list1)) 
print(tuple('python')) # string 'python' 

#%% md

#### 2.10 Tuples in a loop

#%%

#python code for creating tuples in a loop 
  
tup = ('ENPM661',) 
n = 5  #Number of time loop runs 
for i in range(int(n)): 
    tup = (tup,) 
    print(tup)

#%% md

#### 2.11 Using max() , min()

#%%

# A python program to demonstrate the use of  
# cmp(), max(), min() 
  
tuple1 = ('ENPM', '661') 
tuple2 = ('planning', "robots") 
 
print ('Maximum element in tuples 1,2: ' + 
        str(max(tuple1)) +  ',' + 
        str(max(tuple2))) 
print ('Minimum element in tuples 1,2: ' + 
     str(min(tuple1)) + ','  + str(min(tuple2))) 


#%% md

### 3.0 Dictionary
Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’.

A Dictionary in Python works similar to the Dictionary in a real world. Keys of a Dictionary must be unique and of immutable data type such as Strings, Integers and tuples, but the key-values can be repeated and be of any type.

#### 3.1 Creating a Dictionary
In Python, a Dictionary can be created by placing sequence of elements within curly {} braces, separated by ‘comma’. Dictionary holds a pair of values, one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable.

Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing to curly braces{}.

#%%

# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Creating a Dictionary  
# with Integer Keys 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
  
# Creating a Dictionary  
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
  
# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 


#%% md

#### 3.2 Nested Dictionary

#%%


# Creating a Nested Dictionary  
# as shown in the below image 
Dict = {1: 'Geeks', 2: 'For',  
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
  
print(Dict)  


#%% md

#### 3.3 Adding elements to a Dictionary
In Python Dictionary, addition of elements can be done in multiple ways. One value at a time can be added to a Dictionary by defining value along with the key e.g. Dict[Key] = ‘Value’. Updating an existing value in a Dictionary can be done by using the built-in update() method. Nested key values can also be added to an existing Dictionary.

Note- While adding a value, if the key value already exists, the value gets updated otherwise a new Key with the value is added to the Dictionary.

#%%


# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  
# Adding set of values  
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  
# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 
  
# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 


#%% md

#### 3.4 Accessing elements from a Dictionary
In order to access the items of a dictionary refer to its key name.Key can be used inside square brackets.There is also a method called get() that will also help in acessing the element from a dictionary.

#%%

# Python program to demonstrate   
# accesing a element from a Dictionary  
  
# Creating a Dictionary  
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict['name']) 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict[1]) 
  
# accessing a element using get() 
# method 
print("Acessing a element using get:") 
print(Dict.get(3)) 

#%% md

#### 3.5 Removing Elements from Dictionary
In Python Dictionary, deletion of keys can be done by using the del keyword. Using del keyword, specific values from a dictionary as well as whole dictionary can be deleted. Other functions like pop() and popitem() can also be used for deleting specific values and arbitrary values from a Dictionary. All the items from a dictionary can be deleted at once by using clear() method. Items in a Nested dictionary can also be deleted by using del keyword and providing specific nested key and particular key to be deleted from that nested Dictionary. Note- del Dict will delete the entire dictionary and hence printing it after deletion will raise an Error.

#%%


# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
        'B' : {1 : 'Geeks', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 
  
# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 
  
# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 
  
# Deleting a Key  
# using pop() 
Dict.pop(5) 
print("\nPopping specific element: ") 
print(Dict) 
  
# Deleting an arbitrary Key-value pair 
# using popitem() 
Dict.popitem() 
print("\nPops an arbitrary key-value pair: ") 
print(Dict) 
  
# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 

#%% md

#### 3.6 Dictionary Methods
##### 3.6.1 Copy()
They copy() method returns a shallow copy of the dictionary.

###### Syntax
dict.copy()

#%%

original = {1:'geeks', 2:'for'} 

## Write code to copy "original" dictionary and print the newly copied dictionary
directory1 = original.copy()
print(directory1)
#%% md

##### 3.6.2 clear()
The clear() method removes all items from the dictionary.

##### Syntax
dict.clear()

#%%

text = {1: "geeks", 2: "for"} 
  
# write the code to clear the content of the dictionary and then print the empty dictionary 
text.clear()
print(text)
#%% md

##### 3.6.3 pop()
Python pop() method removes an element from the dictionary. It removes the element which is associated to the specified key.

If specified key is present in the dictionary, it remove and return its value.

If the specified key is not present, it throws an error KeyError.

##### Syntax
dict.pop(key, def)

##### Parameters :
key : The key whose key-value pair has to be returned and removed.

def : The default value to return if specified key is not present.

#%%

# Python dictionary pop() Method  
# Creating a dictionary  
inventory = {'shirts': 25, 'paints': 220, 'shoes': 525, 'tshirts': 217}  
# Calling method  
element = inventory.pop('shoes')  
# Displaying result  
print(element)  

#%%

inventory = {'shirts': 25, 'paints': 220, 'tshirts': 217}  

# write code to get the value for the key 'shoes'. If the key is not is the dictionary return 100
element = inventory.pop('shoes')
if element == 0:
    print(100)
#%% md

##### 3.6.4 popitem()
popitem() method in dictionary helps to achieve similar purpose. It removes the arbitrary key-value pair from the dictionary and returns it as tuple.

##### Syntax
dict.popitem()

##### Parameters : None

Returns : A tuple containing the arbitrary key-value pair from dictionary. That pair is removed from dictionary.

#%%


test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" : 2 } 

  
# write the code using popitem() to return + remove arbitrary key value pair and print it 
print(test_dict.popitem())
#%% md

##### 3.6.5 get()
This method returns the value for the given key, if present in the dictionary. If not, then it will return None (if get() is used with only one argument).

##### Syntax
Dict.get(key, default=None)

#%%

dic = {"A":1, "B":2} 
print(dic.get("A")) 

# write the code to get the value for key 'C'. Print "Not found" if the key is not present
f = 0
f= dic.get("c")
if f == None
    print("NOt found")
#%% md

##### 3.6.6 values()
values() is an inbuilt method in Python programming language that returns a list of all the values available in a given dictionary.

##### Syntax
dictionary_name.values()

#%%

dictionary = {"A": 2, "B": 3, "C": 4} 

# write the code to print the values in the dictionary
print(dictionary.values())
#%% md

##### 3.6.7 update()
In Python Dictionary, update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.

##### Syntax
dict.update([other_dictionary])

Parameters: This method takes either a dictionary or an iterable object of key/value pairs (generally tuples) as parameters.

Returns: It doesn’t return any value but updates the Dictionary with elements from a dictionary object or an iterable object of key/value pairs.

#%%

# Dictionary with three items  
Dictionary1 = { 'A': 'Geeks', 'B': 'For', } 
Dictionary2 = { 'B': 'Geeks' } 
  
# Dictionary before Updation 
print("Original Dictionary:") 
print(Dictionary1) 

# Write the code to update "Dictionary1" with "Dictionary2" and print
Dictionary1.update([Dictionary2])
print(Ditionary1)
#%% md

### 4.0 Loop: 'for'

#%% md

#### Creating a new List with the name "my_list"

#%%

my_list = [1, 2, 3, 4, 'Python', 'is', 'neat']

#%% md

Iterating through each term in the List. Printing each element of the List

#%%

for item in my_list:
    print(item) 

#%% md

#### Syntax: "break"

Iterating through the list and if target value is reached, break.

This will break and terminate the loop when the required keyword is found.

#%%

for item in my_list:
    if item == 'Python':
        break
    print(item)

#%% md

#### Syntax "continue"

Iterating through the list, if target is reached, move on to the next element

The number '4' doesn't get printed

Continue to the next item without executing the lines occuring after continue inside the loop.

#%%

for item in my_list:
    if item == 4:
        continue
    print(item)

#%% md

#### Syntax "enumerate"

Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 

This enumerate object can then be used directly in for loops

#%%

for idx, val in enumerate(my_list):
    print('idx: {}, value: {}'.format(idx, val))

#%% md

#### Syntax "range"
To control the iterations of "for loop", range can be used.

#%%

for number in range(5):
    print(number)

#%%

for number in range(2, 5):
    print(number)

#%% md

The last number '2' specifies the step size of each iteration

#%%

for number in range(0, 10, 2):
    print(number)

#%% md

#### Create a list of strings based on a list of numbers
The rules:

If the number is a multiple of five and odd, the string should be 'five odd'

If the number is a multiple of five and even, the string should be 'five even'

If the number is odd, the string is 'odd'

If the number is even, the string is 'even'

(P.S. Refer textbook for mathematical operations - Section 2.5)

#%%

numbers = [1, 3, 4, 6, 81, 80, 100, 95]

#%%

# Your implementation
my_list = 

#%% md

Assert will cross check if the output generated is the required ouput. If not, it will throw an error

#%%

assert my_list == ['odd', 'odd', 'even', 'even', 'odd', 'five even', 'five even', 'five odd']

#%% md

### Loop: 'while'

With the while loop we can execute a set of statements as long as a condition is true.

The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

#%%

i = 1
while i < 6:
    print(i)
    i += 1

#%% md

With the break statement we can stop the loop even if the while condition is true:

#%%

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#%% md

With the continue statement we can stop the current iteration, and continue with the next:

#%%

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#%% md

With the else statement we can run a block of code once when the condition no longer is true:

#%%

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#%% md

## Plotting using Matplotlib

#%% md

matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

#%%

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

#%% md

#### Formatting the style of your plot
For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot. The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. The default format string is 'b-', which is a solid blue line. For example, to plot the above with red circles, you would issue

#%%

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

#%% md

If matplotlib were limited to working with lists, it would be fairly useless for numeric processing. Generally, you will use numpy arrays. In fact, all sequences are converted to numpy arrays internally. The example below illustrates a plotting several lines with different format styles in one command using arrays.

#%%

import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


#%%



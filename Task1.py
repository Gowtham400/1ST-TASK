#!/usr/bin/env python
# coding: utf-8

# # VARIABLES

# In[ ]:


#declaring variables
var1 = 7
var2 = 18

#swapping variables
var1,var2 = var2,var1

print("var1 = ",var1)
print("var2 = ",var2)


# # NUMBERS

# In[1]:


x=2
y=1.2
print("int(x)= ",int(x))
print("int(y)= ",int(y))
print("float(y)= ",float(y))


# # STRING

# In[2]:


s = "gowtham"
#last character
print(s[-1])
#slicing first two characters
print(s[2:])
#converting first character to upper case
print(s.capitalize())
#finding the character in string
print(s.index("a"))
#reversing
s = s[::-1]
print(s)


# # List

# In[3]:


list1 = [5,9,"cool",6,"sunny",2]
list2 = [21,48,63,22,43,17]
#adding string to the list at end
list1.append("21")
print(list1)
#popping the element
print(list1.pop(2))
#reversing
list2.reverse()
print(list2)
#sorting the elements in the list
list2.sort()
print(list2)


# # Dictionary

# In[6]:


employee ={
    "name" : "lucky",
    "age" : "25",
    "experience":"2 years",
    "company" : "cureya"
}
#getting specified value
print(employee.get("age"))

#all items in the dictionary
print(employee.items())

#popping the specified element
print(employee.pop("company"))


# # Tuples

# In[11]:


tup1 = 1,2,3
tup2 = ('thursday','friday',2,3)
#adding tuples
tup3 = (tup1 + tup2)
print(tup3)
#slicing
print(tup3[1:4])
#length of tuple
print(len(tup3))
#to find if a tuple or not
print(type(tup3))
#no.of times item occurs
print(tup3.count(3))
#deleting the tuple
del tup2
#now for printing tup3 tup2 need not to be defined
print(tup3)


# # if-statement

# In[12]:


import random
num1 = random.randint(0,99)
num2 = random.randint(0,99)

print('a=',num1 ,',' 'b=',num2)
#user expects the sum of random numbers
sum = eval(input("enter sum a+b: "))
result = num1 + num2
#if statement to state whether the user is right or wrong
if sum is result:
    print("TRUE")
else:
    print("False")


# # For-loop

# In[14]:


#a perfect number is the sum of its positive divisors
print(" The perfect numbers below 10000 are : ")
for i in range (1,10000):
    x=0
    for j in range (1,i):
        if i%j==0:
            x=x+j
    if x==i:
        print(i)


# # Arithmetic

# In[15]:


#dimensions of rectangle1
w1 = 4.1
l1 = 9
#dimensions of rectangle2
w2 = 3
l2 = 5.5

print("area of rectangle1 is ",w1*l1)
print("perimeter of rectangle1 is ",2*(l1+w1))

print("area of rectangle2 is ",l2*w2)
print("perimeter of rectangle2 is ",2*(l2+w2))

ratio = (w1*l1)/(w2*l2)
#to avoid decimal in ratio i'll convert it to integer
print("rectangle1 is ",int(ratio),"times bigger than rectangle2")


# # Numpy

# In[18]:


import numpy as np

a=np.array([[5,6,4],[1,2,3]])
print(np.shape(a))

b=np.reshape(a,(3,2))
print(b)


#maximum value along row
n=np.max(a,1)
print(n)
#max value along coloumn
k=np.max(a,0)
print(k)


# In[19]:


p=np.array([[1,3.2,3.4],[7,88.8,38.7]])
#rounding the elements to nearest integers
print(np.round(p))

q=np.array([[1,2,3],[45,5,6]])
#joining the two arrays along column
print(np.concatenate((p,q),axis=0))

#joining the two arrays along row
print(np.concatenate((p,q),axis=1))


# # Matplotlib

# In[20]:


import numpy as np
from matplotlib import pyplot as plt

a=np.array([1,2,3,4,5,6,7,8])

#declaring the equation
b=a**2+a*2+1

#defining the graph along both axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#naming the plot
plt.title('graph')

#assigning x,y axis values
plt.plot(b,a)
plt.show()


# In[22]:


import numpy as np
from matplotlib import pyplot as plt


no_of_mobiles=[1,3,4,7,5,10]
day=[1,2,3,4,5,6]

#assigning x,y axis values to bar graph
plt.bar(day,no_of_mobiles)
#naming the graph
plt.title('mobile sales')
plt.show()


# # Pandas

# In[30]:


import pandas as pd

#assigning dataset
data = {'mobile': ['apple',  'realme',  'Oneplus'],

        
'ratings': [5,4.5,4.8],

'sales': [207847528, 1303171035, 11190846]}

#setting the dataframe
df= pd.DataFrame(data,columns=['mobile',  'ratings',  'sales'])
print(df)


# In[ ]:





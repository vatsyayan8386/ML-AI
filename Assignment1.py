
# coding: utf-8

#         TASK 1
# Q2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

# In[1]:


import numpy as np
import pandas as pd


# In[6]:


num = ""
for i in range(2000,3200):
    if (i % 5 > 0) and (i % 7 == 0):
        num = num + str(i) + ", "
        
print("Numbers divisble by 7 but not a muliple of 5 : ", num);
            


# Q3. Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[26]:


Fname = input("Enter first name: ")
Lname = input("Enter last name: ")
Name = Fname + " " + Lname
Rname = ""
for i in Name:
    Rname = i + Rname

print(Rname)


Name_rev = Lname + " " + Fname
print(Name_rev)


# Q4. Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r^3

# In[11]:


import math as math
r = 12
V = (4/3) * math.pi * r**3
print("Volum of sphere: ", V)


#         TASK2
# Q1. Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[14]:


seq = input("Enter comma-separated number: ")

seq_list = list(seq.split(","))
print(seq_list)

type(seq_list)


# In[16]:


char = "*"

for i in range(1,10):
    if i < 6:
        print(char*i, '\n')
        num = i;
    else:
        num = num-1
        if num > 0:
            print(char*num, '\n')
            


# Q3. Write a Python program to reverse a word after accepting the input from the user.

# In[20]:


strng = "AcadGild"
RevStr = ""
for i in strng:
    RevStr = i + RevStr

print(RevStr)


# Q4. WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens

# In[25]:


print("WE, THE PEOPLE OF INDIA, \n \t having solemnly resolved to constitute India into a SOVEREIGN,\n \t \t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n \t \t  and to secure to all its citizens")


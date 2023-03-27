# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:18:54 2019

@author: luedern3
"""
###### Use the following line to get a piece of data from the User to complete the assignment
userIn = input()

# 1 Print what data type userIn is, using the type function: type()
print (type(userIn))

# 2 Create a variable that's 2 words, and set it equal to the length of the userIn variable using the
# length function: len()
twoWords = len(userIn)
print (twoWords)
print (type(twoWords))
#What data type is it?

# 3 Write a print statement, that will state the userInput variable, the length of it,
# as a valid sentence. You must use + concatenation syntax for credit
print ('userInput is ' + str(userIn) +' and the length is ' + str(twoWords))

##### Do not edit the enclosed area (Unless told). When you have answered the above,
# remove the triple quotes and run the code

import matplotlib.pyplot as plt
i = 0
x = []
y = []
while (i < 5):
   userInput = input('Write a word in the terminal ')
   x.append(userInput)
   y.append(len(userInput))
   i += 1

plt.bar(x,y, align='center')
plt.title('The Amount of Characters in each Word')

# 4 type plt. and scroll to find ylabel, click it use plt.title as a template and label the y axis
# Do the same for the xaxis
plt.ylabel('Number of characters')
plt.xlabel ("Word")
plt.bar(x,y, color="purple")

plt.title('title')
plt.xlabel('xlabel')
# Try adding some of your own flavor!



import math
inputOne = input("What is your first variable?")
inputTwo = input("What is your second variable?")

pythagoreanTheroem = math.sqrt((float(inputOne) **2) + (float(inputTwo) **2))
print("pythagoreanTheorem")
# Pythagorean's Theorem :  a2 + b2 = c2
# Ask a user for  a and b then solve for c

# To square something in python use the following schema: variable ** 2 ,

# To square root, use: math.sqrt(variable)
# print c

# Ask the user for c and a this time, and solve for b

# Print b
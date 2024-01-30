# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:32:48 2024

@author: USER
"""

import pandas
file=pandas.read_csv("country_data.csv")

print(file)
print(file.info())
print(file.info())


import pandas as pd

file = pd.read_csv("country_data.csv")
df = pd.DataFrame(file) # <- This line

print(df.describe())

#storing data
B1=30
B2=40
B3=30
B4=40

print(B1)
print(B2)

#using Lists
age=[30,40,30,49,22,35,22,46,29,25,39]
print(age)

#List indexesstart at 0which has teh value of 30
print(age[0])
print(age[1])
print(age[10])

#this will give an error as there is no value at index 11
print(age[11])


#Basic stats
age=[30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average=sum(age)/len(age)
print(average)

# Storing Text
C2 = "M"
C3 = "M"
C4 = "F"
print (C2)
print(C3)
print(C4)

#using Lists
gender=["M","M","F","M","F","F","F","M","M","F","M"]
print(gender)

print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])








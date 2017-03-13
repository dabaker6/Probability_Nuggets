# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:00:36 2017

@author: bakerda
"""

#Complete the mean function to make it return the mean of a list of numbers

data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]

def mean(data):
    x = sum(data)
    y = len(data)
    return x/y

print(mean(data1))

################################################################

def mean2(data):
    return sum(data1)/len(data1)

print (mean2(data1))
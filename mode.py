# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:05:43 2017

@author: bakerda
"""

#Complete the mode function to make it return the mode of a list of numbers
data1=[1,2,5,10,-20,5,5]
def mode(data):
    #Insert your code here
    x = 0
    for i in range (len(data)):
        xi = data.count(data[i])
        if xi > x:
            mode = data[i]    
            x = xi
    return mode
print(mode(data1))
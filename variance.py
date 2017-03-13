# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:31:11 2017

@author: bakerda
"""

#Complete the variance function to make it return the variance of a list of numbers
data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
def mean(data):
    return sum(data)/len(data)
def variance(data):
    #Insert your code here
    mu = mean(data)    
    ndata = []
    for i in range(len(data)):
        x = (data[i] - mu)**2
        ndata.append(x)
    return mean (ndata)
        
print(variance(data3))

##############################################################################

def mean2(data):
    return sum(data)/len(data)

def variance2(data):
    mu = mean2(data)
    #construct list in a single line
    #(x-mu)**2 is applied to every value x in the list data as it's looped over
    return mean([(x-mu)**2 for x in data])

print(variance2(data3))
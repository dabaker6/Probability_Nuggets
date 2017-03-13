# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:09:59 2017

@author: bakerda
"""

import math

#N = 30, 95% CI alpha = 1.96, 99% = 2.576, 98% = 2.326, 90% = 1.645

data = (0.79,0.7,0.73,0.66,0.65,0.7,0.74,0.81,0.71,0.7)

def mean(data):
    return sum(data)/len(data)

print (mean(data))

def variance(data):
    mu = mean(data)
    return mean([(x-mu)**2 for x in data])

def alpha(data):
    return 1.96
    
def CI(data):
    return alpha(data)*math.sqrt(variance(data)/len(data))
    
def test(data, h):
    m = mean(data)
    c = CI(data)
    return abs(m-h) <=c
   
h = .55   
   
print ("The mean is "+str(mean(data))+" +/- "+str(CI(data))+" therefore the null hypothesis is "+str(test(data,h)))
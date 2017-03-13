# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:02:00 2017

@author: bakerda
"""

import numpy as np

x = (0,1,2)
y = (0,2,2)

def sumofx(x):
    sumx = sum(x)

    return sumx
    

def sumofy(y):
    sumy = sum(y)

    return sumy   

    
def xi2(x):
    x = sum([i**2 for i in x])
    return x

def sumxiyi(x,y):
    sumxiyi = sum(np.multiply([i for i in x],[i for i in y]))
    return sumxiyi

def c(x,y):
    n = len(x)
    c = (1/n)*sumofy(y)-0.00143*((1/n)*sumofx(x))
    
    return c
    
def m(x,y):
    n = len(x)
    m = (sumxiyi(x,y)-(1/n)*(sumofx(x)*sumofy(y)))/(xi2(x)-(1/n)*sumofx(x)**2)
    return m
    
def predict(value,x,y):
    y = m(x,y)*value+c(x,y)
    return y
    
 
#print (sumofxy(x,y))
print (xi2(x))
print (sumxiyi(x,y))

print (c(x,y))


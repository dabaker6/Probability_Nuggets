# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:25:59 2017

@author: bakerda
"""

import numpy as np

def xbar(data):
    return sum(data)/len(data)
    
def reg(x,y):
    
    numer = sum(np.multiply([i-xbar(x) for i in x],[i-xbar(y) for i in y]))
    
    denom = sum([(i-xbar(x))**2 for i in x])

    m = numer/denom
    c = xbar(y)-(m*xbar(x))
    
    return m,c
    


x = (0,1,2)
y = (0,2,2)

print(reg(x,y))
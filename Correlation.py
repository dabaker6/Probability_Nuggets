# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:36:32 2017

@author: bakerda
"""
import numpy as np
import math

def xbar(data):
    return sum(data)/len(data)
    
def r(x,y):
    
    numer = sum(np.multiply([i-xbar(x) for i in x],[i-xbar(y) for i in y]))
    
    sumsqrdiff_x = sum([(i-xbar(x))**2 for i in x])
    sumsqrdiff_y = sum([(i-xbar(y))**2 for i in y])
    
    denom = math.sqrt(sumsqrdiff_x*sumsqrdiff_y)    
    
    print("numerator = "+str(numer))
    print("sumsqrdiff_x = "+str(sumsqrdiff_x))
    print("sumsqrdiff_y = "+str(sumsqrdiff_y))
      
    return numer/denom   
    
data_x = (2,4,6)
data_y = (8,14,26)

print("r = "+str(r(data_x,data_y)))

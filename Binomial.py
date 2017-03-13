# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:26:12 2017

@author: bakerda
"""

import math as mt

import matplotlib.pyplot as plt

def Binomial(N,p):
    Dist = [mt.factorial(N)/(mt.factorial(i)*(mt.factorial(N-i)))*mt.pow(p,i)*mt.pow(1-p,N-i) for i in range (1,N+1)]

    print(plt.bar(range(len(Dist)), Dist, color="blue"))
    
    i = 0
    
    while (sum(Dist[:i])) <0.1:
        i = i+1
    print("The greatest number in the critical zone is "+str(i-1)+" out of an N of "+str(N))
    
    #print(Dist)    
    
N = 10000
p = 0.495

Binomial(N,p)
    
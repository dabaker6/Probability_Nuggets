# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:02:53 2017

@author: bakerda
"""

#Complete the median function to make it return the median of a list of numbers
data1=[1,2,5,10,-20]
def median(data):
    sdata = sorted(data)
    #// indicates floor division in python 3
    return sdata[(len(data)-1)//2]

print (median(data1))

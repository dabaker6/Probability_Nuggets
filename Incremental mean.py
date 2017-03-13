# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:13:06 2017

@author: bakerda
"""

from __future__ import division

def mean(oldmean,n,x):
    #Insert your code here
    return ((oldmean*n)+x)/(n+1)

currentmean=10
currentcount=5
new=4

print (mean(currentmean,currentcount,new)) #Should print 9
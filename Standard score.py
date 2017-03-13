# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:16:57 2017

@author: bakerda
"""

def standardscore(x,u,sigma):
    z = (x-u)/sigma
    return z
    
print (standardscore(130,100,15))
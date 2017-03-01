# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:19:18 2016

@author: bakerda
"""

import random
import math

num = input("please enter a number: ")
num = int(num)

def seq(num):
    i=0
    while i < num:
        yield i
        i+=1
        
lin = []

for i in seq(num):
    i = str(i)
    i = i[:1]
    i = float(i)
    lin.append(i)

print("\n")
print("For the numbers in the linear sequence 1 to "+str(num)+", the distribution of numbers is:")
for i in range(1,10):
    print(str(i)+' = '+str("%.2f" % round( (lin.count(i)/float(num))*100,2))+"%")

print("\n")
input("Press enter to continue...")

def fibo(num):
    i=0
    x=1
    y=0
    z=0
    while i < num:
        yield z
        z = x + y
        x = y
        y = z
        i+=1

prime =[]

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False;
    return n>1;

for n in range(1,num):
    if isPrime(n):
        n = str(n)
        n = n[:1]
        n = float(n)
        prime.append(n)

plen = (len(prime))

print("\n")
print("There are "+str(plen)+" prime numbers in the range 0 to "+str(num)+", the distribution of these is:")
for i in range(1,10):
    print(str(i)+' = '+str("%.2f" % round( (prime.count(i)/float(plen))*100,2))+"%")
    
ben = []

for i in fibo(num):
    i = str(i)
    i = i[:1]
    i = float(i)
    ben.append(i)

print("\n")
print("For the first "+str(num)+" numbers in the fibonacchi sequence, the distribution of numbers is:")
for i in range(1,10):
    print(str(i)+' = '+str("%.2f" % round( (ben.count(i)/float(num))*100,2))+"%")

print("\n")
input("Press enter to continue...")




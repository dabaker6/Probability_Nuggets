# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:21:17 2017

@author: bakerda
"""

import random

nums = [1,2,3]
results = []

for i in range(0,9):
    results.append([])

    prize = random.choice(nums)
    guess = random.choice(nums)

    #print("guess is: "+str(guess))

    nums_update = [x for x in nums if x != guess]
    #print("Nums_update is: "+str(nums_update))

    host = random.choice(nums_update)
    #print("host is: "+str(host))

    if prize == guess:
        results[i].append(1)
    elif prize != guess:
        results[i].append(0)    

    nums_update2 = [x for x in nums_update if x != host]
    guess2 = nums_update2[0]

    if prize == guess2:
        results[i].append(1)
    elif prize != guess2:
        results[i].append(0)
    
print(results)





# Loop over rows.
for row in results:
    # Loop over columns.
    for column in row:
        print(column, end="")
    print(end="\n")
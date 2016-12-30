import itertools
import random
from random import randint
import timeit


def subsetsum(r, length, target):
    array = sorted(random.sample(range(r), length)) #create an array between 0 and r
    target = randint (0, target) #target can be between 0 and the target, comment this out to set the target specifically
    #target =  round ((sum (array))/3)

    start = timeit.default_timer()
    print (target, array) #print the target and array
    for i in range(0, len(array)+1):
        for subset in itertools.combinations(array, i): #for each subset
            print (subset)  #print the subset and the sum of it
            if sum (subset) == target: #check if the subset sum is equal to the target
                print ("Subset equals the target", (subset), (sum (subset))) #if it is print the subset
                stop = timeit.default_timer()
                print (stop - start) 
                return subset
    print ("Target not found")  #if the target hasn't been found by the end of the iteration
    stop = timeit.default_timer()
    print (stop - start) 

#range of array ints from 0 to *, array length, target range from 0 to r     
subsetsum(100,20,400)

import itertools
import random
from random import randint, sample
import timeit


def subsetsum(bitlength, length):

    max_n_bit_number = 2**bitlength-1 #the max bit length is 2*bitlength-1
    array = sorted( [ randint(0,max_n_bit_number) for i in range(length) ])#create a random sorted array
    target = randint(0,length*max_n_bit_number) #target is between 0 and the length*maxbitnumber
    #target = sum(sample(array, randint(0,n)))
    
    start = timeit.default_timer()#start timer
    print (target, array) #print the target and array

    if target > sum(array):
        print ("Target is greater than sum of array")
        return 0
    
    for i in range(0, len(array)+1):
        for subset in itertools.combinations(array, i): #for each subset
            print (subset)  #print the subset and the sum of it
            if sum (subset) == target: #check if the subset sum is equal to the target
                print ("Subset equals the target", (subset), (sum (subset))) #if it is print the subset
                stop = timeit.default_timer()
                print (stop - start) 
                return subset
    print ("Target not found")  #if the target hasn't been found by the end of the iterations
    stop = timeit.default_timer()
    print (stop - start)
    return 0


subsetsum(10,20)#bitlength and length of array

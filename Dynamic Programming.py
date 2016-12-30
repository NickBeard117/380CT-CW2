import random
from random import randint
import timeit

n = 26 #length of array
bitlength = 10 #specify bit length
max_n_bit_number = 2**bitlength-1 #the max bit length is 2*bitlength-1
array = sorted( [ randint(0,max_n_bit_number) for i in range(n) ])#create a random sorted array
target = randint(0,n*max_n_bit_number) #create a random target


print (array, target) #print the array and target

start = timeit.default_timer() #start time
def dynamic(array, i, target): #array, i for the location in the array, target
    if target == 0:
        return 1    
    else:
        if i >= len(array):
            if target == 0:
                return 1 #success
            else: #if the target is not equal to 0 (it hasn't been found)
                return 0 #fail

            
    iterations = dynamic(array, i + 1, target)
    iterations += dynamic(array, i + 1, target - array[i])
    return iterations #call the function again


print("Number of iterations: ", dynamic(array, 0, target)) # call function and print total number of iterations, 0 is a fail, anything above 0 is a success
stop = timeit.default_timer() #the stop time for the program
print (stop - start) #total runtime


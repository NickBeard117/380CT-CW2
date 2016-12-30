import random
from random import randint
import timeit

array = sorted(random.sample(range(50), 25)) #create an array between 0 and *. CHANGE the first value to increase the range and the second value to increase the list size
target = randint (0, 200) #target can be between * and the *
print (array, target) #print the array and target

start = timeit.default_timer() #start time
def dynamic(array, i, target): #array, i for the location in the array, target
    if i >= len(array):#if i is greater than the length of the array
        if target == 0: #and the target is equal to 0 (it has been found)
            return 1 #success
        else: #if the target is not equal to 0 (it hasn't been found)
            return 0 #fail
            
    iterations = dynamic(array, i + 1, target)
    iterations += dynamic(array, i + 1, target - array[i])
    return iterations #call the function again


print("Number of iterations: ", dynamic(array, 0, target)) # call function and print total number of iterations, 0 is a fail, anything above 0 is a success
stop = timeit.default_timer() #the stop time for the program
print (stop - start) #total runtime

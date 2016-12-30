import itertools
import random
from random import randint
import timeit

array = sorted(random.sample(range(50), 25)) #create an array between 0 and r
target = randint (0, 200) #target can be between 0 and the target, comment this out to set the target specifically
print (array, target)

start = timeit.default_timer()
def dynamic(array, i, target):
    if i >= len(array):
        if target == 0:
            return 1
        else:
            return 0
            
    iterations = dynamic(array, i + 1, target)
    iterations += dynamic(array, i + 1, target - array[i])
    return iterations


print("Number of iterations: ", dynamic(array, 0, target))
stop = timeit.default_timer()
print (stop - start) 

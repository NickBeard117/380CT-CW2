import random
from random import randint, sample
import timeit

n = 20
bitlength = 10 #specify bit length
max_n_bit_number = 2**bitlength-1 #the max bit length is 2*bitlength-1
array = sorted( [ randint(0,max_n_bit_number) for i in range(n) ])#create a random sorted array
target = randint(0,n*max_n_bit_number) #create a random target
#target = sum(sample(array, randint(0,n)))

count = 0 #checking how many times it loops
print (array, target) #print the array and target
start = timeit.default_timer() #start time

def dynamic(array, n, target, count):

    for i in range (n):
        count += 1
        
        #we add array[i] to each element of the array and the result is inc_array
        inc_array = [x+array[i] for x in array]
        #concatenate array and inc_array
        array = (array + inc_array)    
    
        #if an array element is greater than the target, remove it
        j=0
        while j <(len(array)):
            if array[j] > target:
                del array [j]
            else:
                j+= 1

        
        #check the array to see if the target has been found
        for k in range (len(array)):
            if array[k] == target or target == 0:
                print ('true')
                print ("Iterations: ",count)
                return 1
           
    print ("False. Iterations: ",count)
    


dynamic(array, n, target, count)

stop = timeit.default_timer() #the stop time for the program
print (stop - start) #total runtime



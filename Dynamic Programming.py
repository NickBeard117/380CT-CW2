import random
from random import randint, sample
import timeit

n = 10 #length of array
bitlength = 10 #bit length
max_n_bit_number = 2**bitlength-1 #the max bit length
array = sorted([randint(0,max_n_bit_number) for i in range(n)])#create a random sorted array

target = randint(0,n*max_n_bit_number) #create a random target
#target = sum(sample(array, randint(0,n-1))) #create a target that will return true

print ("Length of array: ",n, "Target: ", target,"\nArray: ",array)

start = timeit.default_timer() #start time

S = [[0 for x in range(n+1)] for y in range(target+1)]
for i in range (n+1):
    S[0][i] =1
for i in range (1, target+1):
    S[i][0] =0

for i in range (1, target+1):
    for j in range (1, n+1):
        S[i][j] = S[i][j-1]
        if (i >= array[j-1]):
            S[i][j] = S[i][j] or S[i-array[j-1]][j-1]

#for i in range (target+1):
    #for j in range (n+1):
      #print (S[i][j], end="")
    #print (" ")

if(S[target][n] == 1):
    print ("Target Found")
else:
    print ("Target Not Found")
    
stop = timeit.default_timer() #the stop time for the program    
print (stop - start) #total runtime



import itertools
import random
from random import randint, sample
import timeit

class SSP():

    def __init__(self, array=[], target=0):
        self.array = array
        self.target = target
        self.length = len(array)

    def random_true_array (self,bitlength, length):
        max_n_bit_number = 2**bitlength-1 #the max bit length is 2*bitlength-1
        self.array = sorted( [ randint(0,max_n_bit_number) for i in range(length) ])#create a random sorted array
        self.target = sum(sample(self.array, randint(0,length)))
        self.length = len(self.array)
        print ("Length of array: ",self.length, "Target: ", self.target,"\nArray: ",self.array)

    def random_array (self,bitlength, length):
        max_n_bit_number = 2**bitlength-1 #the max bit length is 2*bitlength-1
        self.array = sorted( [ randint(0,max_n_bit_number) for i in range(length) ])#create a random sorted array
        self.target = randint(0,length*max_n_bit_number) #target is between 0 and the length*maxbitnumber
        self.length = len(self.array)
        print ("Length of array: ",self.length, "Target: ", self.target,"\nArray: ",self.array)
     
    def exhaustive (self):
        start = timeit.default_timer()#start timer

        if self.target > sum(self.array):
            print ("Target is greater than sum of array")
            return 0
        
        for i in range(0, len(self.array)+1):
            for subset in itertools.combinations(self.array, i): #for each subset
                if sum (subset) == self.target: #check if the subset sum is equal to the target
                    print ("Subset equals the target", (subset), (sum (subset))) #if it is print the subset
                    stop = timeit.default_timer()
                    print (stop - start) 
                    return subset
        print ("Target not found")  #if the target hasn't been found by the end of the iterations
        stop = timeit.default_timer()
        print (stop - start)
        return 0

    def dynamic (self):
        start = timeit.default_timer() #start time
        
        S = [[0 for x in range(self.length+1)] for y in range(self.target+1)]
        for i in range (self.length+1):
            S[0][i] =1
        for i in range (1, self.target+1):
            S[i][0] =0

        for i in range (1, self.target+1):
            for j in range (1, self.length+1):
                S[i][j] = S[i][j-1]
                if (i >= self.array[j-1]):
                    S[i][j] = S[i][j] or S[i-self.array[j-1]][j-1]

        #for i in range (self.target+1):
            #for j in range (self.length+1):
              #print (S[i][j], end="")
            #print (" ")

        if(S[self.target][self.length] == 1):
            stop = timeit.default_timer() #the stop time for the program    
            print (stop - start) #total runtime
            print ("Target Found")
            return 1
        else:
            stop = timeit.default_timer() #the stop time for the program    
            print (stop - start) #total runtime
            print ("Target Not Found")
            return 0

instance = SSP()
instance.random_true_array(10,25)
instance.dynamic()


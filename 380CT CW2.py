import itertools
import random
from random import randint, sample
import timeit

class SSP():

    def __init__(self, S=[], target=0):
        self.S = S
        self.target = target
        self.length = len(S)

    def random_true_set (self,bitlength, length):
        max_n_bit_number = 2**bitlength-1 #the max bit length is 2*bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(length) ])#create a random sorted S
        self.target = sum(sample(self.S, randint(0,length)))
        self.length = len(self.S)
        print ("Length of set: ",self.length, "Target: ", self.target,"\nSet: ",self.S)

    def random_set (self,bitlength, length):
        max_n_bit_number = 2**bitlength-1 #the max bit length is 2*bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(length) ])#create a random sorted S
        self.target = randint(0,length*max_n_bit_number) #target is between 0 and the length*maxbitnumber
        self.length = len(self.S)
        print ("Length of set: ",self.length, "Target: ", self.target,"\nSet:\n",self.S)


     
    def exhaustive (self):
        start = timeit.default_timer()#start timer

        if special_cases(self, start) == 0: #check for special cases
            return 0

        for i in range(0, len(self.S)+1):
            for subset in itertools.combinations(self.S, i): #for each subset
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

        if special_cases(self, start) == 0: #check for special cases
            return 0
        
        S = [[0 for x in range(self.length+1)] for y in range(self.target+1)]
        for i in range (self.length+1):
            S[0][i] =1
        for i in range (1, self.target+1):
            S[i][0] =0

        for i in range (1, self.target+1):
            for j in range (1, self.length+1):
                S[i][j] = S[i][j-1]
                if (i >= self.S[j-1]):
                    S[i][j] = S[i][j] or S[i-self.S[j-1]][j-1]

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
        
def special_cases(self, start):
        #if the target is greater than the sum of the set, it cannot be exactly found
        if self.target > sum(self.S):
            print ("Target is greater than sum of set")
            stop = timeit.default_timer()
            print (stop - start)
            return 0
        #the same goes for when the target is less than the smallest value in the ser (but is not 0)
        if self.target < self.S[0] and self.target != 0:
            print ("Target is smaller than the smallest number in the set")
            stop = timeit.default_timer()
            print (stop - start)
            return 0

        #any values greater than the target should be ignored
        print("\nValues greater than the target are being deleted from the set")
        self.S = [x for x in self.S if x < self.target+1]
        self.length = len(self.S)
        print ("\nThe new S is:\n", self.S)
        
        #the target could be an element in the S already
        if self.target in self.S:
            print("\n \n Target is already in the set")
            stop = timeit.default_timer()
            print (stop - start)
            return 0
        


                

instance = SSP()
instance.random_set(20,25)
instance.exhaustive()


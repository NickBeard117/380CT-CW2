import itertools
import random
from random import randint, sample
import timeit
import bisect

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
        #print ("Length of set: ",self.length, "Target: ", self.target,"\nSet: ",self.S)

    def random_set (self,bitlength, length):
        max_n_bit_number = 2**bitlength-1 #the max bit length is 2*bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(length) ])#create a random sorted S
        self.target = randint(0,length*max_n_bit_number) #target is between 0 and the length*maxbitnumber
        self.length = len(self.S)
        #print ("Length of set: ",self.length, "Target: ", self.target,"\nSet:\n",self.S)

    def random_reverse_set (self,bitlength, length):
        max_n_bit_number = 2**bitlength-1 #the max bit length is 2*bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(length) ])#create a random sorted S
        self.S.reverse()
        self.target = randint(0,length*max_n_bit_number) #target is between 0 and the length*maxbitnumber
        self.length = len(self.S)
        #print ("Length of set: ",self.length, "Target: ", self.target,"\nSet:\n",self.S)

     
    def exhaustive (self):
        start = timeit.default_timer()#start timer

        #if instance.special_cases(start) == 0: #check for special cases
            #return 0

        for i in range(0, len(self.S)+1):
            for subset in itertools.combinations(self.S, i): #for each subset
                if sum (subset) == self.target: #check if the subset sum is equal to the target
                    #print ("Target found")
                    #print ("Subset equals the target", (subset), (sum (subset))) #if it is print the subset
                    stop = timeit.default_timer()
                    print (stop - start) 
                    return subset
        #print ("Target not found")  #if the target hasn't been found by the end of the iterations
        stop = timeit.default_timer()
        print (stop - start)
        return 0
    
    def dynamic (self):
        start = timeit.default_timer() #start time

        #if instance.special_cases(start) == 0: #check for special cases
            #return 0
        
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
        
    def greedy (self):
        start = timeit.default_timer()#start timer
        
        #if instance.special_cases(start) == 0: #check for special cases
           #return 0
        
        total = 0
        candidate = []
        used = []
  
        for i in range(0, len(self.S)):
            if self.S[i] + total <= self.target:
                total = total + self.S[i]
                used.append(self.S[i])
                
        stop = timeit.default_timer()
        

        #print ("\nThis is the closest to the total using greedy: ", total)
        #print ("Using these values: ", self.S)
        print ((total/self.target)*100 ,",",stop - start)


    def grasp (self):
        start = timeit.default_timer()#start timer
        
        #if instance.special_cases(start) == 0: #check for special cases
            #return 0
            
        best = []
        
        for k in range (10000):
            array = self.S[:]
            j = 0
            greedy = []
            grasp = []
            nd = []
            nu = []

            #this section creates the greedy array
            while j < len(array):
                candidate = random.choice(array)
                if sum(greedy)<self.target:
                    greedy.append(candidate)
                    array.remove(candidate)
                else:
                    j += 1
                
            if sum(best) == 0:
                best = greedy[:]

            #local search here
            if (random.randint(0, 1)) == 1:
                rnu = random.choice(greedy)
                nu = [x for x in array if x > rnu]
                if len(nu) > 0:
                    nu = nu[0]
                    greedy.remove(rnu)
                    greedy.append(nu)
                    array.remove(nu)
                    grasp = greedy[:]                
            else:
                rnd = random.choice(greedy)
                nd = [x for x in array if x < rnd]
                if len(nd) > 0:
                    nd = nd[len(nd)-1]
                    greedy.remove(rnd)
                    greedy.append(nd)
                    array.remove(nd)
                    grasp = greedy[:]
            #end of local search
            
            if abs(sum(grasp)-self.target) < abs(sum(best)-self.target):
                print (best, sum(best))
                best = grasp[:]
           
        #stop = timeit.default_timer()
        #print (sum(best), self.target)
        #print (sum(grasp))
        if ((sum(best)/self.target)*100)>100:
            print(200-((sum(best)/self.target)*100))
        else:
            print((sum(best)/self.target)*100)
        
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
            
            #the target could be an element in the set already
            if self.target in self.S or self.target == 0:
                print("\n \n Target is already in the set")
                stop = timeit.default_timer()
                print (stop - start)
                return 0
            
            #if all elements in the set are even, but the target is odd, it cannot be found
        


instance = SSP()
##instance.random_reverse_set(10,25)
##instance.grasp()

##for i in range(40, 41):
##    print("n =", i)
##    print ("\n\n")
for _ in range(1):
    instance.random_set(10,25)
    instance.grasp()
       


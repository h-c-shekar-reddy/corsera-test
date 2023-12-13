import numpy as np
import matplotlib.pyplot as plt
import copy

def coinFlip(p):    
    #perform the binomial distribution (returns 0 or 1)    
    result = np.random.binomial(1,p)  
    return result
#probability of heads vs. tails. This can be changed.
probability = .5
#declaring array size
n = 10000
q = 100
p = True
#initiate array
array1 = np.arange(n)
array2 = np.arange(q)
array3 = np.arange(q)
#perform desired numbered of flips at required probability set above
i = 0 
j = 0
k = True
l = 0
b = 0
while k == True :
    array1[i] = coinFlip(probability)    
    i+=1
    j+=1
    a = np.count_nonzero(array1 == 1)
    if(np.count_nonzero(array1 == 1) == 1000):
        print("Number of tries to get "+str(np.count_nonzero(array1 == 1))+" heads = "+ str(j))#STRING CONCATINATION
        array2[l] = int(np.count_nonzero(array1 == 1))
        array3[l] = int(j)
        k = False
    elif (np.count_nonzero(array1 == 1)%10 == 0) and (a != b):
        print("Number of tries to get "+str(np.count_nonzero(array1 == 1))+" heads = "+ str(j))
        b = np.count_nonzero(array1 == 1)
        array2[l] = int(np.count_nonzero(array1 == 1))
        array3[l] = int(j)
        l+=1

#print results
print("probability of getting Head or Tail ", probability)
#Tails = 0, Heads = 1

plt.plot(array2,array3)
plt.title('Coin Exp')
plt.xlabel('Number of Tries')
plt.ylabel('Average Time')
plt.show()
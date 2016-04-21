# version code 988
# Please fill out this stencil and submit using the provided submission script.

import sys
sys.path.append('../..')

import random
from itertools import combinations
from vec import *
from GF2 import one
from vecutil import list2vec
from independence import *



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = list2vec([ randGF2() for x in range(6) ])
        if a0*u==s and b0*u==t:
            return u

#print(choose_secret_vector(one, 0))

## Problem 2

def randGF2vec(vecLength=6):
    return list2vec([ randGF2() for x in range(vecLength)])
    
def findIndepedentTrio(vecLength=6, numPairs=4):
    while True:
        vecList = [(a0,b0)]+[ (randGF2vec(), randGF2vec()) for y in range(numPairs) ]
        independentSet = True
        
        for vecCombination in combinations(vecList, 3):
            subList = [ a for a,b in vecCombination ] + [ b for a,b in vecCombination ]
            if rank(subList)!=len(subList):
                independentSet = False
                break
                
        if independentSet:
            return vecList

indVecs = findIndepedentTrio()
for i, pair in enumerate(indVecs):
    print('secret_a%s = Vec(%s,%s)' % (i, pair[0].D, pair[0].f))
    print('secret_b%s = Vec(%s,%s)' % (i, pair[1].D, pair[1].f))

# Give each vector as a Vec instance
secret_a0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: 0, 5: one})
secret_b0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: 0, 5: one})
secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: 0, 4: 0, 5: one})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: 0, 4: 0, 5: one})
secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: 0, 4: one, 5: one})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: 0, 4: one, 5: one})
secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: one})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: one, 4: one, 5: 0})
secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: one, 4: one, 5: one})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: one, 5: one})










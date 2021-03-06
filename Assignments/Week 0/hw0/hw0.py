# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [ x for x in L if x % num!=0 ]



## Problem 2
def myLists(L): return [ list(range(1,x+1)) for x in L ]



## Problem 3
def myFunctionComposition(f, g): return { x:g[f[x]] for x in f.keys() }


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j
complex_addition_b = 1j
complex_addition_c = -1 + .001j
complex_addition_d = .001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    sum = 0
    for num in L:
        sum += num
    return sum



## Problem 7
def myProduct(L):
    prod = 1
    for num in L:
        prod *= num
    return prod
    


## Problem 8
def myMin(L):
    minVal = L[0]
    for num in L:
        if num < minVal:
            minVal = num
    return minVal
    


## Problem 9
def myConcat(L):
    retString = ''
    for string in L:
        retString += string
    return retString
    


## Problem 10
def myUnion(L):
    retSet = set()
    for setVal in L:
        retSet = retSet | setVal
    return retSet
    

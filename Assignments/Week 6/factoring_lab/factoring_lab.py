import sys
sys.path.append('../..')

from vec import Vec
from mat import Mat
from GF2 import one
from math import *
from matutil import *
from datetime import *

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod
from echelon import transformation_rows

import echelon

def root_method(N):
    for a in range(int(sqrt(N))+1, N):
        factor = sqrt(a*a-N)
        if factor==int(factor):
            print('root_method(%s):%s %s' % (N, a+factor, a-factor)) 
            return a-factor
    return(None)
    
# root_method(55)
# root_method(77)
# root_method(146771)
#root_method(118)

def checkEuclid(r,s,t):
    a = r*s
    b = s*t
    d = gcd(a,b)
    print('gcd of %s and %s is %s' % (a,b,d))
    print('%s/%s=%s, %s/%s==%s' % (a,d,a/d,b,d,b/d))
    print('d=%s, s=%s' % (d,s))
    
# N = 367160330145890434494322103
# a = 67469780066325164
# b = 9429601150488992

# print((a*a-b*b)/N)
# print(gcd(N, a-b), N/gcd(N, a-b))

# primeset = {2, 3, 5, 7, 11, 13}
# print(dumb_factor(12, primeset))
# print(dumb_factor(154, primeset))
# print(dumb_factor(2*3*3*3*11*11*13, primeset))
# print(dumb_factor(2*3*5*7*19, primeset))

## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    return 0 if i % 2==0 else one
    
# print('int2GF2(3):%s' % int2GF2(3))
# print('int2GF2(100):%s' % int2GF2(100))


## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset, { k:int2GF2(v) for k,v in factors })

# print(make_Vec({2,3,11}, [(2,3), (3,2)]))
# print(make_Vec({2,3,5,7,11}, [(3,1)]))
# print(make_Vec({2,3,5,7,11}, [(2,17), (3, 0), (5,1), (11,3)]))

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of prime
    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots = []
    rowlist = []
    a = intsqrt(N)+2
    while len(roots) < len(primeset)+1:
        primeFactors = dumb_factor(a*a-N, primeset)
        if len(primeFactors) > 0:
            roots.append(a)
            rowlist.append(make_Vec(primeset, primeFactors))
        a += 1
    return roots, rowlist

#print(2419, find_candidates(2419, primes(32)))

# print(gcd(53*77-2*3*3*5*13, 2419))
# print(gcd(52*67*71, 2*3*3*5*19*23))

## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist = [ roots[i] for i in v.D if v[i]==one]
    a = prod(alist)
    c = prod({ x*x-N for x in alist })
    b = intsqrt(c)
    return (a,b)
    
# N = 2419
# rowIndex = -2
# roots, rowlist = find_candidates(N, primes(32))
# M = transformation_rows(rowlist)
# print(roots, M[rowIndex])

# a,b = find_a_and_b(M[rowIndex], roots, N)
# print(a, b, a-b, gcd(a-b, N), N/gcd(a-b, N))

## Task 5
# N = 2461799993978700679
# rowIndex = -1
# roots, rowlist = find_candidates(N, primes(1000))
# M = transformation_rows(rowlist)
# print(roots, M[rowIndex])

# a,b = find_a_and_b(M[rowIndex], roots, N)
# print(a, b, a-b, gcd(a-b, N), N/gcd(a-b, N))

smallest_nontrivial_divisor_of_2461799993978700679 = 1230926561

print(datetime.now().time())
N = 20672783502493917028427
rowIndex = -1
roots, rowlist = find_candidates(N, primes(1000))
M = transformation_rows(rowlist)
print(roots, M[rowIndex])

a,b = find_a_and_b(M[rowIndex], roots, N)
print(a, b, a-b, gcd(a-b, N), N/gcd(a-b, N))
print(datetime.now().time())

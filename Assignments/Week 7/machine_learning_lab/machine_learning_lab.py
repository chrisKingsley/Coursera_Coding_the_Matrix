import sys
sys.path.append('../..')

from mat import *
from vec import *
from vecutil import *
from matutil import *
from cancer_data import *
import random

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    codomain = { k:1 if u.f.get(k,0)>=0 else -1 for k in u.D }
    return Vec(u.D, codomain)
    
#print(signum(Vec({'A','B','C'}, {'A':3,'B':-2,'C':0})))

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    '''
    dotProd = signum(A*w)*signum(b)
    return 0.5*(len(b.D)-dotProd)/len(b.D)

# A = listlist2mat([[2,4,3,5,0],[4,-2,-5,4,0],[-8,14,21,-2,0],[-1,-4,-4,0,0],[-2,-18,-19,-6,0],[5,-3,1,-5,2]])
# w = list2vec([1,-2,3,-4,5])
# b = list2vec([1,1,1,-1,-1,-1])
# print(fraction_wrong(A, b, w))

## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    resid = A*w-b
    return resid*resid

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    '''
    return 2*(A*w-b)*A

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    return w - sigma*find_grad(A,b,w)


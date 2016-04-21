# version code 1049
# Please fill out this stencil and submit using the provided submission script.

import sys
sys.path.append('../..')

from orthogonalization import orthogonalize
import orthonormalization
from QR import factor
from triangular import triangular_solve
from mat import Mat
from vec import Vec
from vecutil import list2vec
from matutil import *
from math import sqrt



## Problem 1
def basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - a list of linearly independent Vecs with equal span to vlist
    '''
    return [ x for x in orthogonalize(vlist) if x*x>1e-20 ]

# veclist = [[2,4,3,5,0],[4,-2,-5,4,0],[-8,14,21,-2,0],[-1,-4,-4,0,0],[-2,-18,-19,-6,0],[5,-3,1,-5,2]]
# for v in basis([ list2vec(x) for x in veclist ]):
    # print(v)

## Problem 2
def subset_basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - linearly independent subset of vlist with the same span as vlist
    '''
    return [ vlist[i] for i,x in enumerate(orthogonalize(vlist)) if x*x>1e-20 ]

# veclist = [[2,4,3,5,0],[4,-2,-5,4,0],[-8,14,21,-2,0],[-1,-4,-4,0,0],[-2,-18,-19,-6,0],[5,-3,1,-5,2]]
# for v in subset_basis([ list2vec(x) for x in veclist ]):
    # print(v)

## Problem 3
def orthogonal_vec2rep(Q, b):
    '''
    Input:
        - Q: an orthogonal Mat
        - b: Vec whose domain equals the column-label set of Q.
    Output:
        - The coordinate representation of b in terms of the rows of Q.
    Example:
        >>> Q = Mat(({0, 1}, {0, 1}), {(0, 1): 0, (1, 0): 0, (0, 0): 2, (1, 1): 2})
        >>> b = Vec({0, 1},{0: 4, 1: 2})
        >>> orthogonal_vec2rep(Q, b) == Vec({0, 1},{0: 8, 1: 4})
        True
    '''
    return Q*b

# Q = Mat(({0, 1}, {0, 1}), {(0, 1): 0, (1, 0): 0, (0, 0): 2, (1, 1): 2})
# b = Vec({0, 1},{0: 4, 1: 2})
# print(orthogonal_vec2rep(Q, b))
# Q=listlist2mat([[1/sqrt(2),1/sqrt(2),0],[1/sqrt(3),-1/sqrt(3),1/sqrt(3)],[-1/sqrt(6),1/sqrt(6),2/sqrt(6)]])
# b=list2vec([10,20,30])
# x = orthogonal_vec2rep(Q, b)
# print(Q, b, x, x*Q, b*Q.transpose(), Q*b)

## Problem 4
def orthogonal_change_of_basis(A, B, a):
    '''
    Input:
        - A: an orthogonal Mat
        - B: an orthogonal Mat whose column labels are the row labels of A
        - a: the coordinate representation in terms of rows of A of some vector v 
    Output:
        - the Vec b such that b is the coordinate representation of v in terms of columns of B
    Example:
        >>> A = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (2, 0): 0, (1, 0): 0, (2, 2): 1, (0, 2): 0, (2, 1): 0, (1, 1): 1})
        >>> B = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 2, (2, 0): 0, (1, 0): 0, (2, 2): 2, (0, 2): 0, (2, 1): 0, (1, 1): 2})
        >>> a = Vec({0, 1, 2},{0: 4, 1: 1, 2: 3})
        >>> orthogonal_change_of_basis(A, B, a) == Vec({0, 1, 2},{0: 8, 1: 2, 2: 6})
        True
    '''
    return a*A*B

# A = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (2, 0): 0, (1, 0): 0, (2, 2): 1, (0, 2): 0, (2, 1): 0, (1, 1): 1})
# B = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 2, (2, 0): 0, (1, 0): 0, (2, 2): 2, (0, 2): 0, (2, 1): 0, (1, 1): 2})
# a = Vec({0, 1, 2},{0: 4, 1: 1, 2: 3})
# print(orthogonal_change_of_basis(A, B, a))
# A=listlist2mat([[1/sqrt(2),1/sqrt(2),0],[1/sqrt(3),-1/sqrt(3),1/sqrt(3)],[-1/sqrt(6),1/sqrt(6),2/sqrt(6)]])
# a=list2vec([sqrt(2),1/sqrt(3),2/sqrt(6)])
# print(A, a, a*A*A)
#print(orthogonal_change_of_basis(A, A, a))

## Problem 5
def orthonormal_projection_orthogonal(W, b):
    '''
    Input:
        - W: Mat whose rows are orthonormal
        - b: Vec whose labels are equal to W's column labels
    Output:
        - The projection of b orthogonal to W's row space.
    Example: 
        >>> W = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (1, 0): 0, (0, 2): 0, (1, 1): 1})
        >>> b = Vec({0, 1, 2},{0: 3, 1: 1, 2: 4})
        >>> orthonormal_projection_orthogonal(W, b) == Vec({0, 1, 2},{0: 0, 1: 0, 2: 4})
        True
    '''
    return b-W*b*W

# W = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (1, 0): 0, (0, 2): 0, (1, 1): 1})
# b = Vec({0, 1, 2},{0: 3, 1: 1, 2: 4})
# print(orthonormal_projection_orthogonal(W, b))
# W = listlist2mat([[1/sqrt(2),1/sqrt(2),0],[1/sqrt(3),-1/sqrt(3),1/sqrt(3)]])
# b = list2vec([10,20,30])
# print(orthonormal_projection_orthogonal(W, b))

# v1, v2 = list2vec([1,1]), list2vec([2,1])
# v1_star, v2_star = orthogonalize([v1,v2])
# print(v1_star, v2_star, v1_star/sqrt(v1_star*v1_star), v2_star/sqrt(v2_star*v2_star))


## Problem 6
# Write your solution for this problem in orthonormalization.py.
# vecList = [ list2vec(v) for v in [[4, 3, 1, 2],[8, 9,-5,-5],[10, 1,-1, 5]] ]
# print(vecList, orthonormalization.orthonormalize(vecList))

## Problem 7
# Write your solution for this problem in orthonormalization.py.
# L = [list2vec(v) for v in [[4,3,1,2],[8,9,-5,-5],[10,1,-1,5]]]
# Qlist, Rlist = orthonormalization.aug_orthonormalize(L)
# print(coldict2mat(L))
# print(coldict2mat(Qlist))
# print(coldict2mat(Rlist))
# print(coldict2mat(Qlist)*coldict2mat(Rlist))
# print(coldict2mat(Qlist)*coldict2mat(Rlist)-coldict2mat(L))

## Problem 8
# Please give each solution as a Vec

def check(A,Q,R,b):
    c = Q.transpose()*b
    b_perp = b - b_parallel
    print(b_parallel, b_perp, b_parallel*b_perp)
    return b_perp
    
least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]]) 
least_squares_b1 = list2vec([10, 8, 6])

x_hat_1 = list2vec([1.08, 0.984])


least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

x_hat_2 = list2vec([2.5, 2.67])



## Problem 9
def QR_solve(A, b):
    '''
    Input:
        - A: a Mat
        - b: a Vec
    Output:
        - vector x that minimizes norm(b - A*x)
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR.factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result * result < 1E-10
        True
    '''
    Q,R = factor(A)
    c = Q.transpose()*b
    return triangular_solve(mat2rowdict(R), sorted(A.D[1],key=repr), c)

# A=Mat(({'a','b','c'},{'A','B'}), {('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1, ('c','B'):-2})
# b = Vec({'a','b','c'}, {'a':1,'b':-1})
# x = QR_solve(A,b)
# print(x)
# print(A.transpose()*(b-A*x))

# print(QR_solve(least_squares_A1, least_squares_b1))
# print(QR_solve(least_squares_A2, least_squares_b2))
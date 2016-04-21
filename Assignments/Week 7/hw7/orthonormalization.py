import sys
sys.path.append('../..')

from orthogonalization import orthogonalize
from math import sqrt
from matutil import *

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    return [ v/sqrt(v*v) for v in orthogonalize(L) ]


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    Q_mat = coldict2mat(orthonormalize(L))
    R_mat = Q_mat.transpose() * coldict2mat(L)
    return list(mat2coldict(Q_mat).values()), list(mat2coldict(R_mat).values())

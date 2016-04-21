
import sys

sys.path.append('../..')

from vec import Vec
from mat import Mat
from bitutil import *
from GF2 import one
from matutil import *
from vecutil import *

## Task 1 part 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""
G = listlist2mat([[one,0,one,one],[one,one,0,one],[0,0,0,one],[one,one,one,0],[0,0,one,0],[0,one,0,0],[one,0,0,0]])
#print(G)

## Task 1 part 2
# Please write your answer as a list. Use one from GF2 and 0 as the elements.
encoding_1001 = [0,0,one,one,0,0,one]
#print(G*list2vec([one,0,0,one]))

## Task 2
# Express your answer as an instance of the Mat class.
R = listlist2mat([[0,0,0,0,0,0,one],[0,0,0,0,0,one,0],[0,0,0,0,one,0,0],[0,0,one,0,0,0,0]])
#print(R)
#print(R*G)

## Task 3
# Create an instance of Mat representing the check matrix H.
H = listlist2mat([[0,0,0,one,one,one,one],[0,one,one,0,0,one,one],[one,0,one,0,one,0,one]])
#print(H*G)

## Task 4 part 1
def find_error(e):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        >>> find_error(Vec({0,1,2}, {2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        >>> find_error(Vec({0,1,2}, {1:one, 2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{2: one})    
    """
    index = [ sum([ 2**(2-k) for k,v in e.f.items() if v==one ])-1 ]
    codomain = { d:one for d in index if d>=0 }
    return(Vec(set(range(7)), codomain))
    
# print("one", find_error(Vec({0,1,2}, {0:one})))
# print(find_error(Vec({0,1,2}, {2:one})))
# print(find_error(Vec({0,1,2}, {1:one, 2:one})))

## Task 4 part 2
# Use the Vec class for your answers.
non_codeword = list2vec([one,0,one,one,0,one,one])
# print(non_codeword)
# print(H*non_codeword)
error_vector = find_error(H*non_codeword)
# print(error_vector)
code_word = error_vector + non_codeword
# print(code_word)
original = R * code_word
# print(original)


## Task 5
def find_error_matrix(S):
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
    """
    return coldict2mat({ k:find_error(v) for k,v in mat2coldict(S).items() })

# S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
# print(mat2coldict(S))
# M = Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
# print(find_error_matrix(S))
# print("find_error_matrix(S)==M : ", find_error_matrix(S)==M)

## Task 6
s = "I'm trying to free your mind, Neo. But I can only show you the door. You’re the one that has to walk through it."
P = bits2mat(str2bits(s))
E = noise(P, 0.02)
#print("original:%s\nerror:%s" % (s, bits2str(mat2bits(E+P))))

## Task 7
C = G*P
#print(C)
bits_before = len(mat2bits(P))
bits_after = len(mat2bits(C))
#print(bits_before)
#print(bits_after)

## Ungraded Task
CTILDE = C + noise(C, 0.02)
#print("original:%s\nerror:%s" % (bits2str(mat2bits(R*C)), bits2str(mat2bits(R*CTILDE))))

## Task 8
def correct(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: a matrix whose columns are the corresponding valid codewords.
    Example:
        >>> A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
        >>> correct(A)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
    """
    return find_error_matrix(H*A) + A
    
# A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
# M = Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
# print(A, correct(A), M)
# print("M==correct(A): %s" % (M==correct(A)))

print("original: %s\ncorrupted: %s\ncorrected: %s" % (s, bits2str(mat2bits(R*CTILDE)), bits2str(mat2bits(R*correct(CTILDE)))))

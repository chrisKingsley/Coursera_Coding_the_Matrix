

import sys
sys.path.append('../..')
sys.path.append('../../Week 4/geometry')

from mat import Mat
from vec import Vec
from image_mat_util import *
from solver import solve
from matutil import *
from vecutil import *

## Task 1
def move2board(v): 
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the 
          origin and q intersects the whiteboard plane at p.
    '''
    return Vec({'y1','y2','y3'}, {'y1':v['y1']/v['y3'], 'y2':v['y2']/v['y3'], 'y3':1})

## Task 2
def make_equations(x1, x2, w1, w2): 
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {('y3','x1'):x1*w1, ('y3','x2'):x2*w1, ('y3','x3'):w1, ('y1','x1'):-x1, ('y1','x2'):-x2, ('y1','x3'):-1})
    v = Vec(domain, {('y3','x1'):x1*w2, ('y3','x2'):x2*w2, ('y3','x3'):w2, ('y2','x1'):-x1, ('y2','x2'):-x2, ('y2','x3'):-1})
    return [u, v]


## Task 3
rowVecs = [None] * 9
rowVecs[0], rowVecs[1] = make_equations(358,36,0,0)
rowVecs[2], rowVecs[3] = make_equations(329,597,0,1)
rowVecs[4], rowVecs[5] = make_equations(592,157,1,0)
rowVecs[6], rowVecs[7] = make_equations(580,483,1,1)
rowVecs[8] = Vec(rowVecs[0].D, { ('y1', 'x1'):1 })
L = rowdict2mat(rowVecs)
#print(L)

b = list2vec( [0, 0, 0, 0, 0, 0, 0, 0, 1] )
h = solve(L, b)
#print(h, L*h)

H = Mat(({'y1', 'y2', 'y3'}, {'x1', 'x2', 'x3'}), h.f)
#print(H)

## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector 
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).
    '''
    # codomain = {}
    # for k,v in mat2coldict(Y).items():
        # codomain[ k ] = (1/v['y3'])*v
    # return coldict2mat(codomain)
    return coldict2mat({ k:(1/v['y3'])*v for k,v in mat2coldict(Y).items() })

# Y_in = Mat(({'y1', 'y2', 'y3'}, {0,1,2,3}),
# {('y1',0):2, ('y2',0):4, ('y3',0):8,
# ('y1',1):10, ('y2',1):5, ('y3',1):5,
# ('y1',2):4, ('y2',2):25, ('y3',2):2,
# ('y1',3):5, ('y2',3):10, ('y3',3):4})
# print(mat2coldict(Y_in))
# print(Y_in, mat_move2board(Y_in))

(X_pts, colors) = file2mat('board.png', ('x1','x2','x3'))
Y_pts = H * X_pts
Y_board = mat_move2board(Y_pts)

mat2display(Y_board, colors, ('y1', 'y2', 'y3'),
scale=100, xmin=None, ymin=None, browser='firefox')


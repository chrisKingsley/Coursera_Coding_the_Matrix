import sys
import sys
sys.path.append('../..')

from mat import Mat
from matutil import *
from image_mat_util import *
from math import *

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels, labels), { (a,a):1 for a in labels })
    
# idMat = identity()
# (imageMat, colMat) = file2mat('cit.png')
# #print(colMat)
# mat2display(idMat*imageMat, colMat, browser="firefox")
# input('hit return to continue')
# print(idMat*imageMat==imageMat)

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    transMat = identity()
    transMat[('x','u')] = x
    transMat[('y','u')] = y
    return transMat

# transMat = translation(10,20)
# print(transMat)
# (imageMat, colMat) = file2mat('cit.png')
# mat2display(imageMat, colMat, browser="firefox")
# mat2display(transMat*imageMat, colMat, browser="firefox")
# input('hit return to continue')

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    scaleMat = identity()
    scaleMat[('x','x')] = a
    scaleMat[('y','y')] = b
    return scaleMat
    
# scaleMat = scale(2,3)
# print(scaleMat)
# (imageMat, colMat) = file2mat('cit.png')
# mat2display(imageMat, colMat, browser="firefox")
# mat2display(scaleMat*imageMat, colMat, browser="firefox")
# input('hit return to continue')


## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    domain = ({'x','y','u'},{'x','y','u'})
    codomain = { ('x','x'):cos(angle),('x','y'):-sin(angle),('y','x'):sin(angle),('y','y'):cos(angle),('u','u'):1 }
    return Mat(domain, codomain)

# rotMat = rotation(pi/2)
# print(rotMat)
# (imageMat, colMat) = file2mat('cit.png')
# mat2display(imageMat, colMat, browser="firefox")
# mat2display(rotMat*imageMat, colMat, browser="firefox")
# input('hit return to continue')

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y) * rotation(angle) * translation(-x,-y)
    
# rotaboutMat = rotate_about(10,2,-pi/2)
# print(rotaboutMat)
# (imageMat, colMat) = file2mat('cit.png')
# mat2display(imageMat, colMat, browser="firefox")
# mat2display(rotaboutMat*imageMat, colMat, browser="firefox")
# input('hit return to continue')

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    reflectMat = identity()
    reflectMat[('x','x')] = -1
    return reflectMat

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    reflectMat = identity()
    reflectMat[('y','y')] = -1
    return reflectMat
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    return Mat(({'r','g','b'},{'r','g','b'}), { ('r','r'):scale_r,('g','g'):scale_g,('b','b'):scale_b })

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    scales = { 'r':77/256, 'g':151/256, 'b':28/256 }
    codomain = { (x,y):scales[y] for x in scales for y in scales } 
    return Mat(({'r','g','b'},{'r','g','b'}), codomain)

#print(grayscale())

## Task 10
def reflect_about(x1,y1,x2,y2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    if x2==x1:
        return translation(x2,0)*reflect_y()*translation(-x2,0)
    
    m =(y2-y1)/(x2-x1)
    b = y2-x2*m 
    return rotate_about(0,b,atan(m)-pi/2)*reflect_y()*rotate_about(0,b,pi/2-atan(m))


# reflectaboutMat = reflect_about(217,159,600,0)
# print(reflectaboutMat)
# (imageMat, colMat) = file2mat('cit.png')
# mat2display(imageMat, colMat, browser="firefox")
# mat2display(reflectaboutMat*imageMat, colMat, browser="firefox")
# input('hit return to continue')
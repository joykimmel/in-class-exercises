#prints vector magnitude and a dot product from two arrays. 
#utilizes 2 menthods for finding magnitude and dot product

from numpy import *
from math import *

def vector():
  d1 = array([3,-4,2],float)
  d2 = array([2,1,-1.5],float)

  #method 1 for finding magnitude ~ transpose, and then squareroot the dotproduct of the vector and its transpose
  mag1 = transpose(d1)
  print "method1"
  print "magnitude vector 1: %s" % (sqrt(dot(d1,mag1)))
  
  mag2 = transpose(d2)
  print "magnitude vector 2: %s" % (sqrt(dot(d2,mag2)))

  #method 2, square the individual elements of each array and squareroot it
  print 
  magnituded1 = sqrt(d1[0]*d1[0] + d1[1]*d1[1] + d1[2]*d1[2])
  magnituded2 = sqrt(d2[0]*d2[0] + d2[1]*d2[1] + d2[2]*d2[2])

  print "method 2: magnitude 1 and 2"
  print magnituded1
  print magnituded2

  print "dot product: 2 methods for calculating dot product"
  print dot(d1,d2)
  print d1[0]*d2[0] + d1[1]*d2[1] + d1[2]*d2[2]

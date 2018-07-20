# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:16:35 2018

@author: evan9
"""

import numpy as np

np.random.seed(0)

#1-dimension array
x1 = np.random.randint(10, size=6)
print(x1)
#2-dimension array
x2 = np.random.randint(10, size=(3,4))
print(x2)
#3-dimension array
x3 = np.random.randint(10, size=(3,4,5))
print(x3)


#How many dimensions
print('ndim:', [i.ndim for i in [x1,x2,x3]], [type(i.ndim) for i in [x1,x2,x3]])
#Shape of array
print('shape:', [i.shape for i in [x1,x2,x3]], [type(i.shape) for i in [x1,x2,x3]])
#How many items
print('size:', [i.size for i in [x1,x2,x3]], [type(i.size) for i in [x1,x2,x3]])
#Data type in array
print('dtype:', [i.dtype for i in [x1,x2,x3]], [type(i.dtype) for i in [x1,x2,x3]])
#Data size (bytes) in each item
print('itemsize:', [i.itemsize for i in [x1,x2,x3]], [type(i.itemsize) for i in [x1,x2,x3]])
#Data size (bytes) in whole array = size * itemsize
print('nbytes:', [i.nbytes for i in [x1,x2,x3]], [type(i.nbytes) for i in [x1,x2,x3]])




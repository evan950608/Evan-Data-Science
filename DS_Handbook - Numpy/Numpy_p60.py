# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 20:30:38 2018

@author: evan9
"""

import numpy as np


a = np.random.random(100)
print(np.sum(a), a.sum())
print(np.max(a), a.max())
print(np.min(a), a.min())
print('----------')

b = np.random.random((3,5))
print('b=', b, sep='\n')
print(b.sum())
print(b.max(axis=0))    #column
print(b.max(axis=1))    #row
print(np.prod(b))
print(np.mean(b))
print(np.std(b))
print(np.var(b))
print(np.argmax(b))
print(np.argmin(b))
print(np.median(b))
#numpy.percentile(a, q, axis=None, out=None, overwrite_input=False, interpolation='linear', keepdims=False)
print(np.percentile(b, 75))
#Compute the qth percentile of the data along the specified axis.
#Returns the qth percentile(s) of the array elements.
print('----------')

c = np.zeros((2,2))
d = np.array([[1, 0],
              [0, 1]])
#d = np.eye(2)
e = np.array([[1, 1],
              [1, 1]])
print(np.any(c))
print(np.any(d))
print(np.any(e))
print(np.all(c))
print(np.all(d))
print(np.all(e))
print('----------')








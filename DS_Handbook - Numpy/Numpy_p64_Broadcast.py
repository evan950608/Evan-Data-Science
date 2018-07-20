# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 15:53:33 2018

@author: evan9
"""

import numpy as np

a = np.array([0, 1, 2])
print(a + 5)
print(a + np.array([5, 5, 5]))
b = np.ones((3,3))
print(b + 5)
print(b + a)
c = np.arange(3)
d = np.arange(3)[:, np.newaxis]
print(c)
print(d)
print(c + d)
print('----------')

e = np.ones((2,3))    #shape (2,3)
f = np.arange(3)      #shape (3,) (1,3) (2,3)
print(e)
print(f)
print(e + f)
print('----------')

g = np.arange(3).reshape((3,1))    #shape (3,1)      (3,3)
h = np.arange(3)                   #shape (3,) (1,3) (3,3)
print(g)
print(h)
print(g + h)
print('----------')

i = np.ones((3,2))    #shape (3,2)
j = np.arange(3)      #shape (3,)  (1,3) (3,3)
print(i)
print(j)
#print(i + j)    #traceback
print('----------')

k = np.random.random((10,3))
print(k)
k_avg = k.mean()
k_avg_cln = k.mean(0)    #average of each column    #return a (1,3) array
k_avg_row = k.mean(1)    #average of each row       #return a (10,) array
print(k_avg)
print(k_avg_cln)
print(k_avg_row.reshape((10,1)))
### subtract column average from each number ###
k_centered = k - k_avg_cln
print(k_centered)
print(k_centered.mean(0))    #Approaches zero
print('----------')












# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 21:16:15 2018

@author: evan9
"""

import numpy as np

r = np.random.RandomState(0)
x = r.randint(10, size=(3,4))
y = x < 6
print(x)
print(y)
print(y.dtype)
print(np.sum(y))
print(np.count_nonzero(y))
print(np.sum(y, axis=1))

print(np.any(x > 5))
print(np.all(x > 5))
print(np.all(x < 8, axis=0))

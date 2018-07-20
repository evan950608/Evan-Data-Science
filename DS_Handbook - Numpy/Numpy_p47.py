# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 17:19:31 2018

@author: evan9
"""

import numpy as np

np.random.seed(0)
x2 = np.random.randint(10, size=(5,5))
print(x2)

x2_slct = x2[1:4, 2:4]
print(x2_slct)
x2_rev = x2[::-1, ::-1]
print(x2_rev)

x2_slct[0, 1] = 99
print(x2_slct)
print(x2)

x2_copy = x2[1:4, 2:4].copy()
x2_copy[1, 0] = 88
print(x2_copy)
print(x2)


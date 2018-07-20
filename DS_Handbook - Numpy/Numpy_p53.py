# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:02:05 2018

@author: evan9
"""

import numpy as np
import math

a = np.arange(5)
b = np.arange(1, 6)
print(a / b)
print('----------')

c = np.arange(16).reshape((4,4))
print(c)
print(c**2)
print(2**c)
print('----------')

x = np.arange(4)
print(x)
print(x + 5)
print(np.add(x, 5))
print(x - 5)
print(np.subtract(x, 5))
print(x * 2)
print(np.multiply(x, 2))
print(x / 2)
print(np.divide(x, 2))
print(x // 2)
print(np.floor_divide(x, 2))
print(x % 2)
print(np.mod(x, 2))
print(-x)
print(np.negative(x))
print(x ** 3)
print(np.power(x, 3))
print('----------')

y = np.arange(-2, 3)
print(y)
print(abs(y))
print(np.abs(y))
print(np.absolute(y))
z = np.array([3 + 4j, 12 - 5j, math.sqrt(3) + 1j])
print(abs(z))
print('----------')

theta = np.linspace(0, np.pi, 3)    #[0, 0.5pi, pi]
print(np.sin(theta))
print(np.cos(theta))
print(np.tan(theta))
value = np.array([0.5, 0.5 * math.sqrt(2), 1, 0.6])
print(np.arcsin(value) * (180/math.pi))
print(np.arccos(value) * (180/math.pi))
print(np.arctan(value) * (180/math.pi))
print('----------')

d = np.array([1, 2, 3])
print('e ** x=', np.exp(d))
print('e ** x=', np.power(math.e, d))
print('2 ** x=', np.exp2(d))
print('2 ** x=', np.power(2, d))
print('3 ** x=', np.power(3, d))
print('----------')

e = np.array([1, 2, 4, 10])
print('ln(x)=', np.log(e))    #log(e)(x) = ln(x) = np.log(x)
print('log2(x)=', np.log2(e))
print('log(x)=', np.log10(e))
print('----------')

f = np.arange(5)
g = np.empty(5)
np.multiply(f, 10, out=g)
print(g)
h = np.multiply(f, 10)
print(h)
i = np.zeros(10)
np.power(f, 2, out=i[::2])
print(i)
print('----------')

j = np.arange(1, 6)
print(np.add.reduce(j))
print(np.multiply.reduce(j))
print(np.add.accumulate(j))
print(np.multiply.accumulate(j))
print('----------')

print(np.multiply.outer(j, j))





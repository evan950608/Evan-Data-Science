# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:28:38 2018

@author: evan9
"""

import numpy

'''
grid = numpy.arange(1,13).reshape((4,3))
print(grid)
print(grid[1,1])

x1 = numpy.arange(1,4)
print(x1)
print(x1[numpy.newaxis, :])
print(x1.reshape(1,3))
print(x1[:, numpy.newaxis])
print(x1.reshape(3,1))
'''

#Merge
print('### Merge ###')
a = numpy.array([1,2,3])
b = numpy.array([3,2,1])
print(numpy.concatenate([a, b]))
print(numpy.concatenate([b, a]))
c = numpy.array([a, b])
print(c)
print(numpy.concatenate([c, c]))
print(numpy.concatenate([c, c], axis=1))

d = numpy.array([[4, 5, 6],
                 [7, 8, 9]])
print('d.shape', d.shape)
e = numpy.array([[10, 11, 12],
                 [13, 14, 15]])
print('e.shape', e.shape)
vst = numpy.vstack([d, e])
print(vst)
print('vst.shape', vst.shape)
hst = numpy.hstack([d, e])
print(hst)
print('hst.shape', hst.shape)
dst = numpy.dstack([d, e])
print(dst)
print('dst.shape', dst.shape)

print(dst[:, :, 0])
print(dst[:, :, 1])
print(vst[:2, :])
print(hst[:, :3])


#Split
print('### Split ###')
f = [1, 2, 3, 99, 99, 3, 2, 1]
f1, f2, f3 = numpy.split(f, [3, 5])
print(f1, f2, f3)

g = numpy.arange(25).reshape((5,5))
g1, g2 = numpy.vsplit(g, [3])
print(g1, '\n', g2, sep='')
g3, g4 = numpy.hsplit(g, [2])
print(g3, '\n', g4, sep='')

h = numpy.arange(64).reshape((4,4,4))
h1, h2 = numpy.hsplit(h, [2])
print(h)
print(h1, '\n\n', h2, sep='')





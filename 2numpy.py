# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:25:22 2021

@author: Caroline
"""

import numpy as np

a= [[11,12,13],[21,22,23],[31,32,33]]

b=np.array(a)

print(b)
print(b.ndim)
print(b.shape)
print(b.size)

#X=np.array([[1,0,1],[2,2,2]]) 
#out=X[0,1:3]
#print(out)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]]) 
Z=np.dot(X,Y)
print(Z)
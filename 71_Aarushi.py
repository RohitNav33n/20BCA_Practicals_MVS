# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:50:43 2021

@author: user
"""

import numpy as np
X = np.array([1,2,3,4,5,6,7])
print(X)
print(X[1])
print(X[3])
print(X[6])
print(np.shape(X))
X=np.array([1,2,3,4,5,6,7]).T
print(X)
Matrix = np.array([[1,2,3,4,5],[6,7,8,9,1],[5,4,3,9,2],[9,5,1,8,2]])
print(Matrix)
print(np.shape(Matrix))
print((Matrix).T)
print(Matrix[:,0])
print(Matrix[0,:])
print(np.zeros(7))
print(np.zeros(3))
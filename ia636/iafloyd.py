# -*- encoding: utf-8 -*-
# Module iafloyd

from numpy import *

def iafloyd(f):
    from ianormalize import ianormalize

    f_ = 1.*ianormalize(f, [0,255])
    g = zeros(f_.shape)
    for i in range(f_.shape[0]):
        for j in range(f_.shape[1]):
            if f_[i,j] >= 128:
                g[i,j] = 255
            erro = f_[i,j] - g[i,j]
            if j < f_.shape[1]-1:
                f_[i,j+1] = f_[i,j+1] + 7*erro/16.
            if i < f_.shape[0]-1 and j > 0:
                f_[i+1,j-1] = f_[i+1,j-1] + 3*erro/16.
            if i < f_.shape[0]-1:
                f_[i+1,j] = f_[i+1,j] + 5*erro/16.
            if i < f_.shape[0]-1 and j < f_.shape[1]-1:
                f_[i+1,j+1] = f_[i+1,j+1] + erro/16.
    g = g > 0
    return g


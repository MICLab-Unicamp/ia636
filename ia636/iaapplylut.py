# -*- encoding: utf-8 -*-
# Module iaapplylut

from numpy import *

def iaapplylut(fi, it):
    g = it[fi]
    if len(g.shape) == 3:
        aux = zeros((3,g.shape[0],g.shape[1]), fi.dtype.name)
        for i in range(3):
            aux[i,:,:] = g[:,:,i]
        g = aux
    return g


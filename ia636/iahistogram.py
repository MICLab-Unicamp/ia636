# -*- encoding: utf-8 -*-
# Module iahistogram

import numpy as np

def iahistogram(f):

    return np.bincount(f.ravel())
def iahistogram_eq(f):

    from numpy import amax, zeros, arange, sum

    n = amax(f) + 1
    h = zeros((n,),int)
    for i in arange(n):
      h[i] = sum(i == f)
    return h
def iahistogram_eq1(f):

    import numpy as np
    n = f.size
    m = f.max() + 1
    haux = np.zeros((m,n),int)
    fi = f.ravel()
    i = xrange(n)
    haux[fi,i] = 1
    h = haux.sum(axis=1)
    return h


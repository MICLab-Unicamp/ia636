# -*- encoding: utf-8 -*-
# Module iahwt

from numpy import *

def iahwt(f):
    from iahaarmatrix import iahaarmatrix

    f = asarray(f).astype(float64)
    if len(f.shape) == 1: f = f[:,newaxis]
    (m, n) = f.shape
    A = iahaarmatrix(m)
    if (n == 1):
        F = dot(A, f)
    else:
        B = iahaarmatrix(n)
        F = dot(dot(A, f), transpose(B))
    return F


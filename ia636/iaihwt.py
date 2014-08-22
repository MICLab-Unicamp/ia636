# -*- encoding: utf-8 -*-
# Module iaihwt

from numpy import *

def iaihwt(f):
    from iahaarmatrix import iahaarmatrix

    f = asarray(f).astype(float64)
    if len(f.shape) == 1: f = f[:,newaxis]
    (m, n) = f.shape
    A = iahaarmatrix(m)
    if (n == 1):
        F = dot(transpose(A), f)
    else:
        B = iahaarmatrix(n)
        F = dot(dot(transpose(A), f), B)
    return F


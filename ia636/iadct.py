# -*- encoding: utf-8 -*-
# Module iadct

from numpy import *

def iadct(f):
    from iadctmatrix import iadctmatrix
    f = asarray(f).astype(float64)
    if len(f.shape) == 1: f = f[:,newaxis]
    (m, n) = f.shape
    if (n == 1):
        A = iadctmatrix(m)
        F = dot(A, f)
    else:
        A=iadctmatrix(m)
        B=iadctmatrix(n)
        F = dot(dot(A, f), transpose(B))
    return F


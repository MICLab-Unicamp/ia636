# -*- encoding: utf-8 -*-
# Module iaidct

from numpy import *

def iaidct(f):
    from iadctmatrix import iadctmatrix

    f = asarray(f).astype(float64)
    if len(f.shape) == 1: f = f[:,newaxis]
    (m, n) = f.shape
    if (n == 1):
        A = iadctmatrix(m)
        F = dot(transpose(A), f)
    else:
        A=iadctmatrix(m)
        B=iadctmatrix(n)
        F = dot(dot(transpose(A), f), B)
    return F


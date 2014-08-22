# -*- encoding: utf-8 -*-
# Module iaihadamard

from numpy import *

def iaihadamard(f):
    from iahadamardmatrix import iahadamardmatrix

    f = asarray(f).astype(float64)
    if len(f.shape) == 1: f = f[:,newaxis]
    (m, n) = f.shape
    A = iahadamardmatrix(m)
    if (n == 1):
        F = dot(transpose(A), f)
    else:
        B = iahadamardmatrix(n)
        F = dot(dot(transpose(A), f), B)
    return F


# -*- encoding: utf-8 -*-
# Module iahadamard

from numpy import *

def iahadamard(f):
    from iahadamardmatrix import iahadamardmatrix

    f = asarray(f).astype(float64)
    if len(f.shape) == 1: f = f[:,newaxis]
    (m, n) = f.shape
    A = iahadamardmatrix(m)
    if (n == 1):
        F = dot(A, f)
    else:
        B = iahadamardmatrix(n)
        F = dot(dot(A, f), transpose(B))
    return F


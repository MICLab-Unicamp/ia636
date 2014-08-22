# -*- encoding: utf-8 -*-
# Module iadft

from numpy import *

def iadft(f):
    from ia636 import iadftmatrix
    f = asarray(f).astype(float64)
    if (len(f.shape) == 1):
        m = len(f)
        A = iadftmatrix(f.shape[0])
        F = sqrt(m) * dot(A, f)
    elif (len(f.shape) == 2):
        (m, n) = f.shape
        A = iadftmatrix(m)
        B = iadftmatrix(n)
        F = sqrt(m * n) * dot(dot(A, f), B)
    else:
        (p,m,n) = f.shape
        A = iadftmatrix(m)
        B = iadftmatrix(n)
        C = iadftmatrix(p)
        Faux = dot(A,f)
        Faux = dot(Faux,B)
        F = sqrt(p)*sqrt(m)*sqrt(n)*dot(C,Faux)
    return F


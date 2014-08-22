# -*- encoding: utf-8 -*-
# Module iaidft

from numpy import *

def iaidft(F):
    from ia636 import iadftmatrix

    s = F.shape
    if len(F.shape) == 1: F = F[newaxis,newaxis,:]
    if len(F.shape) == 2: F = F[newaxis,:,:]

    (p,m,n) = F.shape
    A = iadftmatrix(m)
    B = iadftmatrix(n)
    C = iadftmatrix(p)
    Faux = dot(conjugate(A),F)
    Faux = dot(Faux,conjugate(B))
    f = dot(conjugate(C),Faux)/(sqrt(p)*sqrt(m)*sqrt(n))

    return f.reshape(s)


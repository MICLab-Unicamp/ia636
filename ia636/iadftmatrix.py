# -*- encoding: utf-8 -*-
# Module iadftmatrix

from numpy import *

def iadftmatrix(N):
    x = arange(N).reshape(N,1)
    u = x
    Wn = exp(-1j*2*pi/N)
    A = (1./sqrt(N)) * (Wn ** dot(u, x.T))
    return A


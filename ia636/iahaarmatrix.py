# -*- encoding: utf-8 -*-
# Module iahaarmatrix

from numpy import *

def iahaarmatrix(N):
    from iameshgrid import iameshgrid

    n = floor(log(N)/log(2))

    if 2**n != N:
       raise Exception, 'error: size '+str(N)+' is not multiple of power of 2'

    z, k = iameshgrid(1.*arange(N)/N, 1.*arange(N))
    p  = floor(log(maximum(1,k))/log(2))
    q  = k - (2**p) + 1
    z1 = (q-1)   / (2**p)
    z2 = (q-0.5) / (2**p)
    z3 = q       / (2**p)
    A  = (1/sqrt(N)) * ((( 2**(p/2.)) * ((z >= z1) & (z < z2))) \
                              + ((-2**(p/2.)) * ((z >= z2) & (z < z3))))
    A[0,:] = 1/sqrt(N)
    return A


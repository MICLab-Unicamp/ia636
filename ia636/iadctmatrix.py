# -*- encoding: utf-8 -*-
# Module iadctmatrix

from numpy import *

def iadctmatrix(N):
    from iameshgrid import iameshgrid
    x, u = iameshgrid(range(N), range(N)) # (u,x)
    alpha = ones((N,N)) * sqrt(2./N)
    alpha[0,:] = sqrt(1./N) # alpha(u,x)
    A = alpha * cos((2*x+1)*u*pi / (2.*N)) # Cn(u,x)
    return A


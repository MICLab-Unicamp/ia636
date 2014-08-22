# -*- encoding: utf-8 -*-
# Module iaisdftsym

from numpy import *

def iaisdftsym(F):

    if len(F.shape) == 1: F = F[newaxis,newaxis,:]
    if len(F.shape) == 2: F = F[newaxis,:,:]

    n,m,p = F.shape
    x,y,z = indices((n,m,p))

    Xnovo = mod(-1*x,n)
    Ynovo = mod(-1*y,m)
    Znovo = mod(-1*z,p)

    aux = conjugate(F[Xnovo,Ynovo,Znovo])

    return alltrue(abs(F-aux)<10E-4)


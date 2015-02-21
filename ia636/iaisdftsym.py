# -*- encoding: utf-8 -*-
# Module iaisdftsym

import numpy as np

def iaisdftsym(F):

    if len(F.shape) == 1: F = F[np.newaxis,np.newaxis,:]
    if len(F.shape) == 2: F = F[np.newaxis,:,:]

    n,m,p = F.shape
    x,y,z = np.indices((n,m,p))

    Xnovo = np.mod(-1*x,n)
    Ynovo = np.mod(-1*y,m)
    Znovo = np.mod(-1*z,p)

    aux = np.conjugate(F[Xnovo,Ynovo,Znovo])

    return (abs(F-aux)<10E-4).all()


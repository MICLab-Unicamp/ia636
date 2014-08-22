# -*- encoding: utf-8 -*-
# Module iamosaic

from numpy import *
import scipy

def iamosaic(f,N,s=1.0):
    f = asarray(f)
    d,h,w = f.shape

    nLines = ceil(float(d)/N)
    nCells = nLines*N

    # Add black slices to match the exact number of mosaic cells
    fullf = resize(f, (nCells,h,w))
    fullf[d:nCells,:,:] = 0

    Y,X = indices((nLines*h,N*w))

    Pts = array([
            (floor(Y/h)*N + floor(X/w)).ravel(),
            mod(Y,h).ravel(),
            mod(X,w).ravel() ]).astype(int).reshape((3,nLines*h,N*w))

    g = scipy.ndimage.interpolation.zoom(fullf[Pts[0],Pts[1],Pts[2]],s,order=5)

    return g


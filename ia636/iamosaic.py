# -*- encoding: utf-8 -*-
# Module iamosaic

import numpy as np
import scipy
import scipy.ndimage

def iamosaic(f,N,s=1.0):
    f = np.asarray(f)
    d,h,w = f.shape

    nLines = np.ceil(float(d)/N)
    nCells = nLines*N

    # Add black slices to match the exact number of mosaic cells
    fullf = np.resize(f, (nCells,h,w))
    fullf[d:nCells,:,:] = 0

    Y,X = np.indices((nLines*h,N*w))

    Pts = np.array([
            (np.floor(Y/h)*N + np.floor(X/w)).ravel(),
            np.mod(Y,h).ravel(),
            np.mod(X,w).ravel() ]).astype(int).reshape((3,nLines*h,N*w))
    g = fullf[Pts[0],Pts[1],Pts[2]]
    if (s != 1.0):
        g = scipy.ndimage.interpolation.zoom(g,s,order=5)
        #g = scipy.misc.imresize(g,s,interp='bilinear')
    return g


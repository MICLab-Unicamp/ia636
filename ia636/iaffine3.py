# -*- encoding: utf-8 -*-
# Module iaffine3

def iaffine3(f, T, interpol='CLOSEST', destshape='SAME', destorg=(0,)):
    import numpy as np
    from ia636 import iainterpollin
    from ia636 import iainterpolclosest
    if T.ndim != 2 or T.shape[0] != T.shape[1]:
        raise ValueError, 'T must be a square matrix'

    dim = T.shape[0] - 1
    if dim != 2 and dim != 3:
        raise ValueError, 'T must be either 3x3 or 4x4 (2D or 3D transform)'

    if f.ndim < dim:
        raise ValueError, 'dimention of f is not compatible with the transform matrix'

    # if dimension of f is higher than dim then several planes need to be transformed.
    cor = (f.ndim > dim)

    # split the shape of f in two parts. sht is the part where the tranform is applied,
    # shh is not subject to the affine transform
    sht = f.shape[f.ndim - dim:]
    shh = f.shape[:f.ndim - dim]


    invT = np.linalg.inv(T.astype(np.float))
    # get the limits of the destination image
    shmin = np.asarray(destorg).astype(int)

    # f shape as a column
    fshapecol = np.asarray(sht)
    fshapecol.shape = (dim, 1)
    if destshape == 'SAME':
        shmax = np.asarray(sht)
        shmin = np.zeros((1), int)
    elif destshape == 'FIT':
        if dim == 2:
            M = np.asarray([[0,0,1,1],[0,1,0,1]]).astype(float)
        else:
            M =np.asarray([[0,0,0,0,1,1,1,1],[0,0,1,1,0,0,1,1],[0,1,0,1,0,1,0,1]]).astype(float)
        M *= (np.asarray(fshapecol)-1)
        M = np.vstack((M, np.ones((1,M.shape[1]))))
        M = np.dot(T, M)
        shmax = np.ceil(np.max(M, 1)[:-1]).astype(int)
        shmin = np.floor(np.min(M, 1)[:-1]).astype(int)
    else:
        shmin = np.asarray(destorg).astype(int)
        shmax = np.asarray(destshape).astype(int) + shmin
    # shmin in column shape
    shimincol = np.reshape(shmin, (shmin.shape[0], 1))

    # get indices in target space
    ind = np.indices(shmax-shmin)
    ind.shape = (ind.shape[0], np.prod(ind.shape[1:]))
    ind += shimincol

    # shape of target image
    dstshape = tuple(shmax - shmin)

    #apply inverse transform on the target coordinates
    tind = np.vstack((ind, np.ones((1, np.size(ind[0]))))).astype(float)
    oind = np.dot(invT, tind)

    # remove out of bounds indices
    oindr = oind.copy()
    oindr[:-1, :] = np.maximum(oind[:-1,:], 0)
    oindr[:-1, :] = np.minimum(oindr[:-1,:], fshapecol-1)

    # Select interpolation function
    if interpol=='LINEAR':
        interpolfunc = iainterpollin
    elif interpol=='CLOSEST':
        interpolfunc = iainterpolclosest
    else:
        # the user is providing his own interpolation function
        interpolfunc=interpol


    # interpolate data
    if cor:
        count = np.prod(shh)
        fr = np.reshape(f, ((count,) + sht))
        interpshape = ((count,) + (np.prod(dstshape),))
        g = np.empty(interpshape)
        for i in range(count):
            g[i] = interpolfunc(fr[i], oindr[0:-1,:])
            # set to 0 points out of bounds
            g[i, np.not_equal(np.sum(np.not_equal(oindr, oind), 0), 0)] = 0
        g.shape = (shh + dstshape)

    else:
        g = interpolfunc(f, oindr[0:-1,:])
        # set to 0 points out of bounds
        g[np.not_equal(np.sum(np.not_equal(oindr, oind), 0), 0)] = 0
        g.shape = dstshape
    return g


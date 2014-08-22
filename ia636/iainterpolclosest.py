# -*- encoding: utf-8 -*-
# Module iainterpolclosest

def iainterpolclosest(f, pts):
    # f - one, two or three dimention array
    # pts - array of points to interpolate
    import numpy as np
    ptsi = np.rint(pts).astype(int)
    ptsi[ptsi<0] = 0

    # make sure ptsi dimention is >= 2
    if ptsi.ndim==1:
        ptsi.shape = (1, ptsi.size)
    for i in range(0, f.ndim):
        ptsi[i] = np.minimum(ptsi[i], f.shape[i]-1)
    return f[list(ptsi)]


# -*- encoding: utf-8 -*-
# Module iavarfilter

from numpy import *

def iavarfilter(f,h,CV=True):

    from ia636 import iapconv

    f = asarray(f).astype(float64)
    h = asarray(h).astype(bool)[::-1,::-1]

    n = sum(ravel(h))
    h = h/float(n)
    fm = iapconv(f, h)
    f2m = iapconv(f**2, h)

    g = f2m - fm**2

    if (CV):
        fm = fm + 1e-320*(fm == 0) # change zero by a very small number (prevent 'math range error')
        g[g<0.0] = 0.0 # avoid negative numbers due to numeric precision
        g = sqrt(g) / fm

    return g


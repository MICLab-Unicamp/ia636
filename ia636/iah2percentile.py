# -*- encoding: utf-8 -*-
# Module iah2percentile

def iah2percentile(h,p):

    import numpy as np
    s = h.sum()
    k = ((s-1) * p/100.)+1
    dw = np.floor(k)
    up = np.ceil(k)
    hc = np.cumsum(h)
    if isinstance(p, int):
       k1 = np.argmax(hc>=dw)
       k2 = np.argmax(hc>=up)
    else:
       k1 = np.argmax(hc>=dw[:,np.newaxis],axis=1)
       k2 = np.argmax(hc>=up[:,np.newaxis],axis=1)
    d0 = k1 * (up-k)
    d1 = k2 * (k -dw)
    return np.where(dw==up,k1,d0+d1)


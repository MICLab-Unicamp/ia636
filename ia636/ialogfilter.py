# -*- encoding: utf-8 -*-
# Module ialogfilter

from numpy.fft import fft2, ifft2
from numpy import *

def ialogfilter(f, sigma):
    from ialog import ialog
    from iaifftshift import iaifftshift
    from iaisdftsym import iaisdftsym

    if len(shape(f)) == 1: f = f[newaxis,:]
    h = ialog(shape(f), map(int, array(shape(f))/2.), sigma)
    h = iaifftshift(h)
    H = fft2(h)
    if not iaisdftsym(H):
       raise Exception, "error: log filter is not symmetrical"
    G = fft2(f) * H
    g = ifft2(G).real
    return g


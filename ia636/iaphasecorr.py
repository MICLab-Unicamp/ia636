# -*- encoding: utf-8 -*-
# Module iaphasecorr

from numpy import *

def iaphasecorr(f,h):
    F = fft.fftn(f)
    H = fft.fftn(h)
    T = F*conjugate(H)
    R = T/abs(T)
    g = fft.ifftn(R)
    return g.real


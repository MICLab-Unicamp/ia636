# -*- encoding: utf-8 -*-
# Module ianeg

from numpy import *

def ianeg(f):

    f = asarray(f)
    if f.dtype in ['b','uint8','???']: # (numarray implementara uint16 e boolean)
        k = 2**(8*f.itemsize) - 1
        g = k - f
    else: # Trata os tipos com sinal
        g = -f.astype(float)
    return g


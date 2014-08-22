# -*- encoding: utf-8 -*-
# Module iapad

from numpy import *

def iapad(f, thick=[1,1], value=0):

    f, thick = asarray(f), asarray(thick)
    g = (value * ones(array(f.shape)+2*thick)).astype(f.dtype.char)
    g[thick[0]:-thick[0], thick[1]:-thick[1]] = f
    return g


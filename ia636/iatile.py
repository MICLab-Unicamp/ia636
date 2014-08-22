# -*- encoding: utf-8 -*-
# Module iatile

from numpy import *

def iatile(f, new_size):

    f = asarray(f)
    if len(f.shape) == 1: f = f[newaxis,:]

    aux = resize(f, (new_size[0], f.shape[1]))
    aux = transpose(aux)
    aux = resize(aux, (new_size[1], new_size[0]))
    g = transpose(aux)
    return g


# -*- encoding: utf-8 -*-
# Module iacomb

from numpy import *

def iacomb(s, delta, offset):

    s = asarray(s)
    if product(s.shape) == 1:
        g = zeros(s)
        g[offset::delta] = 1
    elif s.size >= 2:
        g = zeros((s[0], s[1]))
        g[offset[0]::delta[0], offset[1]::delta[1]] = 1

    if s.size == 3:
        aux = zeros(s)
        for i in range(offset[2], s[2], delta[2]):
            aux[:,:,i] = g
        g = aux
    return g


# -*- encoding: utf-8 -*-
# Module iacrop

from numpy import *

def iacrop(f, side='all', color='black'):
    from ianeg import ianeg


    f = asarray(f)
    if len(f.shape) == 1: f = f[newaxis,:]
    if color == 'white': f = ianeg(f)

    aux1, aux2 = sometrue(f,0), sometrue(f,1)
    col, row = flatnonzero(aux1), flatnonzero(aux2)

    #if (not col) and (not row):
    #    return None

    if   side == 'left':   g = f[:, col[0]::]
    elif side == 'right':  g = f[:, 0:col[-1]+1]
    elif side == 'top':    g = f[row[0]::, :]
    elif side == 'bottom': g = f[0:row[-1]+1, :]
    else:                  g = f[row[0]:row[-1]+1, col[0]:col[-1]+1]

    if color == 'white': g = ianeg(g)
    return g


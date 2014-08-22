# -*- encoding: utf-8 -*-
# Module iaroi

from numpy import *

def iaroi(f, p1, p2):

    f = asarray(f)
    if len(f.shape) == 1: f = f[newaxis,:]

    g = f[p1[0]:p2[0]+1, p1[1]:p2[1]+1]
    return g


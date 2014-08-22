# -*- encoding: utf-8 -*-
# Module iargb2gray

from numpy import *

def iargb2gray(f):

    g =  f[0,:,:]*0.299 + f[1,:,:]*0.587 + f[2,:,:]*0.114
    return g.astype(f.dtype)


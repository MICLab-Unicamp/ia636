# -*- encoding: utf-8 -*-
# Module iasub2ind

from numpy import *

def iasub2ind(dim, x, y):

    x, y = asarray(x), asarray(y)
    i = x*dim[1] + y
    i = i.astype(int32)
    return i


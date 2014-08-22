# -*- encoding: utf-8 -*-
# Module iaind2sub

from numpy import *

def iaind2sub(dim, i):

    x = i / dim[1]
    y = i % dim[1]
    return x, y


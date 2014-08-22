# -*- encoding: utf-8 -*-
# Module iaifftshift

from numpy import *

def iaifftshift(H):
    from iaptrans import iaptrans

    HS = iaptrans(H, ceil(-array(shape(H))/2).astype(int))
    return HS


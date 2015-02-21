# -*- encoding: utf-8 -*-
# Module iadftview

from numpy import *

def iadftview(F):
    from ia636 import iafftshift
    from ia636 import ianormalize

    FM = iafftshift(log(abs(F)+1))
    return ianormalize(FM).astype(uint8)


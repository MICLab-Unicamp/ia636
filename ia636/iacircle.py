# -*- encoding: utf-8 -*-
# Module iacircle

from numpy import *

def iacircle(s, r, c):

    rows, cols = s[0], s[1]
    rr0,  cc0  = c[0], c[1]
    rr, cc = meshgrid(range(rows), range(cols), indexing='ij')
    g = (rr - rr0)**2 + (cc - cc0)**2 <= r**2
    return g


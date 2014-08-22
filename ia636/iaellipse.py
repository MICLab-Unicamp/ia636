# -*- encoding: utf-8 -*-
# Module iaellipse

from numpy import *
import math

def iaellipse(s, r, c, theta = 0):
    rows, cols = s[0], s[1]
    rr0,  cc0  = c[0], c[1]
    rr, cc = meshgrid(range(rows), range(cols), indexing='ij')
    rr = rr - rr0
    cc = cc - cc0
    cos = math.cos(theta)
    sen = math.sin(theta)
    i = cos/r[1]
    j = sen/r[0]
    m = -sen/r[1]
    n = cos/r[0]
    g = ((i*cc + m*rr)**2 + (j*cc + n*rr)**2) <= 1
    return g


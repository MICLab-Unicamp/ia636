# -*- encoding: utf-8 -*-
# Module iarectangle

from numpy import *

def iarectangle(s, r, c):

    rows,  cols  = s[0], s[1]
    rrows, rcols = r[0], r[1]
    rr0,   cc0   = c[0], c[1]
    rr, cc = meshgrid(range(rows), range(cols), indexing='ij')

    min_row, max_row = rr0-rrows/2.0, rr0+rrows/2.0
    min_col, max_col = cc0-rcols/2.0, cc0+rcols/2.0

    g1 = (min_row <= rr) & (max_row > rr)
    g2 = (min_col <= cc) & (max_col > cc)

    g = g1 & g2
    return g


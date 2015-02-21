# -*- encoding: utf-8 -*-
# Module iaapplylut

import numpy as np

def iaapplylut(fi, it):
    g = it[fi]
    if len(g.shape) == 3:
        g = np.swapaxes(g, 0,2)
        g = np.swapaxes(g, 1,2)
    return g


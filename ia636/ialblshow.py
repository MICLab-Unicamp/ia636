# -*- encoding: utf-8 -*-
# Module ialblshow

import numpy as np
from numpy.random import rand

def ialblshow(f):
    from iaapplylut import iaapplylut

    nblobs = f.max()
    r = np.floor(0.5 + 255*rand(nblobs, 1))
    g = np.floor(0.5 + 255*rand(nblobs, 1))
    b = np.floor(0.5 + 255*rand(nblobs, 1))
    ct = np.concatenate((r,g,b), 1)
    ct = np.concatenate(([[0,0,0]], ct))

    g = iaapplylut(f, ct)
    return g


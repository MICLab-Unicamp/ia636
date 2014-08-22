# -*- encoding: utf-8 -*-
# Module iaisolines

import numpy as np
import ia636 as ia

def iaisolines(f, nc=10, n=1):
    maxi = np.ceil(f.max())
    mini = np.floor(f.min())
    d = int(np.ceil(1.*(maxi-mini)/nc))
    m = np.zeros((d,1))
    m[0:n,:] = 1
    m = np.resize(m, (maxi-mini, 1))
    m = np.concatenate((np.zeros((mini,1)), m))
    m = np.concatenate((m, np.zeros((256-maxi,1))))
    m = np.concatenate((m,m,m), 1)
    ct = m*ia.iacolormap('hsv') + (1-m)*ia.iacolormap('gray')
    g = ia.iaapplylut(f, ct)
    return g


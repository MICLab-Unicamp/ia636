# -*- encoding: utf-8 -*-
# Module iaptrans

from numpy import *

def iaptrans(f,t):
    import numpy as np
    g = np.empty(f.shape)
    if f.ndim == 1:
      W = f.shape[0]
      col = arange(W)
      g[:] = f[(col-t)%W]
    elif f.ndim == 2:
      H,W = f.shape
      rr,cc = t
      row,col = np.indices(f.shape)
      g[:] = f[(row-rr)%H, (col-cc)%W]
    elif f.ndim == 3:
      Z,H,W = f.shape
      zz,rr,cc = t
      z,row,col = np.indices(f.shape)
      g[:] = f[(z-zz)%Z, (row-rr)%H, (col-cc)%W]
    return g

# implementation using periodic convolution
def iaptrans2(f, t):
    from ia636 import iapconv

    f, t = asarray(f), asarray(t).astype(int32)
    h = zeros(2*abs(t) + 1)
    t = t + abs(t)
    h[tuple(t)] = 1
    g = iapconv(f, h)
    return g


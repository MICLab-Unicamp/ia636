# -*- encoding: utf-8 -*-
# Module iapercentile

def iapercentile(f, p=1):

   import numpy as np
   k = (f.size-1) * p/100.
   dw = np.floor(k).astype(int)
   up = np.ceil(k).astype(int)
   g  = np.sort(f.ravel())
   d  = g[dw]
   d0 =   d   * (up-k)
   d1 = g[up] * (k -dw)
   return np.where(dw==up, d, d0+d1)


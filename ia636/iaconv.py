# -*- encoding: utf-8 -*-
# Module iaconv

import numpy as np

def iaconv(f, h):
    f, h = np.asarray(f), np.asarray(h,float)
    if len(f.shape) == 1: f = f[np.newaxis,:]
    if len(h.shape) == 1: h = h[np.newaxis,:]
    if f.size < h.size:
        f, h = h, f
    g = np.zeros(np.array(f.shape) + np.array(h.shape) - 1)
    if f.ndim == 2:
        for i in xrange(h.shape[0]):
            for j in xrange(h.shape[1]):
                if h[i,j]:
                  g[i:i+f.shape[0], j:j+f.shape[1]] += h[i,j] * f

    if f.ndim == 3:
        for i in xrange(h.shape[0]):
            for j in xrange(h.shape[1]):
                for k in xrange(h.shape[2]):
                    if h[i,j,k]:
                      g[i:i+f.shape[0], j:j+f.shape[1], k:k+f.shape[2]] += h[i,j,k] * f

    return g


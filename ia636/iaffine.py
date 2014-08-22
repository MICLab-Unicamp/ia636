# -*- encoding: utf-8 -*-
# Module iaffine

import numpy as np

def iaffine(f,T,domain=0):

    if np.sum(domain) == 0:
        domain = f.shape
    if len(f.shape) == 2:
        H,W = f.shape
        y1,x1 = np.indices((domain))

        yx1 = np.array([ y1.ravel(),
                         x1.ravel(),
                         np.ones(np.product(domain))])
        yx_float = np.dot(np.linalg.inv(T), yx1)
        yy = np.rint(yx_float[0]).astype(int)
        xx = np.rint(yx_float[1]).astype(int)

        y = np.clip(yy,0,H-1).reshape(domain)
        x = np.clip(xx,0,W-1).reshape(domain)

        g = f[y,x]

    if len(f.shape) == 3:
        D,H,W = f.shape
        z1,y1,x1 = np.indices((domain))
        zyx1 = np.array([ z1.ravel(),
                          y1.ravel(),
                          x1.ravel(),
                          np.ones(np.product(domain)) ])
        zyx_float = np.dot(np.linalg.inv(T), zyx1)

        zz = np.rint(zyx_float[0]).astype(int)
        yy = np.rint(zyx_float[1]).astype(int)
        xx = np.rint(zyx_float[2]).astype(int)

        z = np.clip(zz, 0, D-1).reshape(domain) #z
        y = np.clip(yy, 0, H-1).reshape(domain) #rows
        x = np.clip(xx, 0, W-1).reshape(domain) #columns

        g = f[z,y,x]

    return g


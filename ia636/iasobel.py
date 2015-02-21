# -*- encoding: utf-8 -*-
# Module iasobel

def iasobel(f):
    import numpy as np
    from ia636 import iaimginfo, iapconv

    wx = np.array([[1.,2.,1.],
                   [0.,0.,0.],
                   [-1.,-2.,-1.]])
    wy = np.array([[1.,0.,-1.],
                   [2.,0.,-2.],
                   [1.,0.,-1.]])
    gx = iapconv(f, wx)
    gy = iapconv(f, wy)
    mag = np.abs(gx + gy*1j)
    theta = np.arctan2(gy,gx)
    return mag,theta


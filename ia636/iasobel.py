# -*- encoding: utf-8 -*-
# Module iasobel

from numpy import *
import numpy.oldnumeric.mlab as Mlab
from numpy.oldnumeric.mlab import *

def iasobel(f):
    from iapconv import iapconv
    from ia636 import iaimginfo

    def test_arctan2(x,y):
        from numpy import arctan2
        try:
            return (arctan2(x,y))
        except:
            return 0

    wx = array([[1.,2.,1.],
                [0.,0.,0.],
                [-1.,-2.,-1.]])
    wy = array([[1.,0.,-1.],
                [2.,0.,-2.],
                [1.,0.,-1.]])
    gx = iapconv(f, wx)
    gy = iapconv(f, wy)
    mag = abs(gx + gy*1j)
    theta = reshape(map(test_arctan2, ravel(gy), ravel(gx)), f.shape)
    return mag,theta


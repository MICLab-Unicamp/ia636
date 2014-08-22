# -*- encoding: utf-8 -*-
# Module iahadamardmatrix

from numpy import *

def iahadamardmatrix(N):
    from iameshgrid import iameshgrid

    def bitsum(x):
        s = 0 * x
        while x.any():
            s += x & 1
            x >>= 1
        return s

    n = floor(log(N)/log(2))

    if 2**n != N:
       raise Exception, 'error: size '+str(N)+' is not multiple of power of 2'

    u, x = iameshgrid(range(N), range(N))

    A = ((-1)**(bitsum(x & u)))/sqrt(N)
    return A


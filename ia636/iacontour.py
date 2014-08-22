# -*- encoding: utf-8 -*-
# Module iacontour

from numpy import *

def iacontour(f):

    f_ = f > 0
    new_shape = array(f_.shape)+2
    n = zeros(new_shape); n[0:-2,1:-1] = f_
    s = zeros(new_shape); s[2:: ,1:-1] = f_
    w = zeros(new_shape); w[1:-1,0:-2] = f_
    e = zeros(new_shape); e[1:-1,2:: ] = f_
    fi = logical_and(logical_and(logical_and(n,s),w),e)
    fi = fi[1:-1,1:-1]
    g = f_ - fi
    g = g > 0
    return g


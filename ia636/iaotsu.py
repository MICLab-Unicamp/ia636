# -*- encoding: utf-8 -*-
# Module iaotsu

from numpy import *

def iaotsu(f):
    n = product(shape(f))
    h = 1.*bincount(f.ravel()) / n  # used bincount instead of iahistogram
    if len(h) == 1: return 1,1
    x = arange(product(shape(h)))
    w0 = cumsum(h)
    w1 = 1 - w0
    eps = 1e-10
    m0 = cumsum(x * h) / (w0 + eps)
    mt = m0[-1]
    m1 = (mt - m0[0:-1]*w0[0:-1]) / w1[0:-1]
    sB2 = w0[0:-1] * w1[0:-1] * ((m0[0:-1] - m1)**2)
    t = argmax(sB2)
    v = sB2[t]
    st2 = sum((x-mt)**2 * h)
    eta = v / st2
    return t, eta


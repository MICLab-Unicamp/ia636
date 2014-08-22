# -*- encoding: utf-8 -*-
# Module iapolar

from numpy import *

def iapolar(f, domain, thetamax = 2 * pi):

    from ia636 import iainterpollin
    f = array(f)
    m,n = f.shape
    dm,dn = domain
    Ry,Rx = floor(array(f.shape)/2)

    b = min(Ry,Rx)/dm
    a = thetamax/dn

    y,x = indices(domain)

    XI = Rx + (b*y)*cos(a*x)
    YI = Ry + (b*y)*sin(a*x)

    g = iainterpollin(f, array([YI.ravel(), XI.ravel()]))
    g.shape = domain

    return g


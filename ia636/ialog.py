# -*- encoding: utf-8 -*-
# Module ialog

from numpy import *

def ialog(s, mu, sigma):

    def test_exp(x,sigma):
       try:
          return (exp(-(x / (2. * sigma**2))))
       except:
          return 0

    mu = array(mu)
    if product(shape(s)) == 1:
       x = arange(s)
       r2 = (x-mu)**2
    else:
       (rr, cc) = indices( s)
       r2 = (rr-mu[0])**2  + (cc-mu[1])**2

    r2_aux = ravel(r2)
    aux = reshape(map(test_exp, r2_aux, 0*r2_aux+sigma), r2.shape)
    g = -(((r2 - 2 * sigma**2) / (sigma**4 * pi)) * aux)
    return g


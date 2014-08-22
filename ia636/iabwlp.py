# -*- encoding: utf-8 -*-
# Module iabwlp

from numpy import *
import string

def iabwlp(fsize, tc, n, option='circle'):
    from iafftshift import iafftshift

    def test_exp(x, y):
        try:
            return x**(2*y)
        except:
            return 1E300 # Infinito!

    rows, cols = fsize[0], fsize[1]
    mh, mw = rows/2, cols/2
    rr, cc = meshgrid(arange(-mh,rows-mh), arange(-mw,cols-mw), indexing='ij') # center
    if string.find(string.upper(option), 'SQUARE') != -1:
        H = 1./(1.+(sqrt(2)-1)*(maximum(abs(1.*rr/rows) , abs(1.*cc/cols))*tc)**(2*n))
    else:
        aux1 = ravel(sqrt(((1.*rr)/rows)**2 + ((1.*cc)/cols)**2)*tc)
        aux2 = 0.*aux1 + n
        aux = reshape(map(test_exp, aux1, aux2), cc.shape)
        H = 1./(1+(sqrt(2)-1)*aux)
    H = iafftshift(H)
    return H


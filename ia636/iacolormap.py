# -*- encoding: utf-8 -*-
# Module iacolormap

from numpy import *
import colorsys

def iacolormap(type='gray'):
    from ianormalize import ianormalize
    from iacolormap import iacolormap

    if type == 'gray':
        ct = transpose(resize(arange(256), (3,256)))
    elif type == 'hsv':
        h = arange(256)/255.
        s = ones(256)
        v = ones(256)
        ct = ianormalize(reshape(map(colorsys.hsv_to_rgb, h, s, v), (256,3)), [0,255]).astype(uint8)
    elif type == 'hot':
        n = int(3./8*256)
        r = concatenate((arange(1,n+1)/n, ones(256-n)), 1)[:,newaxis]
        g = concatenate((zeros(n), arange(1,n+1)/n, ones(256-2*n)), 1)[:,newaxis]
        b = concatenate((zeros(2*n), arange(1,256-2*n+1)/(256-2*n)), 1)[:,newaxis]
        ct = ianormalize(concatenate((r,g,b), 1), [0,255]).astype(uint8)
    elif type == 'cool':
        r = (arange(256)/255.)[:,newaxis]
        ct = ianormalize(concatenate((r, 1-r, ones((256,1))), 1), [0,255]).astype(uint8)
    elif type == 'bone':
        ct = ianormalize((7*iacolormap('gray') + iacolormap('hot')[:,::-1]) / 8., [0,255]).astype(uint8)
    elif type == 'copper':
        ct = ianormalize(min(1, dot(iacolormap('gray')/255., [[1.25,0,0],[0,0.7812,0],[0,0,0.4975]])), [0,255]).astype(uint8)
    elif type == 'pink':
        ct = ianormalize(sqrt((2*iacolormap('gray') + iacolormap('hot')) / 3), [0,255]).astype(uint8)
    else:
        ct = zeros((256,3))
    return ct


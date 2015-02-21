# -*- encoding: utf-8 -*-
# Module iacolormap

import numpy as np
import colorsys
import ia636 as ia

def iacolormap(type='gray'):

    if type == 'gray':
        ct = np.transpose(np.resize(np.arange(256), (3,256)))
    elif type == 'hsv':
        h = np.arange(256)/255.
        s = np.ones(256)
        v = np.ones(256)
        ct = ia.ianormalize(np.reshape(map(colorsys.hsv_to_rgb, h, s, v), (256,3)), [0,255]).astype(np.uint8)
    elif type == 'hot':
        n = np.floor(256./3) #np.floor(3./8*256)
        r = np.concatenate((np.arange(1,n+1)/n, np.ones(256-n)), 1)[:,np.newaxis]
        g = np.concatenate((np.zeros(n), np.arange(1,n+1)/n, np.ones(256-2*n)), 1)[:,np.newaxis]
        b = np.concatenate((np.zeros(2*n), np.arange(1,256-2*n+1)/(256-2*n)), 1)[:,np.newaxis]
        ct = ia.ianormalize(np.concatenate((r,g,b), 1), [0,255]).astype(np.uint8)
    elif type == 'cool':
        r = (np.arange(256)/255.)[:,np.newaxis]
        ct = ia.ianormalize(np.concatenate((r, 1-r, np.ones((256,1))), 1), [0,255]).astype(np.uint8)
    elif type == 'bone':
        ct = ia.ianormalize((7 * iacolormap('gray') + iacolormap('hot')[:,::-1]) / 8., [0,255]).astype(np.uint8)
    elif type == 'copper':
        cg = iacolormap('gray')/255.
        fac = np.dot(cg, [[1.25,0,0],[0,0.7812,0],[0,0,0.4975]])
        aux = np.minimum(1, fac)
        ct = ia.ianormalize(aux).astype(np.uint8)
    elif type == 'pink':
        ct = ia.ianormalize(np.sqrt((2*iacolormap('gray') + iacolormap('hot')) / 3), [0,255]).astype(np.uint8)
    else:
        ct = np.zeros((256,3))
    return ct


# -*- encoding: utf-8 -*-
# Module iatcrgb2ind

import numpy as np

def iatcrgb2ind(f):

    f = np.asarray(f)
    r, g, b = f[0].astype(np.int), f[1].astype(np.int), f[2].astype(np.int)
    c = r + 256*g + 256*256*b

    (t,i) = np.unique(c,return_inverse=True)

    n = len(t)
    rt = np.reshape(map(lambda k:int(k%256), t), (n,1))
    gt = np.reshape(map(lambda k:int((k%(256*256))/256.), t), (n,1))
    bt = np.reshape(map(lambda k:int(k), t/(256*256.)), (n,1))

    cm = np.concatenate((rt, gt, bt), axis=1)
    fi = i.reshape(r.shape)
    return fi,cm


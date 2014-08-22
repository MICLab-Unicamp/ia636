# -*- encoding: utf-8 -*-
# Module iapconv

def iapconv4(f,h):
   import numpy as np

   h_ind=np.nonzero(h)
   f_ind=np.nonzero(f)
   if len(h_ind[0])>len(f_ind[0]):
       h,    f    = f,    h
       h_ind,f_ind= f_ind,h_ind

   gs = np.maximum(np.array(f.shape),np.array(h.shape))
   if (f.dtype == 'complex') or (h.dtype == 'complex'):
       g = np.zeros(gs,dtype='complex')
   else:
       g = np.zeros(gs)

   f1 = g.copy()
   f1[f_ind]=f[f_ind]

   if f.ndim == 1:
     (W,) = gs
     col = np.arange(W)
     for cc in h_ind[0]:
        g[:] += f1[(col-cc)%W] * h[cc]

   elif f.ndim == 2:
     H,W = gs
     row,col = np.indices(gs)
     for rr,cc in np.transpose(h_ind):
        g[:] += f1[(row-rr)%H, (col-cc)%W] * h[rr,cc]

   else:
     Z,H,W = gs
     d,row,col = np.indices(gs)
     for dd,rr,cc in np.transpose(h_ind):
        g[:] += f1[(d-dd)%Z, (row-rr)%H, (col-cc)%W] * h[dd,rr,cc]
   return g
from numpy import *

def iapconv(f, h):

    f, h = asarray(f), asarray(h,dtype=float)
    #faux, haux = ravel(f), ravel(h)

    s = f.shape
    # Checking the shape of the image F.
    if len(f.shape) == 1:
        f = f[newaxis,newaxis,:]
    elif len(f.shape) == 2:
        f = f[newaxis,:,:]

    # Checking the shape of the image H.
    if len(h.shape) == 1:
        h = h[newaxis,newaxis,:]
    elif len(h.shape) == 2:
        h = h[newaxis,:,:]

    # Getting the dimensions of images F and H
    (fslices, frows, fcols) = f.shape
    (hslices, hrows, hcols) = h.shape

    ds1 = int((hslices-1)/2.)
    ds2 = hslices - ds1

    dr1 = int((hrows-1)/2.)
    dr2 = hrows - dr1

    dc1 = int((hcols-1)/2.)
    dc2 = hcols - dc1

    p = concatenate((concatenate((f[-ds2+1::,:,:], f)), f[0:ds1,:,:]))
    p = concatenate((concatenate((p[:,-dr2+1::,:], p), 1), p[:,0:dr1,:]), 1)
    p = concatenate((concatenate((p[:,:,-dc2+1::], p), 2), p[:,:,0:dc1]), 2)

    g = zeros((fslices,frows,fcols))

    for i in range(hslices):
        for j in range(hrows):
            for k in range(hcols):
                hw = h[hslices-i-1, hrows-j-1, hcols-k-1]
                if (hw):
                    g = g + h[hslices-i-1,hrows-j-1,hcols-k-1] * p[i:fslices + i,j:frows + j, k:fcols + k]
    g.shape = s
    return g


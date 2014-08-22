# -*- encoding: utf-8 -*-
# Module iapconv2

def iapconv2(f,h):
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

